from grpc import Grpc

class Container:
    def __init__(self):
        self.info = "container"
        self.grpc = Grpc(5051)


if __name__ == '__main__':
    c = Container()
    print('Ok. Container created.')
