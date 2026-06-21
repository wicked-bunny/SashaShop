
from sqlalchemy.orm import mapped_column, Mapped

from Bot.SashaShop.database.models import BaseModel


class User(BaseModel):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]