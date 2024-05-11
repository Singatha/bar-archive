from slqalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:example@psql-bar-archive-service-db/barArchiveDB")
sqlacodegen postgresql://postgres:example@psql-bar-archive-service-db/barArchiveDB --outfile ./models/db.py