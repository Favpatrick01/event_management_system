from uuid import UUID
from fastapi import APIRouter, HTTPException, Response
from database import user_db
from schemas.user import DeactivateUser, User, UserCreate, UserUpdate


class UserServices:

    @staticmethod
    def get_user_by_id(id):
        user = user_db.get(str(id))
        if not user:
         return None
        return user
    
    @staticmethod
    def add_user(user_in: UserCreate ):
       user = User(
        id=str(UUID(int=len(user_db) + 1)),
        **user_in.model_dump(),
    )
       user_db[user.id] = user
       return user
    

    @staticmethod
    def update_user(id: UUID, user_in: UserUpdate):
       user = user_db.get(str(id))
       if not user:
          return None
       user.name = user_in.name
       user.email = user_in.email
       return user
    
    @staticmethod
    def deactivate_user(id: UUID, user_in: DeactivateUser):
       user = user_db.get(str(id))
       if not user:
        return None

       user.is_active = user_in.is_active
       return user
       
   
    @staticmethod
    def delete_user(id: UUID): 
        user = user_db.get(str(id))
        if not user:
           return None

        del user_db[user.id]
        return True


user_services = UserServices()



  