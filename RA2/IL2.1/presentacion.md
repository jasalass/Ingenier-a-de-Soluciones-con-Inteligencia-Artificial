# IL2.1: Arquitectura y Frameworks de Agentes

## Objetivos de la Sesión
- Comprender qué es un agente inteligente y sus componentes fundamentales.
- Dominar el ciclo de razonamiento ReAct (Reason + Act) y el Function Calling nativo.
- Aprender a construir agentes usando frameworks LangChain y CrewAI.
- Implementar equipos de agentes colaborativos para tareas complejas.
- Entender cómo se configura el proveedor de LLM en cada framework (LangChain y CrewAI).

## 1. ¿Qué es un Agente Inteligente?

Un agente de IA trasciende las limitaciones de un LLM tradicional. Mientras que un LLM funciona como una **entrada → salida** simple, un agente es un sistema autónomo que implementa un ciclo continuo de **percepción → razonamiento → decisión → acción**.

### Diferencias Clave:
- **LLM**: Responde una vez con información estática de entrenamiento.
- **Agente**: Mantiene conversaciones, usa herramientas externas, planifica y ejecuta tareas complejas.

### Componentes Fundamentales:
1. **Cerebro (Core Engine)**: El LLM que impulsa el razonamiento y toma de decisiones.
2. **Memoria**: Sistema para mantener contexto (corto plazo) e historial (largo plazo).
3. **Herramientas**: Funciones que permiten interactuar con APIs, bases de datos y sistemas externos.
4. **Planificación**: Capacidad de descomponer objetivos complejos en pasos ejecutables.

La **analogía del becario inteligente** ilustra perfectamente el concepto: le das una tarea de alto nivel (ej. "Investiga el mercado de acciones de Apple"), y el agente descubre qué herramientas usar, cómo interpretarlas y cómo entregar una recomendación fundamentada.

## 2. Arquitecturas y Patrones de Implementación

### Evolución de Implementación: Del Parsing Manual al Function Calling

**Agente Básico (Vanilla Python)**:
- Implementación desde cero usando el patrón ReAct (Reason + Act).
- El LLM escribe intenciones en texto estructurado: `"Action: {tool: 'search', query: 'Elon Musk'}"`
- Parsing manual con expresiones regulares para extraer acciones.
- **Limitaciones**: Frágil, propenso a errores de formato, difícil de escalar.

**Function Calling Nativo**:
- OpenAI proporciona mecanismo estructurado para llamar funciones.
- El LLM devuelve JSON bien formado en lugar de texto a parsear.
- Definición de herramientas usando JSON Schema: especifica nombre, descripción y parámetros.
- **Ventajas**: Confiable, seguro, elimina errores de parsing.

### Tipos de Agentes según Capacidades:

1. **Agente Reactivo**: Responde inmediatamente a estímulos sin mantener estado complejo.
2. **Agente de Planificación**: Crea planes multi-paso, mantiene contexto entre acciones.
3. **Agente Reflexivo**: Evalúa sus acciones, aprende de errores, auto-corrige estrategias.

La progresión natural lleva a frameworks que abstraen esta complejidad y proporcionan abstracciones de alto nivel.

## 3. LangChain: Framework para Agentes Individuales

**LangChain** actúa como una capa de abstracción que simplifica enormemente la construcción de aplicaciones con LLMs, especializándose en **agentes individuales potentes**.

### Ventajas Clave:
- **Abstracciones de alto nivel**: `AgentExecutor` maneja automáticamente el ciclo ReAct.
- **Ecosistema maduro**: Cientos de integraciones con APIs, bases de datos y servicios.
- **Gestión automática**: Historial de mensajes, formato de herramientas, manejo de errores.
- **Flexibilidad**: Múltiples tipos de agentes (Zero-shot, Conversational, Structured Chat).

### Implementación Simplificada:
```python
from langchain_classic.agents import initialize_agent, Tool  # LangChain v1: langchain.agents.create_agent

# Definir herramientas con decorador simple
@tool
def get_wikipedia_summary(query: str) -> str:
    """Busca información en Wikipedia"""
    return wikipedia.summary(query, sentences=2)

# Crear y ejecutar agente en pocas líneas
agent = initialize_agent(
    tools=[get_wikipedia_summary],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

result = agent.run("¿Quién fue Marie Curie?")
```

**Configuración del proveedor en LangChain**:
`ChatOpenAI` recibe el proveedor de forma explícita, leyendo las variables `LLM_*` del entorno:

```python
llm = ChatOpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model=os.getenv("LLM_MODEL", "mistral-small-latest"),
    temperature=0,
)
```

## 4. CrewAI: Orquestación de Equipos de Agentes

Mientras LangChain excel en agentes individuales, **CrewAI** se especializa en **equipos de agentes colaborativos**. Aplicando la analogía de una agencia: no una persona que hace todo, sino especialistas que colaboran.

### Conceptos Fundamentales:
- **Agent**: Agente individual con rol, objetivo (`goal`) e historia (`backstory`) específicos.
- **Task**: Tarea asignada con descripción, salida esperada y dependencias.
- **Crew**: Equipo coordinado que ejecuta tareas siguiendo un proceso definido.
- **Process**: Coordinación secuencial, jerárquica o concurrente entre agentes.

