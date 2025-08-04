
import os
from openai import OpenAI

# Inicializar cliente
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Listar modelos disponibles
models = client.models.list()

# Mostrar solo los IDs de modelo
for model in models.data:
    print(model.id)
