from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db
from . import crud

router = APIRouter()


@router.get("/")
async def create_employee(db: AsyncSession = Depends(get_db)):
    return await crud.test(db)


@router.get("/fucker")
async def create_employee(db: AsyncSession = Depends(get_db)):
    return "Fuck you?"
