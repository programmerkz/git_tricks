from grpc import Grpc

class Conainer:
    def __init__(self):
        self.info = "container"
        self.grpc = Grpc()


if __name__ == '__main__':
    c = Container()
    print('Ok. Container created.')
