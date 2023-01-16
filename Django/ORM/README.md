# Django ORM vs SQLAlchemy

## What is an ORM?
ORM stands for Object Relational Mapping. The ORM is here to connect between the programming language to the database in order to simplify the process of creating an application that relies on data

- Object: ORM stands for Object Relational Mapping.
- Relational: This part represents the RDBMS database you're using (Relational Database Manager System). There are numerous popular relational databases out there, but you're probably usin MSSQL, MySQL, Oracle Database, PostgreSQL, MariaDB, PerconaDB, ir TokuDB. What's common between most relational databases is their relational structures (tables, columns, keys, constraints, etc.).
- Mapping: This final part represents the bridge and connection between the two previous parts.

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

## commands
```python
from django.db import connection
posts = Student.objects.all()

print(posts.query)

print(connection.queries) # get execution time of database, how long the query is gonna take

posts = Student.objcts.filter(surname__startswith='austin')
```