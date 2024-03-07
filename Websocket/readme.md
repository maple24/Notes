# TBD

- websocket proxy on nginx and vite.config.js
- websocket server on python backend

## Securing WebSocket Endpoints Against Cross-Site Attacks

[Securing WebSocket Endpoints Against Cross-Site Attacks](https://dev.solita.fi/2018/11/07/securing-websocket-endpoints.html)

## Python server example

```python
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"received message {message}")
        await websocket.send(f"received msg:{message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
```

## JS client example

```sh
# Websocket class is built-in, do not import 
let client = new WebSocket('ws://localhost:8765')

client.onopen = () => {
    console.log("connected to the server")
    client.send("hello")
}

client.onmessage = (event) => {
    console.log(event.data)
}
```

## VueJs example

```javascript
<script setup>
  import client from './api/websocket';

  client.onopen = () => {
    console.log('open websocket');
  };
</script>
```

```vue
<!-- deal with messages in websocket channel -->
websocketOnMessage(e) {
  const { method, content } = JSON.parse(e.data)
  if (method === 'log') {
    const task_id = content.task_id
    const log = content.content
    this.logContainer[task_id] = this.logContainer[task_id] == undefined ? '' : this.logContainer[task_id] + '>>' + log + '\r'
  } else if (method === 'agent_log') {
    const host = content.host
    const log = content.content
    this.agentLogContainer[host] = this.agentLogContainer[host] == undefined ? '' : this.agentLogContainer[host] + '>>' + log + '\r'
  }
},
```

## proxy

```javascript
// two ways to config websocket at frontend
// 1. ws:true
// 2. target: ws://localhost:8000
// ngnix do not have to config because it works same for http
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
        ws: true
        // rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // Proxying websockets or socket.io: ws://localhost:5173/ws -> ws://localhost:8000/ws
      // '/ws': {
      //   target: 'ws://localhost:8000',
      //   ws: true,
      //   // rewrite: (path) => path.replace(/^\/ws/, ''),
      // },
    },
  },
});
```
