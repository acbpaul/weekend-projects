class GameClient:
    def __init__(self, server_address):
        self.server_address = server_address
        self.connection = None
        self.player = None

    def connect(self):
        pass

    def disconnect(self):
        pass

    def send_message(self, message):
        pass

    def receive_message(self):
        pass

    def handle_server_message(self, message):
        pass

    def user_input(self):
        pass