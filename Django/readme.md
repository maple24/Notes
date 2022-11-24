## Django vs Django RestFramework

> You can use Django only to build a fully functional web app without using any frontend frameworks, such as React, Angular, etc. Doing so, you have used Django for both backend and frontend. Actually, doing like this, you do not have the concept of backend and frontend. Your web app is just your web app, and that is it.

> However, if you want your frontend to look fancy with complex CSS decoration, you may want to consider using frontend frameworks (React, Angular). Of course, you can use Django alone to make your frontend looks fancy too, but you have to write a lot of code to do so, and Django template is not popularly used comparing to frontend frameworks.

> Now, let’s say you want to use a frontend framework. If you do not have a REST API, and your frontend code try to request data from one of your URLs, you will get a string data or an HTML page like what you get from using curl, it is not useful to get that data for your frontend. However, if you have a REST API, your backend data will be serialized in the way that your frontend code can understand and deserialize the returned data into some data objects like dictionary which you can use right the way.

> You can use Django alone to make REST APIs, but you have to write more code and do more design like one of the comment above showing in the example. By using Django Rest Framework, you can write less code and reuse your code better.

> Also, I think you may want to look into the difference between API vs REST API. They are using interchangeably, but they are not the same. For example, when you are using Django, you are using the Django APIs. REST(ful) API which is just one type of API is used for client-server web developments.