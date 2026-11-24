import os

from sqlmodel import Session, SQLModel, create_engine

# SQLite file by default. Lesson 19 (Docker Compose) sets DATABASE_URL to PostgreSQL.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")

# SQLite needs this one extra option when used by a web server; PostgreSQL does not.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)


def create_db_and_tables():
    """Create every table that does not exist yet (like a tiny `migrate`)."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """FastAPI dependency: open one database session per request, then close it."""
    with Session(engine) as session:
        yield session