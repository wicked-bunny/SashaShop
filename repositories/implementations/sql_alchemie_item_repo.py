from sqlalchemy.ext.asyncio import AsyncSession

from repositories.implementations.sql_alchemie_repository import SqlAlchemyRepository
from database.models.items import Items

class SqlAlchemieItemsRepository(SqlAlchemyRepository[Items]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Items)



