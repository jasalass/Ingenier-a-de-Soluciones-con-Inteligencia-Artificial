# IL2.1: Arquitectura y Frameworks de Agentes

## 📋 Descripción General

En este módulo exploramos los fundamentos de la arquitectura de agentes inteligentes basados en LLM, progresando desde implementaciones básicas hasta frameworks avanzados como LangChain y CrewAI. Incluye configuraciones específicas para integración con los proveedores compatibles con OpenAI y soluciones a problemas comunes de compatibilidad.

## 🎯 Objetivos de Aprendizaje

- Comprender qué es un agente inteligente y sus componentes fundamentales (cerebro, memoria, herramientas, planificación)
- Dominar el ciclo de razonamiento ReAct (Reason + Act) y el Function Calling nativo de OpenAI
- Implementar agentes desde cero y usando frameworks LangChain y CrewAI
- Configurar el proveedor de LLM en LangChain y en CrewAI
- Diseñar equipos de agentes colaborativos para tareas complejas
- Entender criterios de selección entre diferentes frameworks

## 📚 Contenido del Módulo

### 1. Fundamentos de Agentes Inteligentes
- **[1-agent-fundamentals.ipynb](1-agent-fundamentals.ipynb)** - Implementación de agente básico desde cero
  - Conceptos fundamentales: cerebro, memoria, herramientas
  - Ciclo ReAct (Reason + Act) manual
  - Parsing de texto y gestión de estado
  - Limitaciones y motivación para frameworks

### 2. Function Calling Nativo
- **[2-agent-function-calling.ipynb](2-agent-function-calling.ipynb)** - Mecanismo estructurado de OpenAI
  - Definición de herramientas con JSON Schema
  - Ventajas sobre parsing manual: confiabilidad, seguridad
  - Flujo de llamadas estructuradas
  - Integración con Wikipedia API

### 3. Framework LangChain
- **[3-langchain-agent.ipynb](3-langchain-agent.ipynb)** - Agentes individuales potentes
  - Abstracciones de alto nivel: AgentExecutor, Tool
  - Configuración simplificada con decoradores
  - Gestión automática de historial y errores
  - Tipos de agentes: Zero-shot, Conversational, Structured

### 4. Framework CrewAI
- **[4-crewai-agent.ipynb](4-crewai-agent.ipynb)** - Equipos colaborativos de agentes
  - Conceptos: Agent, Task, Crew, Process
  - Especialización por roles: Investigador, Escritor
  - Coordinación secuencial con dependencias
  - **🔧 CONFIGURACIÓN**: El objeto `LLM` de CrewAI y su proveedor

## 🔧 Configuraciones Técnicas Importantes

### Variables de Entorno Requeridas

Copia `.env.example` a `.env` en la raíz del repo. En Colab, los notebooks leen
estos mismos nombres desde el panel 🔑 **Secrets**.

```bash
LLM_BASE_URL="https://api.mistral.ai/v1"
LLM_API_KEY="tu_key"
LLM_MODEL="mistral-small-latest"
```

### Configuración para LangChain
```python
llm = ChatOpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model=os.getenv("LLM_MODEL", "mistral-small-latest"),
    temperature=0,
)
```

### Configuración para CrewAI
```python
# CrewAI NO usa LangChain: por debajo usa LiteLLM, con su propia clase LLM.
# El prefijo "openai/" le indica que hable el protocolo de OpenAI contra
# nuestro base_url, así funciona con cualquier proveedor compatible.
from crewai import LLM

llm = LLM(
    model="openai/" + os.getenv("LLM_MODEL", "mistral-small-latest"),
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    temperature=0,
)
```

## ⚠️ Problemas Comunes y Soluciones

### 1. Error de Autenticación en CrewAI
**Síntoma**: `AuthenticationError: Incorrect API key provided`
**Causa**: no se le pasó el proveedor al objeto `LLM` de CrewAI, y LiteLLM
intentó ir a OpenAI por defecto.
**Solución**: construir `LLM(model="openai/...", base_url=..., api_key=...)`
con las variables `LLM_*` y pasarlo a cada `Agent(llm=llm)`.

