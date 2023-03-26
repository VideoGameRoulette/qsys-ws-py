import websocket

class WebsocketRelay:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.ws = None

    def on_message(self, ws, message):
        print("Message: ", message)

    def on_error(self, ws, error):
        print("Error:", error)

    def on_close(self, ws):
        print("WebSocket closed")

    def on_open(self, ws):
        print("WebSocket opened")

    def connect(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(f"ws://{self.ip_address}:{self.port}",
                                        on_message=self.on_message,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def close(self):
        self.ws.close()

    def __del__(self):
        if self.ws:
            self.close()

if __name__ == "__main__":
    ws = WebsocketRelay("localhost", "4445")
    ws.connect()
