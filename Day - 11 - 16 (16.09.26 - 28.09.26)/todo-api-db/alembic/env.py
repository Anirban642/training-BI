import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# Import your config module (reads from .env.dev / .env.prod etc.)
from app.config.config import DATABASE_URL

# Import Base and ALL models so Alembic autogenerate can see them
from app.db.database import Base
from app.models.category import Category
from app.models.todo import Todo              # noqa: F401
from app.models.user import User              # noqa: F401

# Alembic Config object — gives access to alembic.ini values
config = context.config

# Set the DB URL dynamically from our settings (not from alembic.ini)
config.set_main_option(
    "sqlalchemy.url",
    # asyncpg driver must be replaced with psycopg2 for sync migration runs
    # but for async engine we keep asyncpg
    DATABASE_URL
)

# Set up Python logging from alembic.ini [loggers] section
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# This is the MetaData object for autogenerate support
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (no live DB connection needed)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode using async engine."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())