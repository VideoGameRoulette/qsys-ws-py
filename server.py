import asyncio
import websockets

async def handle_message(websocket, path):
    async for message in websocket:
        print("Message: ", message)

async def main():
    print("Listening on localhost:4445")
    async with websockets.serve(handle_message, "localhost", 4445):
        await asyncio.Future()  # keep the server running

asyncio.run(main())