from sqlalchemy.orm import Session, joinedload
from schemas.historySchema import HistorySchema
from models.history import History
from fastapi import HTTPException, status
from sqlalchemy import desc, not_

def get_history_all(db: Session, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History).offset(offset).limit(limit).all())
        count = db.query(History).count()
        return result, count
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener el historial {e}")

def get_history_by_company(db: Session, company_id: int, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History)
                  .options(joinedload(History.sucursal))
                  .options(joinedload(History.company))
                  .options(joinedload(History.article))
                  .options(joinedload(History.office))
                  .filter(History.company_id == company_id, not_(History.description.like('%active%')), not_(History.description.like('%article%')))
                  .order_by(desc(History.id))
                  .offset(offset)
                  .limit(limit)
                  .all())
        # hacer que result.sucursal = sucursal
        result = [history.__dict__ for history in result]
        for history in result:
            if history['sucursal'] is not None:
                history['sucursal'] = history['sucursal'].__dict__
                history['sucursal'].pop('_sa_instance_state', None)

            if history['company'] is not None:
                history['company'] = history['company'].__dict__
                history['company'].pop('_sa_instance_state', None)

            if history['article'] is not None:
                history['article'] = history['article'].__dict__
                history['article'].pop('_sa_instance_state', None)

            if history['office'] is not None:
                history['office'] = history['office'].__dict__
                history['office'].pop('_sa_instance_state', None)

            history.pop('sucursal_id', None)
            history.pop('company_id', None)
            history.pop('article_id', None)
            history.pop('office_id', None)

        count = db.query(History).filter(History.company_id == company_id).count()
        return result, count
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener historial de companias {e}")


def get_history_by_sucursal(db: Session, sucursal_id: int, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History)
                  .options(joinedload(History.sucursal))
                  .options(joinedload(History.company))
                  .options(joinedload(History.office))
                  .filter(History.sucursal_id == sucursal_id)
                  .order_by(desc(History.id))
                  .offset(offset)
                  .limit(limit)
                  .all())

        result = [history.__dict__ for history in result]
        for history in result:
            if history['sucursal'] is not None:
                history['sucursal'] = history['sucursal'].__dict__
                history['sucursal'].pop('_sa_instance_state', None)

            if history['company'] is not None:
                history['company'] = history['company'].__dict__
                history['company'].pop('_sa_instance_state', None)

            if history['office'] is not None:
                history['office'] = history['office'].__dict__
                history['office'].pop('_sa_instance_state', None)

            history.pop('sucursal_id', None)
            history.pop('company_id', None)
            history.pop('office_id', None)

        count = db.query(History).filter(History.sucursal_id == sucursal_id).count()
        return result, count
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener historial de sucursales {e}")


def get_history_by_office(db: Session, office_id: int, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History)
                  .options(joinedload(History.sucursal))
                  .options(joinedload(History.office))
                  .options(joinedload(History.active))
                  .options(joinedload(History.article))
                  .filter(History.office_id == office_id)
                  .order_by(desc(History.id))
                  .offset(offset)
                  .limit(limit)
                  .all())

        result = [history.__dict__ for history in result]
        for history in result:
            if history['office'] is not None:
                history['office'] = history['office'].__dict__
                history['office'].pop('_sa_instance_state', None)

            if history['sucursal'] is not None:
                history['sucursal'] = history['sucursal'].__dict__
                history['sucursal'].pop('_sa_instance_state', None)

            if history['active'] is not None:
                history['active'] = history['active'].__dict__
                history['active'].pop('_sa_instance_state', None)

            if history['article'] is not None:
                history['article'] = history['article'].__dict__
                history['article'].pop('_sa_instance_state', None)

            history.pop('sucursal_id', None)
            history.pop('active_id', None)
            history.pop('office_id', None)
            history.pop('article_id', None)

        count = db.query(History).filter(History.office_id == office_id).count()
        return result, count
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener historial de oficinas {e}")


def get_history_by_article(db: Session, article_id: int, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History)
                  .options(joinedload(History.article))
                  .options(joinedload(History.company))
                  .options(joinedload(History.office))
                  .options(joinedload(History.active))
                  .filter(History.article_id == article_id)
                  .order_by(desc(History.id))
                  .offset(offset)
                  .limit(limit)
                  .all())

        result = [history.__dict__ for history in result]
        for history in result:
            if history['article'] is not None:
                history['article'] = history['article'].__dict__
                history['article'].pop('_sa_instance_state', None)

            if history['company'] is not None:
                history['company'] = history['company'].__dict__
                history['company'].pop('_sa_instance_state', None)

            if history['active'] is not None:
                history['active'] = history['active'].__dict__
                history['active'].pop('_sa_instance_state', None)

            if history['office'] is not None:
                history['office'] = history['office'].__dict__
                history['office'].pop('_sa_instance_state', None)

            history.pop('company_id', None)
            history.pop('active_id', None)
            history.pop('article_id', None)
            history.pop('office_id', None)

        count = db.query(History).filter(History.article_id == article_id).count()
        return result, count
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener historial de articulos {e}")


def get_history_by_active(db: Session, active_id: int, limit: int = 100, offset: int = 0):
    try:
        result = (db.query(History)
                  .options(joinedload(History.office))
                  .options(joinedload(History.article))
                  .options(joinedload(History.active))
                  .filter(History.active_id == active_id)
                  .order_by(desc(History.id))
                  .offset(offset)
                  .limit(limit)
                  .all())

        result = [history.__dict__ for history in result]
        for history in result:
            if history['office'] is not None:
                history['office'] = history['office'].__dict__
                history['office'].pop('_sa_instance_state', None)

            if history['article'] is not None:
                history['article'] = history['article'].__dict__
                history['article'].pop('_sa_instance_state', None)

            if history['active'] is not None:
                history['active'] = history['active'].__dict__
                history['active'].pop('_sa_instance_state', None)

            history.pop('article_id', None)
            history.pop('active_id', None)
            history.pop('office_id', None)

        count = db.query(History).filter(History.active_id == active_id).count()
        return result, count
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Error al obtener historial de activos {e}")

def create_history(db: Session, history: HistorySchema):
    try:
        _history = History(
            description=history.description,
            company_id=history.company_id,
            sucursal_id=history.sucursal_id,
            office_id=history.office_id,
            article_id=history.article_id,
            active_id=history.active_id,
            name_user=history.name_user,
        )

        db.add(_history)
        db.commit()
        db.refresh(_history)
        return _history
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"Error creando historial {e}")