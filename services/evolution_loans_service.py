from typing import List
from models.evolution_loans_model import EvolutionLoansData

class EvolutionLoansService:
    def __init__(self, data: List[EvolutionLoansData]):
        self.data = data
        
    def generate_summary(self) -> str:
        data = self.data
        total_loans = sum(item["loans"] for item in data)
        percentage_growth = ((data[-1]["loans"] - data[0]["loans"]) / data[0]["loans"]) * 100
        month_largest_volume = max(data, key=lambda x: x["loans"])["month"]

        financial_health = (
            "O aumento de empréstimos pode indicar maior confiança dos clientes na economia."
        )
        default_risk = (
            "Clientes com múltiplos empréstimos têm maior probabilidade de inadimplência."
        )
        credit_opportunity = (
            "Oferecer taxas de juros competitivas pode atrair mais clientes para empréstimos."
        )

        # Gera o resumo
        summary = f"""
 Resumo da Evolução de Empréstimos:
 - Total de empréstimos no período: R$ {total_loans:.2f}
 - Crescimento percentual: {percentage_growth:.2f}%
 - Mês com maior volume: {month_largest_volume}

 Insights:
 - Saúde Financeira: {financial_health}
 - Risco de Inadimplência: {default_risk}
 - Oportunidade de Crédito: {credit_opportunity}
        """

        return {"summary": summary}
