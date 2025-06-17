from fastapi import APIRouter, HTTPException, Response
from uuid import UUID
from database import user_db
from schemas.user import Response, DeactivateUser, User, UserCreate, UserUpdate
from services.user import user_services

user_router = APIRouter()



@user_router.get("")
def get_user():
    return user_db


@user_router.get("/{id}")
def get_user_by_id(id: UUID):
    user = user_services.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found") 
    return user


@user_router.post("")
def add_user(user_in: UserCreate):
    user = user_services.add_user(user_in)
    return Response(message="User added successfully", data=user)


@user_router.put("/{id}")
def update_user(id: UUID, user_in: UserUpdate):
    user = user_services.update_user(id,user_in)
    if not user:
        raise HTTPException(status_code=404, 
                            detail=f"User  with Id:{user_in.id}  not found")

    return Response(message="User updated successfully", data=user)


@user_router.patch("/{id}")
def deactivate_user(id: UUID, user_in:DeactivateUser):
    user = user_services.deactivate_user(str(user_in))
    return Response(message=" deactivated successfully", data=user)


@user_router.delete("/{id}")
def delete_user(id: UUID):
    is_deleted = user_services.delete_user(id)
    if not is_deleted:
        raise HTTPException(status_code=404, 
                            detail=f"User with Id : {id} not found")

    return Response(message="User deleted successfully")