from pydantic import BaseModel
from typing import List

class DistributionInvestmentsData(BaseModel):
    month: str
    fixedIncome: int
    stocks: int
    realEstateFunds: int

class DistributionInvestmentsInput(BaseModel):
    data: List[DistributionInvestmentsData]