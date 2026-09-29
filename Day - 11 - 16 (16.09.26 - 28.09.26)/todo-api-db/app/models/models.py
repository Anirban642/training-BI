import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.user import User

from sqlalchemy import Boolean, DateTime, ForeignKey, String, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = (
        UniqueConstraint("user_id", "name", name="uq_categories_user_id_name"),
    )

    # UUID Primary Key
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # UUID Foreign Key to users.id
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    user: Mapped["User"] = relationship(back_populates="categories")
    todos: Mapped[list["Todo"]] = relationship(back_populates="category")


class Todo(Base):
    __tablename__ = "todos"

    # UUID Primary Key
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    isDone: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # UUID Foreign Key to categories.id
    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
        index=True
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    
    # UUID Foreign Key to users.id
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    user: Mapped["User"] = relationship(back_populates="todos")
    category: Mapped["Category"] = relationship(back_populates="todos")