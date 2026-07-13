from repositories.implementations.sql_alchemie_repository import SqlAlchemyRepository
from database.models.items import Items

class IItemsRepository(SqlAlchemyRepository[Items]):
    pass
