# Table of contents
- [Table of contents](#table-of-contents)
  - [reference](#reference)
  - [Django vs Django RestFramework](#django-vs-django-restframework)
  - [websocket channel](#websocket-channel)
  - [why channel](#why-channel)
    - [routing](#routing)
    - [ASGI](#asgi)
    - [client](#client)
    - [django consumer](#django-consumer)
  - [filter](#filter)
  - [general steps](#general-steps)
  - [html variable/condition](#html-variablecondition)
  - [html style](#html-style)
  - [migrate](#migrate)
  - [shell](#shell)
  - [Django admin](#django-admin)
  - [glossary](#glossary)
  - [commands](#commands)
  - [examples](#examples)
  - [FQA](#fqa)

## reference
[django-channels-official](https://channels.readthedocs.io/en/stable/introduction.html#turtles-all-the-way-down)
[django-channels](https://arunrocks.com/understanding-django-channels/)

## Django vs Django RestFramework
> You can use Django only to build a fully functional web app without using any frontend frameworks, such as React, Angular, etc. Doing so, you have used Django for both backend and frontend. Actually, doing like this, you do not have the concept of backend and frontend. Your web app is just your web app, and that is it.

> However, if you want your frontend to look fancy with complex CSS decoration, you may want to consider using frontend frameworks (React, Angular). Of course, you can use Django alone to make your frontend looks fancy too, but you have to write a lot of code to do so, and Django template is not popularly used comparing to frontend frameworks.

> Now, let’s say you want to use a frontend framework. If you do not have a REST API, and your frontend code try to request data from one of your URLs, you will get a string data or an HTML page like what you get from using curl, it is not useful to get that data for your frontend. However, if you have a REST API, your backend data will be serialized in the way that your frontend code can understand and deserialize the returned data into some data objects like dictionary which you can use right the way.

> You can use Django alone to make REST APIs, but you have to write more code and do more design like one of the comment above showing in the example. By using Django Rest Framework, you can write less code and reuse your code better.

> Also, I think you may want to look into the difference between API vs REST API. They are using interchangeably, but they are not the same. For example, when you are using Django, you are using the Django APIs. REST(ful) API which is just one type of API is used for client-server web developments.

## websocket channel
![channel](assets/django-channels.png)
> A channel layer is a kind of communication system. It allows multiple consumer instances to talk with each other, and with other parts of Django.
```python
## settings.py
# enable the channel layer, which allows multiple consumer instances to talk with each other.

# Note that you could the Redis as the backing store. To enable Redis, you could use Method 1 if you want Redis Cloud or Method 2 for local Redis. In this guide, I used Method 3 — In-memory channel layer — which is helpful for testing and for local development purposes.
CHANNEL_LAYERS = {
    'default': {
        ### Method 1: Via redis lab
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #     "hosts": [
        #       'redis://h:<password>;@<redis Endpoint>:<port>' 
        #     ],
        # },

        ### Method 2: Via local Redis
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #      "hosts": [('127.0.0.1', 6379)],
        # },

        ### Method 3: Via In-memory channel layer
        ## Using this method.
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}
```

## why channel
> However if you open a second browser tab to the same room page at http://127.0.0.1:8000/chat/lobby/ and type in a message, the message will not appear in the first tab. For that to work, we need to have multiple instances of the same ChatConsumer be able to talk to each other. Channels provides a channel layer abstraction that enables this kind of communication between consumers.

### routing 
> A Channels routing configuration is an ASGI application that is similar to a Django URLconf, in that it tells Channels what code to run when an HTTP request is received by the Channels server.
```python
# mysite/asgi.py
import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)
```
### ASGI
> add the channels library to the list of installed apps, in order to enable an **ASGI versions of the runserver command**.
```python
# mysite/settings.py
INSTALLED_APPS = [
    'channels',
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# mysite/settings.py
ASGI_APPLICATION = "mysite.asgi.application"
```
### client
```javascript
const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
```
### django consumer
> When a user posts a message, a JavaScript function will transmit the message over WebSocket to a ChatConsumer. The ChatConsumer will receive that message and forward it to the group corresponding to the room name. Every ChatConsumer in the same group (and thus in the same room) will then receive the message from the group and forward it over WebSocket back to JavaScript, where it will be appended to the chat log.
```python
# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
```
```python
# asyncronous consumer
# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
```

## filter
```python
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']
```
```sh
http://example.com/api/products?category=clothing&in_stock=True
```
- filter fields
```python
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'in_stock')
```
- filter class
```python
class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    class Meta:
        model = Product
        fields = ['category', 'in_stock']

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
```
- customized filter
```python
class TaskFilter(django_filters.rest_framework.FilterSet):
    branch = django_filters.CharFilter(field_name='branch', method='branch_filter')
    
    class Meta:
        model = models.Task
        fields = '__all__'
    
    def branch_filter(self, queryset, name, value):
        query = Q()
        for branch in value.split(","):
            query |= Q(branch=branch)
        return queryset.filter(query)
```


## general steps
1. django-admin startproject lecture3
2. python manage.py startapp hello
3. add hello into settings/INSTALLED_APPS
4. create templates/tasks/index.html
5. Add functions in views.py
6. create urls.py in hello directory
7. create route for hello
8. add hello urls into urls.py

## html variable/condition
1. {{ name }}
2. {% for task in tasks %} ... {% endfor %}
3. {% if newyear %} ... {% else %} ... {% endif %}
4. {% block body %} {% endblock %}
5. {% url 'tasks:add' %}
6. {% csfr_token %}
7. {% empty %}

## html style
1. {% load static %}
2. <link rel="stylesheet" href="{% static 'newyear/style.css' %}">

## migrate
1. python manager.py makemigrations: create migrations based on models
2. python manager.py migrate: apply changes to django database

## shell
1. python manager.py shell
2. Flights.objects.all()
3. flights.first()
4. Airport.objects.filter(city="New York")
5. Airport.objects.filter(city="New York").first()
6. Airport.objects.get(city="New York")
7. jfk = Airport(city="New York", code="JFK")
8. jfk.save()

## Django admin
```sh
python manager.py createsuperuser
```

## glossary
1. serializer(django rest framework module)

Transfer database complex data into python json type data.
Originally, database data need be transfered manually.
```python
def book_list(requet):
    books = books.objects.all()
    books_python = list(books(value()))
    return Jsonresponse({
        "books": books_python
    })
# ==================================
@api_view(['GET'])
def book_list(request):
    books = books.objects.all()
    serializer = BookSerializer(books)
    return Response(serializer.data)
```

2. action decorator
```python
class FooViewset(viewsets.ModelViewSet):
	queryset = Foo.objects.all()
	serializer_class = FooSerializer

	@action(detail=False, methods=['get'])
	def get_bars(self, request, *args, **kwargs):	
		# do anything
		# but it should return an HTTP response

# detail: It’s a boolean type argument that tells the router to accept a pk in the URL or not. If set to True, the router will create its URL with pk required.
# methods: it is a list type argument that accepts a list of HTTP methods that are valid for this action. If the method is only set to [‘get’] then all the HTTP requests other than GET will get a 405 (Method not allowed) response.
```

3. readonly id
   `id will be auto-generated`


## commands
1. python shell
```sh
python manage.py shell
```
2. dbshell
```sh
python manage.py dbshell
# show all tables
.tables
# quit
.quit
```

## examples
```python
from django.db import models
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
    # property can be called like, Product.objects.all()[0].sale_price
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    # method will be called like, Product.objects.all()[0].get_discount() 
    # does not have to start with get
    def get_discount(self):
        return "122"
# ============================================
from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "get_discount",
            "my_discount"
        ]
    
    # has to start with get
    def get_my_discount(self, obj):
        return obj.get_discount()
```

## FQA
1. [HTTP GET with request body](https://stackoverflow.com/questions/978061/http-get-with-request-body)
