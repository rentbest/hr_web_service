from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, text
from . import models, schemas


async def test(db: AsyncSession):
    res = await db.execute(text("SELECT 1"))
    return "res.scalars().all"
