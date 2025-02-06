from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo para receber os dados do frontend
class DataInput(BaseModel):
    data: List[dict]

@app.post("/api/generate-summary")
async def generate_summary(data_input: DataInput):
    try:
        # Extrai os dados
        data = data_input.data

        # Calcula métricas simples
        total_valor = sum(item['valor'] for item in data)
        media_valor = total_valor / len(data)
        produto_mais_caro = max(data, key=lambda x: x['valor'])

        # Gera o resumo
        summary = f"""
        Resumo dos Dados:
        - Total de itens: {len(data)}
        - Valor total: R$ {total_valor:.2f}
        - Valor médio: R$ {media_valor:.2f}
        - Produto mais caro: {produto_mais_caro['produto']} (R$ {produto_mais_caro['valor']:.2f})
        """

        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))