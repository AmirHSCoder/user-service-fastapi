from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy import create_engine
from alembic import context
import asyncio

from app.core.config import settings
from app import models

config = context.config

fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

target_metadata = models.Base.metadata


def run_migrations_online():
    connectable = create_engine(settings.DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, render_as_batch=True)

        with context.begin_transaction():
            context.run_migrations()


def run_migrations():
    run_migrations_online()


if context.is_offline_mode():
    raise RuntimeError("Offline mode not supported")
else:
    run_migrations()

