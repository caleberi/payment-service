from fastapi import FastAPI
from .src.controllers import transaction, user, report

payment_service = FastAPI()

payment_service.include_router(user.router)
payment_service.include_router(transaction.router)
payment_service.include_router(report.router)

@payment_service.get("/")
async def ping():
    return "pinged payment-service"

