"""
IL2.3: Orquestación Multi-Agente con CrewAI
==========================================
Ejemplo de cómo dos agentes CrewAI colaboran para resolver una tarea.
"""

# Requiere: pip install -r requirements.txt (desde la raíz del repo)
import os

from dotenv import load_dotenv
load_dotenv()                      # lee LLM_BASE_URL / LLM_API_KEY / LLM_MODEL del .env

from crewai import LLM, Agent, Task, Crew

# CrewAI usa LiteLLM por debajo. El prefijo "openai/" le indica que hable el
# protocolo de OpenAI contra el `base_url` que le pasamos, lo que permite usar
# cualquier proveedor compatible (Groq, Mistral, etc.) sin cambiar el código.
llm = LLM(
    model="openai/" + os.getenv("LLM_MODEL", "mistral-small-latest"),
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    temperature=0,
)

# Agente 1: Investigador
investigador = Agent(
    role="Investigador",
    goal="Buscar información sobre la capital de Francia",
    backstory="Eres experto en encontrar datos rápidos.",
    llm=llm,
)

# Agente 2: Redactor
redactor = Agent(
    role="Redactor",
    goal="Redactar una respuesta clara y breve",
    backstory="Eres especialista en explicar conceptos de forma sencilla.",
    llm=llm,
)

# Tareas. `expected_output` es obligatorio en CrewAI 1.x: describe qué debe
# entregar la tarea, y el agente lo usa como criterio para darla por terminada.
tarea_investigar = Task(
    description="Busca cuál es la capital de Francia",
    expected_output="El nombre de la capital y un dato relevante sobre ella.",
    agent=investigador,
)
tarea_redactar = Task(
    description="Redacta una respuesta usando la información encontrada",
    expected_output="Un párrafo breve y claro dirigido a un lector no experto.",
    agent=redactor,
    context=[tarea_investigar],
)

# Crew (equipo)
crew = Crew(
    agents=[investigador, redactor],
    tasks=[tarea_investigar, tarea_redactar],
    verbose=True,
)

if __name__ == "__main__":
    print("Orquestación multi-agente con CrewAI:")
    print(crew.kickoff())
