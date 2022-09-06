
from pydantic import BaseModel


class CreateTransactionRequest(BaseModel):
    sender_id:str
    reciever_id:str
    narration:str
    amount:float
