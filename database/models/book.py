from sqlalchemy import ForeignKey
from Bot.SashaShop.database.models import BaseModel
from sqlalchemy.orm import mapped_column, Mapped

from Bot.SashaShop.database.models import BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int] # 1$ = 100
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))       #прив'язав book to category