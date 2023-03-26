from websocket_relay import WebsocketRelay

# create an instance of the WebsocketRelay class
ws = WebsocketRelay("localhost", "4445")
ws.connect()
ws.close()
