from fastapi_jwt_auth import AuthJWT
from fastapi import HTTPException
from sqlalchemy.orm import Session
import src.services.user_service as service


def authorized_user_id(db: Session, Authorize: AuthJWT, user_id: str) -> str:
    authorized_user_id = Authorize.get_jwt_subject()
    authorized_user = service.get_user_by_id(db, authorized_user_id)
    if authorized_user.username != "admin":
        if authorized_user_id != user_id:
            raise HTTPException(status_code=401, detail="Unauthorized access")
    

def authorized_admin_user(db: Session, Authorize: AuthJWT) -> str:
    user_id = Authorize.get_jwt_subject()
    db_user = service.get_user_by_id(db, user_id)
    if db_user.username != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized access")