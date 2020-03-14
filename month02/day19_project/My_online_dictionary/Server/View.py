from Server.Controls import Server_Controls


class Server_View:
    def __init__(self, host="192.168.1.4", post=8844):
        self.server = Server_Controls(host, post)

    def show(self):
        while True:
            print("等待链接.....")
            self.server.show()
