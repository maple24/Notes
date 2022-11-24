# TBD
- websocket proxy on nginx and vite.config.js
- websocket server on python backend

## Python server example
```sh
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
```sh
<script setup>
  import client from './api/websocket';

  client.onopen = () => {
    console.log('open websocket');
  };
</script>

```