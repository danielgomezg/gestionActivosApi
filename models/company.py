from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.ext.hybrid import hybrid_property


class Company(Base):
    __tablename__ = 'compania'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    rut = Column(String, unique=True, nullable=False)
    country = Column(String, nullable=False)

    #Relacion con sucursales
    sucursales = relationship('Sucursal', back_populates='company')
    sucursales_count_var = None

    #Relacion con usuario
    users = relationship('Usuario', back_populates='company')

    @hybrid_property
    def sucursales_count(self):
        return len(self.sucursales)


# from sqlalchemy import Table, Column
# from sqlalchemy.sql.sqltypes import Integer, String
# #from database import meta, engine
# from database import Base
#
# class Company(Base):
#     __tablename__ = 'companies'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, unique=True)
