from grpc import Grpc

class Conainer:
    def __init__(self):
        self.info = "container"
        self.grpc = Grpc()
