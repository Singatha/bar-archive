# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Beverage(Base):
    __tablename__ = 'beverage'

    beverage_id = Column(Integer, primary_key=True, server_default=text("nextval('beverage_beverage_id_seq'::regclass)"))
    beverage_name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))


class Ingredient(Base):
    __tablename__ = 'ingredient'

    ingredient_id = Column(Integer, primary_key=True, server_default=text("nextval('ingredient_ingredient_id_seq'::regclass)"))
    beverage_id = Column(ForeignKey('beverage.beverage_id', ondelete='CASCADE'))
    ingredient_name = Column(String(255), nullable=False)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))

    beverage = relationship('Beverage')


class Method(Base):
    __tablename__ = 'method'

    method_id = Column(Integer, primary_key=True, server_default=text("nextval('method_method_id_seq'::regclass)"))
    beverage_id = Column(ForeignKey('beverage.beverage_id', ondelete='CASCADE'))
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))

    beverage = relationship('Beverage')
