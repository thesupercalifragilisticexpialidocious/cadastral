from asyncio import sleep
from datetime import datetime
from random import choice, randint

from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.crud import create_inquiry, get_all_inquiries, get_inquiry, update_inquiry
from app.models import Inquiry
from app.schemas import InquiryCreate, InquiryDB

router = APIRouter()


async def check_match(inquiry_db):
    await sleep(randint(1, 64))
    mock_response = choice(('true', 'false'))
    await update_inquiry(inquiry_db, result=mock_response)


@router.post('/query/', response_model=InquiryDB)
async def add_inquiry(
        inquiry: InquiryCreate,
        background_tasks: BackgroundTasks
) -> Inquiry:
    inquiry_db = await create_inquiry(inquiry)
    background_tasks.add_task(check_match, inquiry_db)
    return inquiry_db


@router.get('/result/', response_model=InquiryDB)
async def get_last_inquiry() -> Inquiry:
    '''Get last inquiry.'''
    inquiry = await get_inquiry()
    return inquiry


@router.get('/result/{id}', response_model=InquiryDB)
async def get_inquiry_by_id(id: int) -> Inquiry:
    inquiry = await get_inquiry(id=id)
    if not inquiry:
        raise HTTPException(
            status_code=404,
            detail=f'No query with id #{id}!',
        )
    return inquiry


@router.get('/history/', response_model=list[InquiryDB])
async def get_all() -> list[Inquiry]:
    inquiries = await get_all_inquiries()
    return inquiries


@router.get('/ping/')
async def ping() -> str:
    return str(datetime.now())