### Ejemplo de Equipo Especializado:
```python
# Agentes especializados con roles claros
researcher = Agent(
    role="Investigador Senior",
    goal="Encontrar información precisa usando fuentes confiables",
    backstory="Experto en investigación académica...",
    tools=[wikipedia_tool]
)

writer = Agent(
    role="Escritor de Biografías",
    goal="Crear contenido claro y estructurado",
    backstory="Escritor profesional especializado..."
)

# Tareas con dependencias
research_task = Task(
    description="Investigar vida y logros de Marie Curie",
    agent=researcher
)

write_task = Task(
    description="Escribir biografía basada en investigación",
    agent=writer,
    context=[research_task]  # Depende del resultado anterior
)

# Equipo coordinado
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)
```

### Configuración Crítica del Proveedor:
**Punto clave**: CrewAI **no** usa LangChain por debajo, sino LiteLLM, con su propia
clase `LLM`. El prefijo `openai/` le indica que hable el protocolo de OpenAI contra
nuestro `base_url`, lo que permite usar cualquier proveedor compatible:
```python
llm = LLM(
    model="openai/" + os.getenv("LLM_MODEL", "mistral-small-latest"),
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
```

**Errores comunes corregidos**:
1. **Herramientas**: Usar `BaseTool`, que en CrewAI 1.x se importa desde `crewai.tools` (antes `crewai_tools`).
2. **Parámetro verbose**: `verbose=True` (boolean), no `verbose=2` (entero).
3. **Configuración LLM**: Pasar `model`, `base_url` y `api_key` explícitos a `crewai.LLM`; no basta con variables de entorno.
4. **Ejecución en notebook**: usar `await crew.kickoff_async()`; `crew.kickoff()` falla dentro del event loop de Jupyter.

## 5. Comparación y Criterios de Selección

### LangChain vs CrewAI: Cuándo Usar Cada Framework

| **Criterio** | **LangChain** | **CrewAI** |
|-------------|--------------|------------|
| **Especialización** | Agentes individuales complejos | Equipos colaborativos |
| **Complejidad de tarea** | Simple a moderada | Compleja, multi-paso |
| **Número de agentes** | Uno, máximo dos | Múltiples especializados |
| **Flexibilidad** | Muy alta, experimental | Estructurada, workflow-oriented |
| **Curva de aprendizaje** | Moderada | Baja para equipos |
| **Ecosistema** | Extenso, maduro | Enfocado, especializado |

### Criterios de Decisión:
- **Experimentación y prototipado** → LangChain
- **Tareas que requieren especialización** → CrewAI  
- **Integración con múltiples LLMs** → LangChain
- **Workflows estructurados con roles claros** → CrewAI
- **Máxima flexibilidad arquitectural** → LangChain
- **Colaboración automática entre agentes** → CrewAI

### Configuraciones Técnicas Críticas:

**Variables de entorno requeridas**:
```bash
LLM_BASE_URL="https://api.mistral.ai/v1"
LLM_API_KEY="tu_key"
LLM_MODEL="mistral-small-latest"
```

**Patrón de mapeo para compatibilidad**:
```python
# Para LangChain directo
llm = ChatOpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model=os.getenv("LLM_MODEL", "mistral-small-latest"),
    temperature=0,
)

# Para CrewAI (requiere mapeo)
os.environ["OPENAI_API_BASE"] = os.environ.get("OPENAI_BASE_URL", "")
llm = LLM(
    model="openai/" + os.getenv("LLM_MODEL", "mistral-small-latest"),
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
```

## 6. Actividad Práctica y Próximos Pasos

### Implementaciones del Módulo:
1. **Fundamentos**: Agente básico desde cero con ciclo ReAct manual.
2. **Function Calling**: Agente usando mecanismo nativo de OpenAI con JSON Schema.
3. **LangChain**: Agente individual con herramientas de Wikipedia, configuración simplificada.
4. **CrewAI**: Equipo investigador-escritor con el proveedor configurado vía `crewai.LLM`.

### Patrones Arquitectónicos Implementados:
- **Monolítico**: Agente básico con toda la lógica en una función.
- **Modular**: Separación clara entre herramientas, cerebro y orquestación.
- **Colaborativo**: Múltiples agentes especializados con tareas interdependientes.

### Configuración de Troubleshooting:
El módulo incluye documentación detallada de errores comunes y sus soluciones, especialmente para la integración de frameworks con los proveedores compatibles con OpenAI.

### Preparación para IL2.2:
- **Memory Systems**: Sistemas de memoria avanzados para agentes persistentes.
- **Model Context Protocol (MCP)**: Estándar para integración de herramientas externas.
- **Tool Integration**: Expansión de capacidades con APIs y bases de datos.
- **Advanced Planning**: Algoritmos de planificación y re-planificación automática.

La base sólida en arquitecturas y frameworks proporcionada en IL2.1 prepara para sistemas de agentes más sofisticados que mantienen estado, integran herramientas complejas y ejecutan planes a largo plazo.