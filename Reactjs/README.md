# Table of contents

- [Table of contents](#table-of-contents)
  - [Reference](#reference)
  - [how reactjs works](#how-reactjs-works)

## Reference

[How reactjs works](https://medium.com/@sweetpalma/gooact-react-in-160-lines-of-javascript-44e0742ad60f)

## how reactjs works

1. Elements: convert JSX to VDOM
2. Rendering: transform VDOM to actual DOM
3. Patching: a process of reconciliation of existing DOM with a freshly built VDOM tree
   - Build a fresh VDOM.
   - Recursively compare it with existing DOM.
   - Locate nodes that were added, removed or changed in any other way.
   - Patch them.
4. Components: components are like functions that return HTML elements

```javascript
// example function to convert javascript element into AST(vnode), in reactJs it is `React.createElement`
function h(nodeName, attributes, ...args) {
    let children = args.length ? [].concat(...args) : null;
    return { nodeName, attributes, children };
}

// render vnode to actual DOM
function render(vnode) {
    // Strings just convert to #text Nodes:
    if (vnode.split) return document.createTextNode(vnode);

    // create a DOM element with the nodeName of our VDOM element:
    let n = document.createElement(vnode.nodeName);

    // copy attributes onto the new node:
    let a = vnode.attributes || {};
    Object.keys(a).forEach(k => n.setAttribute(k, a[k]));

    // render (build) and then append child nodes:
    (vnode.children || []).forEach(c => n.appendChild(render(c)));

    return n;
}

// <div id="foo">Hello!</div>
// transcompiler like Babels can convert html-like syntax into javascript-like syntax
var foo = h('div', { id: "foo" }, 'Hello!')

console.log(foo);

var bar = render(foo)
console.log(bar);
```
