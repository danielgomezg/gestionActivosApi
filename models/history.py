from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship
from datetime import date


from models import  active, article, office, sucursal, category
#from models import article
#from models import office
#from models import sucursal
# from database import engine

# category.Base.metadata.create_all(bind=engine)
# active.Base.metadata.create_all(bind=engine)
# article.Base.metadata.create_all(bind=engine)
# sucursal.Base.metadata.create_all(bind=engine)
# office.Base.metadata.create_all(bind=engine)

class History(Base):
    __tablename__ = 'historial'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=True)
    name_user = Column(String, nullable=False)
    creation_date = Column(Date, default=date.today, nullable=False)
    #current_session_user_id = Column(Integer, nullable=False)

    #Relacion con empresa
    company_id = Column(Integer, ForeignKey('compania.id'), nullable=True)
    company = relationship('Company', back_populates='historial')

    # Relacion con sucursal
    sucursal_id = Column(Integer, ForeignKey('sucursal.id'), nullable=True)
    sucursal = relationship('Sucursal', back_populates='historial')

    # Relacion con oficina
    office_id = Column(Integer, ForeignKey('oficina.id'), nullable=True)
    office = relationship('Office', back_populates='historial')

    # Relacion con article
    article_id = Column(Integer, ForeignKey('articulo.id'), nullable=True)
    article = relationship('Article', back_populates='historial')

    # Relacion con active
    active_id = Column(Integer, ForeignKey('activo.id'), nullable=True)
    active = relationship('Active', back_populates='historial')

    # Relacion con user
    #user_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    #user = relationship('Usuario', back_populates='historial')

