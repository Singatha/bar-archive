from concurrent import futures

import grpc

from compiled_protos import bar_archive_pb2
from compiled_protos import bar_archive_pb2_grpc

from sqlalchemy import create_engine
from models import db
from sqlalchemy import select

engine = create_engine("postgresql://postgres:example@psql-bar-archive-service-db/barArchiveDB")

class BarArchiveServiceServicer(bar_archive_pb2_grpc.BarArchiveServiceServicer):
    def GetBeverageByID(self, request, context):
        print(request.beverage_id)
        with engine.connect() as conn:
            result = conn.execute(select(db.Beverage).where(db.Beverage.beverage_id == request.beverage_id))
            print(result)  
        return bar_archive_pb2.GetBeverageByIDResponse(beverages={}, ingredient={}, method={})
