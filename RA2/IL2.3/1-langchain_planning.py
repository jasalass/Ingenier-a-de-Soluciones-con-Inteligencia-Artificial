"""
IL2.3: Planificación con LangChain
=================================
Ejemplo de cómo un agente LangChain puede planificar y ejecutar pasos usando herramientas.
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


# Herramienta personalizada: suma
def sumar(x):
    """Evalúa una operación aritmética simple.

    Usamos `ast.literal_eval` sobre un árbol validado en vez de `eval()`:
    el argumento viene del LLM, así que es entrada no confiable y `eval()`
    permitiría ejecutar código arbitrario.
    """
    import ast, operator
    OPS = {ast.Add: operator.add, ast.Sub: operator.sub,
           ast.Mult: operator.mul, ast.Div: operator.truediv}

    def _calcular(nodo):
        if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
            return nodo.value
        if isinstance(nodo, ast.BinOp) and type(nodo.op) in OPS:
            return OPS[type(nodo.op)](_calcular(nodo.left), _calcular(nodo.right))
        raise ValueError("operación no permitida")

    try:
        return str(_calcular(ast.parse(x, mode="eval").body))
    except Exception:
        return "Error en la operación"

herramienta_suma = Tool(
    name="Calculadora",
    func=sumar,
    description="Realiza sumas y operaciones matemáticas simples."
)

agente = initialize_agent(
    tools=[herramienta_suma],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    print("Planificación y ejecución con LangChain:")
    print(agente.run("¿Cuánto es 25 * 4 + 130?"))
 