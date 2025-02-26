from fastapi import FastAPI, HTTPException
from controllers.customer_growth_controller import CustomerGrowthController
from controllers.distribution_investments_controller import DistributionInvestmentsController
from controllers.evolution_loans_controller import EvolutionLoansController

app = FastAPI()

@app.get("/customer-growth")
async def getCustomerGrowth():
    try:
      data = CustomerGrowthController().list()
      return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/distribution-investments")
async def getDistributionInvestments():
    try:
      data = DistributionInvestmentsController().list()
      return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/evolution-loans")
async def getEvolutionLoans():
    try:
      data = EvolutionLoansController().list()
      return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))