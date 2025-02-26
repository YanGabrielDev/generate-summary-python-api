from models.distribution_investments_model import DistributionInvestmentsData
from typing import Optional
from mocks.distribution_investments_mock import distribution_investments
from services.distribution_investments_service import DistributionInvestmentsService

class DistributionInvestmentsController:
    def __init__(self, data: Optional[DistributionInvestmentsData] = None):
     self.data = data

    def list(self):
     summary = DistributionInvestmentsService(distribution_investments).generate_summary()
     return {"data": distribution_investments, "summary": summary }