from typing import List, Optional
from models.customer_growth_model import ClientsData, CustomerGrowthList
from mocks.customer_growth_mock import customer_growth
from services.customer_growth_service import CustomerGrowthService


class CustomerGrowthController:
    def __init__(self, data: Optional[List[ClientsData]] = None):
    
        self.data = data
    
    def list(self) -> CustomerGrowthList:
     summary = CustomerGrowthService(customer_growth).generate_summary()
     return {"data": customer_growth, "summary": summary }