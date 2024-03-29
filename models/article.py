from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship
from datetime import date

class Article(Base):
    __tablename__ = 'articulo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description= Column(String, nullable=True)
    code = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    count_active = Column(Integer, default=0, nullable=False)
    creation_date = Column(Date, default=date.today, nullable=False)
    removed = Column(Integer, default=0, nullable=False)

    company_id = Column(Integer, ForeignKey('compania.id'))
    company = relationship('Company', back_populates='articles')

    category_id = Column(Integer, ForeignKey('categoria.id'))
    category = relationship('Category', back_populates='articles')

    actives = relationship('Active', back_populates='article')

    # Relacion con historial
    historial = relationship('History', back_populates='article')

