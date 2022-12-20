# Table of contents
- [Table of contents](#table-of-contents)
  - [reference](#reference)
  - [AJAX](#ajax)
  - [axios](#axios)
    - [use axios](#use-axios)
    - [fetch vs axios](#fetch-vs-axios)
    - [simultaneous requests](#simultaneous-requests)
    - [intercepting requests and responses](#intercepting-requests-and-responses)
  - [bearer token](#bearer-token)
  - [blob](#blob)
  - [bundling](#bundling)
  - [camel case](#camel-case)
  - [commonJS vs ES module](#commonjs-vs-es-module)
  - [CORS](#cors)
  - [CDN](#cdn)
  - [CRUD](#crud)
  - [cookie vs localstorage](#cookie-vs-localstorage)
  - [curl](#curl)
  - [docker daemon](#docker-daemon)
  - [HMR(hot module replacement)](#hmrhot-module-replacement)
  - [JSX](#jsx)
  - [vite](#vite)
  - [stores in frontend](#stores-in-frontend)

## reference
[ultimate guide to enabling cross origin resouce sharing](https://blog.logrocket.com/the-ultimate-guide-to-enabling-cross-origin-resource-sharing-cors/)

## AJAX
> Ajax is short for "Asynchronous JavaScript and XML". AJAX is not a programming language. AJAX allows web pages to be updated asynchronously by exchanging data with a web server behind the scenes. This means that it is possible to update parts of a web page without reloading the whole page.

> Ajax is a set of web development techniques using many web technologies on the client side to create asynchronous web applications. With Ajax, web applications can send and retrieve data from a server asynchronously (in the background) without interfering with the display and behaviour of the existing page. By decoupling the data interchange layer from the presentation layer, Ajax allows web pages and, by extension, web applications, to change content dynamically without the need to reload the entire page. In practice, modern implementations commonly utilize JSON instead of XML.

> Ajax is not a single technology, but rather a group of technologies. HTML and CSS can be used in combination to mark up and style information. The webpage can then be modified by JavaScript to dynamically display — and allow the user to interact with — the new information. The built-in XMLHttpRequest object, or since 2017 the new “fetch()” function within JavaScript, is commonly used to execute Ajax on webpages, allowing websites to load content onto the screen without refreshing the page. Ajax is not a new technology, or different language, just existing technologies used in new ways.
- Asynchronous JavaScript And XML
- Making background HTTP requests using JavaScript
- Handling the response of those HTTP requests with JavaScript
- No page refresh necessary

> AJAX allows us to build Single Page Applications. (An SPA is a web application or web site that interacts with the user by dynamically rewriting the current page rather than loading entire new pages from a server.) SPAs mean no reload or “refresh” within the user interface.

![ajax](assets/ajax.png)

## axios
> Axios is a popular, **promise-based HTTP client** that sports an easy-to-use API and can be used in both the browser and Node.js. Making HTTP requests to fetch or save data is one of the most common tasks a client-side JavaScript application will need to do.

### use axios
```sh
npm install axios
```
> Making an HTTP request is as easy as passing a config object to the Axios function. In its simplest form, the object must have a URL property; if no method is provided, GET will be used as the default value.

> Once an HTTP request is made, Axios returns a promise that is either fulfilled or rejected, depending on the response from the backend service. To handle the result, you can use the then() method, handle error use catch().

### fetch vs axios
- Fetch API is built into the window object and therefore doesn’t need to be installed as a dependency or imported in client-side code.
- Axios needs to be installed as a dependency. However, it automatically transforms JSON data for you, thereby avoiding the two-step process of making a .fetch() request and then a second call to the .json() method on the response.

### simultaneous requests
> One of Axios' more interesting features is its ability to make multiple requests in parallel by passing an array of arguments to the axios.all() method. This method returns a single promise object that resolves only when all arguments passed as an array has resolved. 

### intercepting requests and responses
> You can examine and change HTTP requests from your program to the server and vice versa, which is useful for a variety of implicit tasks, such as logging and authentication. Interceptors receive the entire response object or request config.

```javascript
service.interceptors.request.use(
  config => {
    // do something before request is sent

    if (store.getters.token) {
      // let each request carry token
      // ['X-Token'] is a custom headers key
      // please modify it according to the actual situation
      config.headers['Authorization'] = getToken()
    }
    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)
```

## bearer token
> Bearer authentication (also called token authentication) is an HTTP authentication scheme that involves security tokens called bearer tokens. The name “Bearer authentication” can be understood as “give access to the bearer of this token.” The bearer token is a cryptic string, usually generated by the server in response to a login request. The client must send this token in the Authorization header when making requests to protected resources:

Authorization: Bearer

## blob
> The Blob object represents a blob, which is a file-like object of immutable, raw data; they can be read as text or binary data, or converted into a ReadableStream so its methods can be used for processing the data.

> Blobs can represent data that isn't necessarily in a JavaScript-native format. The File interface is based on Blob, inheriting blob functionality and expanding it to support files on the user's system.

## bundling
> Before ES modules were available in browsers, developers had no native mechanism for authoring JavaScript in a modularized fashion. This is why we are all familiar with the concept of "bundling": using tools that crawl, process and concatenate our source modules into files that can run in the browser.

## camel case
```
addBlog
changeTitle
```

## commonJS vs ES module
> In modern software development, modules organize software code into self-contained chunks that together make up a larger, more complex application.
In the browser JavaScript ecosystem, **the use of JavaScript modules depends on the import and export statements; these statements load and export EMCAScript modules (or ES modules), respectively.**

> The ES module format is the official standard format to package JavaScript code for reuse and most modern web browsers natively support the modules.
**Node.js, however, supports the CommonJS module format by default. CommonJS modules load using require(), and variables and functions export from a CommonJS module with module.exports.**

> The ES module format was introduced in Node.js v8.5.0 as the JavaScript module system was standardized. Being an experimental module, the --experimental-modules flag was required to successfully run an ES module in a Node.js environment.

> However, starting with version 13.2.0, Node.js has stable support of ES modules.

## CORS
> CORS (Cross-Origin Resource Sharing) is a system, consisting of transmitting HTTP headers, that determines whether browsers block frontend JavaScript code from accessing responses for cross-origin requests.

## CDN
![CDN](assets/CDN.png)

## CRUD
- c: create
- r: read
- u: update
- d: delete

## cookie vs localstorage
对前端来说作为临时存储，存储在cookie里或者localstorage都可以。
![cookie vs localstorage](assets/cookievslocalstorage.png)

## curl
> cURL, which stands for client URL, is a command line tool that developers use to transfer data to and from a server. 
![curl](assets/curl.png)

## docker daemon
- The Docker daemon is a service that runs on your host operating system.
- It currently only runs on Linux because it depends on a number of Linux kernel features, but there are a few ways to run Docker on MacOS and Windows too.

## HMR(hot module replacement)
> HMR is a way of exchanging modules in a running application (and adding/removing modules). You basically can update changed modules without a full page reload.

## JSX
> ReactJS relies on **JavaScript Expressions**, popularly known as JSX. In simple terms, JSX is a means of adding HTML code within the JavaScript code.

## vite
> As we build more and more ambitious applications, the amount of JavaScript we are dealing with is also increasing dramatically. It is not uncommon for large scale projects to contain thousands of modules. We are starting to hit a performance bottleneck for JavaScript based tooling: **it can often take an unreasonably long wait (sometimes up to minutes!) to spin up a dev server, and even with Hot Module Replacement (HMR), file edits can take a couple of seconds to be reflected in the browser**. The slow feedback loop can greatly affect developers' productivity and happiness.

vite basically solves two problems:
- slow server start: Vite improves the dev server start time by first dividing the modules in an application into two categories: dependencies and source code.
- slow updates: In Vite, HMR is performed over native ESM. When a file is edited, Vite only needs to precisely invalidate the chain between the edited module and its closest HMR boundary (most of the time only the module itself), making HMR updates consistently fast regardless of the size of your application.
  
## stores in frontend
Isn't Redux just glorified global state?

> Of course it is. But the same holds for every database you have ever used. It is better to treat Redux as an in-memory database - which **your components can reactively depend upon.** Same as Vuex and pinia.