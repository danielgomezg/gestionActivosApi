from sqlalchemy.orm import Session, joinedload
from schemas.historySchema import HistorySchema
from models.history import History
from models.sucursal import Sucursal
from fastapi import HTTPException, status
from sqlalchemy import func, and_, desc

def get_history_all(db: Session, limit: int = 100, offset: int = 0):
    #return db.query(Usuario).offset(offset).limit(limit).all()
    try:
        result = (db.query(History).offset(offset).limit(limit).all())
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener el historial {e}")

def get_history_by_company(db: Session, company_id: int, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History)
                  .options(joinedload(History.sucursal))
                  .options(joinedload(History.user))
                  .filter(History.company_id == company_id)
                  .order_by(desc(History.id))
                  .offset(offset)
                  .limit(limit)
                  .all())
        print(result)
        # hacer que result.sucursal = sucursal
        result = [history.__dict__ for history in result]
        for history in result:
            history['sucursal'] = history['sucursal'].__dict__
            history['sucursal'].pop('_sa_instance_state', None)


        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener historial de companias {e}")

def create_history(db: Session, history: HistorySchema):
    try:
        _history = History(
            description=history.description,
            company_id=history.company_id,
            sucursal_id=history.sucursal_id,
            office_id=history.office_id,
            article_id=history.article_id,
            active_id=history.active_id,
            user_id=history.user_id
        )

        db.add(_history)
        db.commit()
        db.refresh(_history)
        return _history
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"Error creando historial {e}")