from abc import ABC, abstractmethod
from database.models.user import User
from database.models.category import Category
from database.models.items import Items
from repositories.iRepository import IRepository

class IUnitOfWork(ABC):
    # Generic Type
    users: IRepository[User]
    category: IRepository[Category]
    items: IRepository[Items]

    # If you want a neu method for your (exemple) user, you want to create a new Interface special for user
    # Ex: users: IUserRepository
    @abstractmethod
    async def commit(self):
        pass