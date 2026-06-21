from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(
url="sqlite+aiosqlite:///SashaShop.db"
)
session_maker = async_sessionmaker(engine, expire_on_commit=False)