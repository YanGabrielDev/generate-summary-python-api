from typing import List
from models.distribution_investments_model import DistributionInvestmentsData


class DistributionInvestmentsService:
    def __init__(self, data: List[DistributionInvestmentsData]):
        self.data = data

    
    def generate_summary(self) -> str:
        fixed_income = sum(item['fixedIncome'] for item in self.data)
        total_stocks = sum(item['stocks'] for item in self.data)
        total_real_estate_funds = sum(item['realEstateFunds'] for item in self.data)
        popular_investment = max(["Renda Fixa", "Ações", "Fundos Imobiliários"],
        key=lambda x: fixed_income if x == 'Renda Fixa' else total_stocks if x == "Ações" else total_real_estate_funds)


        return_risk = (
            "Renda Fixa tem baixo risco e retorno moderado, enquanto Ações oferecem maior retorno com maior volatilidade."
        )
        diversification_opportunity = (
            "Aumentar a exposição a Fundos Imobiliários pode equilibrar o portfólio e reduzir riscos."
        )
        investment_trend = (
            "Ações estão ganhando popularidade, possivelmente devido ao mercado em alta."
        )

        summary = f"""
Resumo da Distribuição de Investimentos:
- Total em Renda Fixa: R$ {fixed_income:.2f}
- Total em Ações: R$ {total_stocks:.2f}
- Total em Fundos Imobiliários: R$ {total_real_estate_funds:.2f}
- Investimento mais popular: {popular_investment}

Insights:
- Risco x Retorno: {return_risk}
- Oportunidade de Diversificação: {diversification_opportunity}
- Tendência: {investment_trend}
        """
        return {"summary": summary}