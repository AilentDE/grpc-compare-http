from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc

class ExampleService(service_pb2_grpc.ExampleServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloResponse(message=f'Hello, {request.name}!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_pb2_grpc.add_ExampleServicer_to_server(ExampleService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
