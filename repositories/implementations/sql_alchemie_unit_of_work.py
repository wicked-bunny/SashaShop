from sqlalchemy.ext.asyncio import AsyncSession


from repositories.implementations.sql_alchemie_item_repo import SqlAlchemieItemsRepository
from repositories.implementations.sql_alchemie_repository import SqlAlchemyRepository
from repositories.unit_of_work import IUnitOfWork

from database.models.user import User
from database.models.category import Category

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session
        # Special implementation with nue methods for Item
        self.items = SqlAlchemieItemsRepository(self.session)
        # Default
        self.users = SqlAlchemyRepository(self.session, User)
        self.category = SqlAlchemyRepository(self.session, Category)

    async def commit(self):
        await self.session.commit()

