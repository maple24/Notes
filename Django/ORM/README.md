# Django ORM vs SQLAlchemy

## What is an ORM?
ORM stands for Object Relational Mapping. The ORM is here to connect between the programming language to the database in order to simplify the process of creating an application that relies on data

- Object: ORM stands for Object Relational Mapping.
- Relational: This part represents the RDBMS database you're using (Relational Database Manager System). There are numerous popular relational databases out there, but you're probably usin MSSQL, MySQL, Oracle Database, PostgreSQL, MariaDB, PerconaDB, ir TokuDB. What's common between most relational databases is their relational structures (tables, columns, keys, constraints, etc.).
- Mapping: This final part represents the bridge and connection between the two previous parts.

## extensible data modeling
Senario: types of products with slightly different features, if just using one table there are many 'nulls' in some fields.

Solutions:
- Concrete Table Inheritance
> Create a new table for every single product
  - Disadvantages:
    - Field definition duplicated
    - Multiple SELECT with UNION
- Multi-table Inheritance
> Inherite a generic table
- Abstract models
> Inherite an abstract generic table
```python
class Product(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model_in': ('book', 'cupboard')})
    object_id = models.PositiveIntergerField()
    item = GenericForeignKey('content_type', 'object_id')

class Base(models.Model):
    title = models.CharField()

    class Meta:
        abstract = True

class Book(Base):
    pass

class Cupboard(Base):
    pass
```
- Polymorphism

## OR query
```python
# 1. use |
posts = Student.objcts.filter(surname__startswith='austin') | Student.objects.fiter(surname__startswith='baldwin')

# 2. use Q objects
from django.db.models import Q
posts = Student.objcts.filter(Q(surname__startswith='austin') | Q(surname__startswith='baldwin'))

# not
~Q()
```

## AND query
```python
# 1. use &
# student with surname 'baldin' in classroom 3
posts = Student.objects.filter(classroom=3) & Student.objects.fiter(surname__startswith='baldwin')

# 2. use Q objects
posts = Student.objects.filter(Q(surname__startswith='baldwin') & Q(classroom=3))
```

## UNION query
```python
# should have the same field and data type
posts = Student.objects.all().values_list('firstname').union(Teacher.objects.all().value_list('firstname'))
```

## NOT query
```python
# 1. exclude
# 2. ~Q
```

## SELECT & OUTPUT individual fields
```python
# only print the firstname of the selected student
posts = Student.objects.filter(classroom=1).only('firstname')
```

## RAW query
```python
posts = Student.objects.raw("SELECT * FROM student_student")
```

## model inheritance
- abstract models
> used when you have common information needed for number of other models
```python
# the BaseItem does not create an actual table, so there are two tables: ItemA and ItemB
class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTImeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['title']

class ItemA(BaseItem):
    content = models.TextField()

    class Meta(BaseItem.Meta):
        ordering = ['-created']

class ItemB(BaseItem):
    name = models.charField()
```
- multi-table model inheritance
> every model is a model all by itself, one-to-one link is created automatically
- proxy models
> change the behavior of a model, operates on the original model
```python
# BookOrders does not ceate an actual table
class BookContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class BookOrders(BookContent):
    class Meta:
        proxy = True
        ordering = ['created']
    
    def created_on(self):
        return timezone.now() - self.created
```

## django debug toolbar
provide pannels to show debug information
- system information
- timing
- setting/configurations
- header
- SQL
- templates, includes
```python
# pip install django-debug-toolbar
# settings.py
INSTALLED_APPS = [
    'debug_toolbar'
]
STATIC_URL = '/static/

# urls.py
import debug_toolbar
urlpatterns = [
    path('__debug__', include(debug_toolbar.urls))
]

# enable middleware
# in settings.py
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

# set internal ips
# in settings.py
INTERNAL_IPS = [
    '127.0.0.1'
]

# show toolbars
DEBUG_TOOLBAR_PANELS = [

]
```

## performing custom SQL directly
avoid model layer
```python
import django.db.connection
cursor = connection.cursor()
cursor.execute(sql)
r = cursor.fetchone() 
r = cursor.fetchall()
```

## setup multiple database
```python
# in settings.py
DATABSE = {
    'default': {},
    'users_db': {
        'ENGINE': 'django.db.backends.sqlite3'
        'NAME': BASE_DIR / 'users.db.sqlite3'
    }
}

# create a folder called routers
# create db_routers.py in routers
# in db_routers.py
class AuthRouter:
    route_app_labels = {'auth', 'contenttypes'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

# in settings
DATABASE_ROUTERS = ['routers.db_routers.AuthRouter',]

Author.objects.using('users_db').all()
```

## commands
```sh
exact
iexact
contains
icontains
in
gt
gte
lt
lte
startswith
istartswith
endswith
iendswith
range
year
month
day
week_day
isnull
search
regex
iregex
```
```python
from django.db import connection
posts = Student.objects.all()

# show query
print(posts.query)

# get execution time of database, how long the query is gonna take
print(connection.queries) 

posts = Student.objcts.filter(surname__startswith='austin')

posts = Student.objcts.exclude(surname__startswith='austin')

# show different types of values
posts = Student.objects.all().values_list('firstname')
posts = Student.objects.all().values('firstname')

# operator
# >, < does not work in django
# gt (greater than)
# gte (greater than or equal)
# lt (less than)
# lte (less than or equal)

# join three tables, eliminate too many queries
products = Product.objects.all().select_related('book', 'cupboard')
products = Product.objects.all().prefetch_related('book', 'cupboard')
```