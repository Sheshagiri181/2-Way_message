# server.py
import asyncio
import websockets

async def chat(websocket):
    print("Client connected.")
    try:
        while True:
            msg = await websocket.recv()
            print(f"Client: {msg}")
            reply = input("You (Server): ")
            await websocket.send(reply)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

async def main():
    async with websockets.serve(chat, "0.0.0.0", 6789):
        print("Server started at ws://0.0.0.0:6789")
        await asyncio.Future()  # Keep running

asyncio.run(main())



import asyncio
import websockets
async def talk():
    uri = "ws://-------------:6789"# Replace with your server's IP address
    print("Connecting to server...")
    async with websockets.connect(uri) as websocket:
        print("Connected to server.")
        try:
            while True:
                msg = input("You (Client): ")
                await websocket.send(msg)
                reply = await websocket.recv()
                print(f"Server: {reply}")
        except websockets.exceptions.ConnectionClosed:
            print("Server disconnected.")
asyncio.run(talk())

