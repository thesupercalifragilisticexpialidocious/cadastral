from fastapi import FastAPI
from sqladmin import Admin, ModelView

from app.api import router
from app.config import settings
from app.models import engine, Inquiry

app = FastAPI(title=settings.app_title)
app.include_router(router)

admin = Admin(app, engine)


class InquiryAdmin(ModelView, model=Inquiry):
    column_list = [
        Inquiry.date,
        Inquiry.latitude,
        Inquiry.longitude,
        Inquiry.number,
        Inquiry.result
    ]


admin.add_view(InquiryAdmin)
