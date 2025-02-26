from pydantic import BaseModel
from typing import List

class ClientsData(BaseModel):
    month: str  
    clients: int 

class CustomerGrowthInput(BaseModel):
    data: List[ClientsData]  

class CustomerGrowthList:
    summary: str
    data: List[ClientsData]