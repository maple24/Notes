## Django vs Django RestFramework

> You can use Django only to build a fully functional web app without using any frontend frameworks, such as React, Angular, etc. Doing so, you have used Django for both backend and frontend. Actually, doing like this, you do not have the concept of backend and frontend. Your web app is just your web app, and that is it.

> However, if you want your frontend to look fancy with complex CSS decoration, you may want to consider using frontend frameworks (React, Angular). Of course, you can use Django alone to make your frontend looks fancy too, but you have to write a lot of code to do so, and Django template is not popularly used comparing to frontend frameworks.

> Now, let’s say you want to use a frontend framework. If you do not have a REST API, and your frontend code try to request data from one of your URLs, you will get a string data or an HTML page like what you get from using curl, it is not useful to get that data for your frontend. However, if you have a REST API, your backend data will be serialized in the way that your frontend code can understand and deserialize the returned data into some data objects like dictionary which you can use right the way.

> You can use Django alone to make REST APIs, but you have to write more code and do more design like one of the comment above showing in the example. By using Django Rest Framework, you can write less code and reuse your code better.

> Also, I think you may want to look into the difference between API vs REST API. They are using interchangeably, but they are not the same. For example, when you are using Django, you are using the Django APIs. REST(ful) API which is just one type of API is used for client-server web developments.


## Glossary
1. serializer(django rest framework module)

Transfer database complex data into python json type data.
Originally, database data need be transfered manually.
```sh
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
```sh
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


## Commands
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