### 2. Error de Herramientas en CrewAI
**Síntoma**: `'Tool' object is not callable`
**Causa**: Mezclar decorador `@tool` de LangChain con CrewAI
**Solución**: Usar `BaseTool`, que en CrewAI 1.x se importa desde
`crewai.tools` (antes estaba en `crewai_tools`).

### 3. Error de Parámetro Verbose
**Síntoma**: `ValidationError: Input should be a valid boolean`
**Causa**: Usar `verbose=2` en lugar de boolean
**Solución**: Usar `verbose=True` en Crew

## 🏗️ Patrones Arquitectónicos Implementados

| **Patrón** | **Notebook** | **Características** |
|------------|--------------|-------------------|
| **Monolítico** | 1-agent-fundamentals | Toda la lógica en una función, parsing manual |
| **Estructurado** | 2-agent-function-calling | JSON Schema, llamadas nativas |
| **Modular** | 3-langchain-agent | Separación de componentes, abstracciones |
| **Colaborativo** | 4-crewai-agent | Múltiples agentes especializados |

## 🔄 Comparación de Frameworks

| **Criterio** | **LangChain** | **CrewAI** |
|-------------|--------------|------------|
| **Especialización** | Agentes individuales complejos | Equipos colaborativos |
| **Complejidad** | Simple a moderada | Compleja, multi-paso |
| **Flexibilidad** | Muy alta, experimental | Estructurada, workflow-oriented |
| **Configuración** | Directa con variables estándar | Requiere mapeo específico |
| **Curva de aprendizaje** | Moderada | Baja para equipos |
| **Casos de uso** | Experimentación, prototipado | Workflows de producción |

## 📝 Actividades Prácticas

### Ejercicios Implementados
1. **Agente Básico**: Implementación desde cero con ReAct manual
2. **Function Calling**: Agente con Wikipedia usando JSON Schema
3. **LangChain Individual**: Agente con herramientas integradas
4. **Equipo CrewAI**: Investigador + Escritor colaborativo

### Casos de Uso Desarrollados
- **Investigación Automatizada**: Búsqueda y síntesis de información
- **Generación de Contenido**: Biografías basadas en investigación
- **Workflows Multi-agente**: Coordinación secuencial especializada

## 🎓 Preparación para IL2.2

### Conceptos Avanzados Siguientes
- **Memory Systems**: Sistemas de memoria persistente y contextual
- **Model Context Protocol (MCP)**: Estándar para integración de herramientas
- **Advanced Planning**: Algoritmos de planificación y re-planificación
- **Tool Integration**: APIs complejas y bases de datos

### Base Establecida
- ✅ Fundamentos sólidos de agentes inteligentes
- ✅ Experiencia con frameworks principales
- ✅ Configuración del proveedor mediante variables `LLM_*`
- ✅ Patrones de colaboración entre agentes
- ✅ Debugging y troubleshooting de sistemas complejos

## 🔗 Recursos Adicionales

### Documentación Oficial
- [LangChain Agents Documentation](https://python.langchain.com/docs/use_cases/autonomous_agents/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)

### Herramientas de Desarrollo
- [LangSmith](https://smith.langchain.com/) - Observabilidad para agentes LangChain
- [Groq](https://console.groq.com/docs/models) · [Mistral](https://docs.mistral.ai/) - Modelos gratuitos

### Troubleshooting y Soporte
- [GitHub Issues - CrewAI](https://github.com/joaomdmoura/crewAI/issues)
- [LangChain Community](https://github.com/langchain-ai/langchain/discussions)

## 💡 Mejores Prácticas Identificadas

1. **Configuración de Entorno**: Verificar variables antes de ejecutar agentes
2. **Manejo de Errores**: Implementar validación robusta en herramientas
3. **Documentación de Herramientas**: Descripciones claras para mejor selección
4. **Debugging**: Usar modo verbose para observar flujo de decisiones
5. **Versionado**: Mantener compatibilidad entre versiones de frameworks
6. **Testing**: Probar configuraciones en entornos similares a producción