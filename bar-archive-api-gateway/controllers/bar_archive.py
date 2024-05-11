import grpc
from compiled_protos import bar_archive_pb2
from compiled_protos import bar_archive_pb2_grpc

def get_beverage_by_id(beverage_id):
  with grpc.insecure_channel("bar-archive-service-backend:50051") as channel:
    stub = bar_archive_pb2_grpc.BarArchiveServiceStub(channel)
    bar_archive = bar_archive_pb2.GetBeverageByIDRequest(beverage_id=beverage_id)
    print(bar_archive)
    return stub.GetBeverageByID(bar_archive)
