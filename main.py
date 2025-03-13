from fastapi import FastAPI, HTTPException
from controllers.customer_growth_controller import CustomerGrowthController
from controllers.distribution_investments_controller import DistributionInvestmentsController
from controllers.evolution_loans_controller import EvolutionLoansController
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",  
    "https://blue-bank-dashboard.vercel.app",    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"],    
    allow_headers=["*"],    
)

@app.head("/")
async def read_root():
    return {"message": "Bem-vindo à API de Análise Financeira!"}

@app.get("/customer-growth")
async def get_customer_growth():
    try:
        data = CustomerGrowthController().list()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/distribution-investments")
async def get_distribution_investments():
    try:
        data = DistributionInvestmentsController().list()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/evolution-loans")
async def get_evolution_loans():
    try:
        data = EvolutionLoansController().list()  # Corrigido o nome do controller
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import os
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))