from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
from sqlalchemy import Boolean, text


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, server_default=text("true"), nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    categories: Mapped[list["Category"]] = relationship(back_populates="user")
    todos: Mapped[list["Todo"]] = relationship(back_populates="user")
