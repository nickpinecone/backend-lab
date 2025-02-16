import grpc
from greet_pb2 import ExampleRequest
from greet_pb2_grpc import ExampleStub

channel = grpc.insecure_channel('localhost:5000')
stub = ExampleStub(channel)

request = ExampleRequest()
request.name = "Name"
reply = stub.ExampleMethod(request)

print(reply)

