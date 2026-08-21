"""
IL2.3: Planificación Básica con LangChain
========================================
Ejemplo de cómo un agente LangChain puede planificar y ejecutar pasos simples usando una herramienta.
"""

# Requiere: pip install -r requirements.txt (desde la raíz del repo)
import os

from dotenv import load_dotenv
load_dotenv()                      # lee LLM_BASE_URL / LLM_API_KEY / LLM_MODEL del .env

# LangChain v1: langchain.agents.create_agent (o langgraph)
from langchain_classic.agents import initialize_agent, Tool, AgentType
from langchain_openai import ChatOpenAI

# El proveedor se configura por entorno; nunca escribas la key en el código.
llm = ChatOpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model=os.getenv("LLM_MODEL", "mistral-small-latest"),
    temperature=0,
)


# Herramienta personalizada: pasos para preparar café
def pasos_cafe(_):
    return "1. Calentar agua\n2. Añadir café al filtro\n3. Verter agua caliente\n4. Servir en una taza"

herramienta_cafe = Tool(
    name="PasosCafé",
    func=pasos_cafe,
    description="Devuelve los pasos para preparar café."
)

agente = initialize_agent(
    tools=[herramienta_cafe],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    print("Planificación con LangChain:")
    print(agente.run("¿Cuáles son los pasos para preparar café?")) 