from datetime import datetime

from sqlalchemy import Column, CheckConstraint, DateTime, Integer, Float, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.config import settings


engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session


class PreBase:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=PreBase)


class Inquiry(Base):
    __table_args__ = (CheckConstraint(
        ('-90 <= latitude AND latitude <= 90 AND '
         '-180 <= longitude AND longitude <= 180')
    ),)
    latitude = Column(Float)
    longitude = Column(Float)
    number = Column(String(32))
    result = Column(String(10), default='processing')
    date = Column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return (f'${self.latitude}, {self.longitude} '
                f'checked against {self.number}: {self.result}')
