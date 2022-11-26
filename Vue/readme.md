# Table of contents
- [Table of contents](#table-of-contents)
  - [Reference](#reference)
  - [alias\&proxy](#aliasproxy)
  - [computed vs methods](#computed-vs-methods)
  - [computed vs watcher](#computed-vs-watcher)
  - [emit](#emit)
  - [environment variables](#environment-variables)
  - [errors](#errors)
  - [high order array functions](#high-order-array-functions)
  - [icons](#icons)
  - [object vs function](#object-vs-function)
  - [props](#props)
  - [prevent](#prevent)
  

## Reference
---
[javascript](https://wesbos.com/javascript/01-the-basics/variables-and-statements/#statements-and-semi-colons-in-javascript)

## alias&proxy
---
```javascript
// in vite.config.js file
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
});
```

## computed vs methods
---
> A cool thing of the computed properties is that they are cached, that’s mean that the function will run only once until the values don’t change again also if it’s called many times in the same template.

`Methods`:
They are static functions usually used to react to events which happen in the DOM and they accept arguments.
They are incredibly useful for connecting functionality to events, or even just creating small parts of logic to be reused. You can call a method inside another method, they are very versatile!

`Computed properties`:
They **don’t accept arguments** and they are very handy for composing new data from existing sources, they get dynamic values based on other properties.


## computed vs watcher
---
`watcher` is usually used for **more complex logics**, **asyncronous reqeusts**.

`computed properties` are **more appropriate in most cases**, there are times when a custom watcher is necessary. That’s why Vue provides a more generic way to react to data changes through the watch option. This is most useful when you want to perform asynchronous or expensive operations in response to changing data.

## emit
---
understanding: transfer functions to upper level components
```javascript
// on subcomponent:
@submit="onSubmit"
onsubmit:() {
    this.$emit('eventname', value)
}
// on rootcomponent
eventname:(value){
    this.data.push(value)
}
```

## environment variables
---
![env1](assets/env1.png)
![env2](assets/env2.png)

## errors
---


## high order array functions
---
- definition: functions take another function as parameter
- example: for each

## icons
---
[heroicons](https://heroicons.com/)


## object vs function
---
![data must be a function](assets/object.png)
The reason for this is to ensure that for each individual instance of the reusable child component, there is a unique object containing all of the data being operated on. If, in a child component, you instead use data: { ... }, that same data object will be shared between the child components which can cause some nasty bugs.

## props
---
understanding: if props is an object or array, data binding is required; if props is a string or number, no data binding needed.

## prevent
---
```javascript
// prevent default function of click 
@click.prevent="submit"
```