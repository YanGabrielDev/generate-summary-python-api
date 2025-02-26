from typing import List
from models.customer_growth_model import ClientsData

class CustomerGrowthService:
    def __init__(self, data: List[ClientsData]):
    
        self.data = data

    def __calculate_total_customers(self) -> int:
        print(self.data)
        return sum([item["clients"] for item in self.data])

    def __calculate_percentage_growth(self) -> float:

        if not self.data:
            return 0.0
        first_month = self.data[0]["clients"]
        last_month = self.data[-1]["clients"]
        return ((last_month - first_month) / first_month) * 100

    def __find_biggest_growth_month(self) -> str:

        if not self.data:
            return ""
        return max(self.data, key=lambda x: x["clients"])["month"]

    def generate_summary(self):
  
        total_clients = self.__calculate_total_customers()
        growth_percentage = self.__calculate_percentage_growth()
        biggest_growth_month = self.__find_biggest_growth_month()

        # Insights inteligentes
        trend = "exponencial" if growth_percentage > 50 else "linear" if growth_percentage > 20 else "estável"
        causes_growth = "campanhas de marketing" if biggest_growth_month in ["Jul", "Dez"] else "expansão de serviços"
        tendencia_crescimento = (
            "O crescimento segue uma tendência exponencial, indicando que estratégias de marketing estão surtindo efeito."
        )
        causa_crescimento = (
            f"O pico de crescimento em {biggest_growth_month} coincide com a campanha de férias do BlueBank."
        )
        previsao_futura = (
            "Se a tendência atual continuar, o BlueBank atingirá 5.000 clientes em março do próximo ano."
        )        # Gera o resumo
        summary = f"""
Resumo do Crescimento de Clientes:
- Total de clientes no período: {total_clients}
- Crescimento percentual: {growth_percentage:.2f}%
- Mês com maior crescimento: {biggest_growth_month}
- Tendência: {trend}
- Possível causa do crescimento: {causes_growth}

Insights:
- Tendência de Crescimento: {tendencia_crescimento}
- Causa do Crescimento: {causa_crescimento}
- Previsão Futura: {previsao_futura}
        """

        return {"summary": summary}