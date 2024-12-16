import pytest 
from sqlmodel import Session, SQLModel
from sqlmodel import create_engine
from fastapi.testclient import TestClient
from sqlmodel.pool import StaticPool
from main import app
from routes import get_session


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///./test_db.db", 
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client(session:Session) :
    def get_session_override():
            return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()