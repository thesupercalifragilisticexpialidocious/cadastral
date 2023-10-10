from typing import Optional

from sqlalchemy import select

from app.models import AsyncSessionLocal, Inquiry
from app.schemas import InquiryCreate


async def create_inquiry(new_request: InquiryCreate) -> Inquiry:
    inquiry = Inquiry(**new_request.dict())
    async with AsyncSessionLocal() as session:
        session.add(inquiry)
        await session.commit()
        await session.refresh(inquiry)
    return inquiry


async def update_inquiry(
        inquiry: Inquiry,
        result: str,
) -> None:
    inquiry.result = result
    async with AsyncSessionLocal() as session:
        session.add(inquiry)
        await session.commit()


async def get_inquiry(id: Optional[int] = None) -> Inquiry:
    async with AsyncSessionLocal() as session:
        if not id:
            query = await session.execute(
                select(Inquiry).order_by(Inquiry.date.desc())
            )
        else:
            query = await session.execute(
                select(Inquiry).where(Inquiry.id == id)
            )
        return query.scalars().first()


async def get_all_inquiries() -> list[Inquiry]:
    async with AsyncSessionLocal() as session:
        db_objs = await session.execute(
            select(Inquiry).order_by(Inquiry.date.desc())
        )
        return db_objs.scalars().all()
