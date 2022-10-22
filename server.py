import asyncio
 
import websockets

# create handler for each connection
 
async def handler(websocket, path):
 
    data = await websocket.recv()
 
    reply = f"Data recieved as:  {data}!"
    a = input()
 
    await websocket.send(reply)
    await websocket.send(a)
 
 
 
start_server = websockets.serve(handler, "localhost", 5000)
 
 
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()
