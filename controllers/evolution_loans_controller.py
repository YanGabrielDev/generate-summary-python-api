from typing import Optional
from models.evolution_loans_model import EvolutionLoansData
from services.evolution_loans_service import EvolutionLoansService
from mocks.evolution_loans_mock import evolution_loans

class EvolutionLoansController:
    def __init__(self, data: Optional[EvolutionLoansData] = None):
     self.data = data

    def list(self):
     summary = EvolutionLoansService(evolution_loans).generate_summary()
     return {"data": evolution_loans, "summary": summary }