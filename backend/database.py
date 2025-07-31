from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from .config import settings


engine = create_async_engine(settings.DATABASE_URL)

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)

metadata = MetaData()

Base = declarative_base(metadata=metadata)


async def get_db():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
