import time
import asyncio

NUM_REQUESTS = 100

### restful ###
import aiohttp
HTTP_URL = "http://localhost:8000/hello"

async def send_http_request(session, name):
    async with session.post(HTTP_URL, json={"name": name}) as response:
        return await response.json()

async def http_test():
    async with aiohttp.ClientSession() as session:
        tasks = [send_http_request(session, f"user{i}") for i in range(NUM_REQUESTS)]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"HTTP Average Time: {(end_time - start_time) / NUM_REQUESTS:.8f} seconds")
        # print(results)

### grpc ###
import grpc
from server import service_pb2, service_pb2_grpc
GRPC_URL = "localhost:50051"

async def send_grpc_request(stub, name):
    response = await stub.SayHello(service_pb2.HelloRequest(name=name))
    return response.message

async def grpc_test():
    async with grpc.aio.insecure_channel(GRPC_URL) as channel:
        stub = service_pb2_grpc.ExampleStub(channel)
        tasks = [send_grpc_request(stub, f"user{i}") for i in range(NUM_REQUESTS)]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"gRPC Average Time: {(end_time - start_time) / NUM_REQUESTS:.8f} seconds")
        # print(results)

if __name__ == '__main__':
    print("Requests number:", NUM_REQUESTS)
    asyncio.run(http_test())
    asyncio.run(grpc_test())
