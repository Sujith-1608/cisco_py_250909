"""
Database setup module.

This module initializes the SQLite database, creates tables,
and configures the SQLAlchemy session for ORM operations.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_models import Base  # Employee is not used here, so removed to avoid lint warning

# Database engine setup with echo enabled for SQL output
engine = create_engine("sqlite:///employee_app_db.db", echo=True)

# Create all tables defined in Base's metadata
Base.metadata.create_all(engine)

# Session factory bound to the engine
SessionLocal = sessionmaker(bind=engine)

# Create a session instance for database operations
session = SessionLocal()
