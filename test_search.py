import grpc

from protobuf import serve_pb2, serve_pb2_grpc


chanel = grpc.insecure_channel("tstsv.ddns.net:9090")
stub = serve_pb2_grpc.SearchStub(chanel)
res = stub.Search(serve_pb2.Data(
    message="covid", result_number=3))
print(res)
