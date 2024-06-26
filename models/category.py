from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
import pandas as pd
from schemas.categorySchema import CategorySchema

class Category(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, unique=True, nullable=False)
    parent_id = Column(Integer, nullable=False)
    removed = Column(Integer, default=0, nullable=False)
    code = Column(String, nullable=False)

    #Relacion con article
    articles = relationship('Article', back_populates='category')

def validateCategoryFromFile(category):
    try:
        # Aquí puedes acceder a los datos de cada fila
        description = '' if pd.isna(category.iloc[3]) else category.iloc[3]
        parent_id = 0
        print("model category")
        print(description)
        print(parent_id)

        new_category = {
            "description": str(description),
            "parent_id": parent_id
        }

        if new_category["description"] == '':
            return None, "Faltan campos obligatorios"

        print(f"Category : {new_category}")
        new_category = CategorySchema(**new_category)
        return new_category, "ok"

    except Exception as e:
        print(f"Error : {e}")
        print(f"Tipo de error : {type(e)}")
        print("Argumentos del error : ", e.args)
        return None, e