from fastapi import Request
from sqlalchemy.orm import scoped_session


def get_db(request: Request):
    session = scoped_session(request.app.session_factory)
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
