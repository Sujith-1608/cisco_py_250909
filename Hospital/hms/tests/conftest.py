import pytest
import asyncio
from hms.app import routes
from hms.app.db import db, init_db
from hms.app.routes import application

pytestmark = pytest.mark.asyncio


@pytest.fixture
def event_loop():
    """Create a new event loop for each test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def client():
    """
    Flask test client fixture.
    Initializes the in-memory SQLite DB exactly once.
    """
    application.config['TESTING'] = True
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # ✅ Only initialize if not already registered
    if "sqlalchemy" not in application.extensions:
        init_db(application)

    with routes.application.app_context():
        db.create_all()
        yield routes.application.test_client()
        db.session.remove()
        db.drop_all()

