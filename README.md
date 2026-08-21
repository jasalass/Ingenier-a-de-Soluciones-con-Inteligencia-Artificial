# Ingeniería de Soluciones con Inteligencia Artificial

Este repositorio contiene todos los materiales, ejemplos y prácticas del curso **Ingeniería de Soluciones con Inteligencia Artificial**. El curso está organizado en tres grandes módulos (RA), cada uno con submódulos (IL) y ejemplos prácticos en Python y Jupyter.

# IMPORTANTE
Langchain liberó su versión 1.0 oficialmente (Link: https://github.com/davila7/Ingenier-a-de-Soluciones-con-Inteligencia-Artificial) 
Posiblemente algunos bloques de código queden deprecados. Se estará haciendo la mantención del código, pero te recomiendo que revises que las nuevas características de la librería estén utilizando la versión correspondiente.

---

## 📚 Descripción General

El curso cubre desde los fundamentos de la IA generativa y el prompt engineering, hasta el desarrollo de agentes inteligentes y las mejores prácticas para llevar soluciones a producción, incluyendo observabilidad, seguridad y ética.

- **Nivel:** Intermedio
- **Modalidad:** Práctica y conceptual
- **Requisitos:** Python básico, interés en IA

---

## 🏗️ Estructura del Proyecto

```
RA1/  # Fundamentos de IA Generativa y Prompt Engineering
  IL1.1/  # Introducción a LLMs y APIs
  IL1.2/  # Técnicas de prompting
  IL1.3/  # Infraestructura RAG
  IL1.4/  # Evaluación y optimización

RA2/  # Desarrollo de Agentes Inteligentes
  IL2.1/  # Arquitectura y frameworks (LangChain, CrewAI)
  IL2.2/  # Memoria y herramientas externas
  IL2.3/  # Planificación y orquestación
  IL2.4/  # Documentación técnica y arquitectura

RA3/  # Observabilidad, Seguridad y Ética
  IL3.1/  # Observabilidad y métricas
  IL3.2/  # Trazabilidad y logs
  IL3.3/  # Seguridad y ética
  IL3.4/  # Escalabilidad y sostenibilidad
```

Cada subcarpeta IL contiene ejemplos en Python (`.py`), notebooks (`.ipynb`) o guías (`.md`).

---

## 🚦 ¿Cómo usar este repositorio?

1. **Haz un fork** del repositorio a tu cuenta de GitHub.
2. **Consigue tus dos API keys** y cárgalas en los Secrets de Colab (ver [Puesta en marcha](#-puesta-en-marcha-google-colab--recomendado)).
3. **Abre los notebooks en Colab** con el badge que trae cada uno y ejecútalos en orden.
4. **Lee los README.md** de cada carpeta para entender el objetivo de cada módulo.
5. **Consulta los archivos `.md`** para teoría, mejores prácticas y requisitos de cada entrega.

---

## 🚀 Puesta en marcha (Google Colab — recomendado)

No necesitas instalar nada en tu computador. **Todo corre en Colab con servicios gratuitos que no piden tarjeta de crédito.**

### Paso 1 — Consigue tus dos API keys

| Key | Para qué | Dónde obtenerla |
|---|---|---|
| `LLM_API_KEY` | Chat (todos los módulos) | [console.mistral.ai/api-keys](https://console.mistral.ai/api-keys) |
| `GOOGLE_API_KEY` | Embeddings (RA1/IL1.3 y IL1.4) | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |

Para la de Google basta la misma cuenta con la que entras a Colab.

> **¿Por qué dos proveedores?** Mistral se encarga del chat, pero la parte de RAG
> vectorial usa Gemini (`gemini-embedding-001`) para los embeddings. Son servicios
> distintos y ningún proveedor gratuito cubre bien los dos.
>
> La key de Mistral pide verificar un número de teléfono una sola vez.

### Paso 2 — Haz un fork de este repositorio

Botón **Fork** arriba a la derecha en GitHub. Así tus cambios y anotaciones quedan en tu propia copia.

### Paso 3 — Abre el notebook en Colab

Cada notebook trae un badge [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com) al inicio.

> Ojo: ese badge apunta al repositorio del curso. Para abrir **tu fork**, entra a
> [colab.research.google.com](https://colab.research.google.com) → pestaña **GitHub** →
> escribe tu usuario y elige el notebook. También puedes reemplazar el nombre de usuario
> directamente en la URL del badge.

### Paso 4 — Carga tus keys en los Secrets de Colab

En la barra lateral izquierda de Colab, ícono **🔑 Secrets** → **Add new secret**.

El nombre debe escribirse **exactamente así** (mayúsculas y guiones bajos incluidos), porque
es el nombre que buscan los notebooks:

| Name (exacto) | Value | ¿Obligatorio? | Se usa en |
|---|---|---|---|
| `LLM_API_KEY` | tu key de Mistral | **Sí** | Todos los notebooks |
| `GOOGLE_API_KEY` | tu key de Google AI Studio | **Sí, desde IL1.3** | RA1/IL1.3 y RA1/IL1.4 (embeddings) |
| `LANGSMITH_API_KEY` | tu key de LangSmith | No, opcional | RA1/IL1.4 (`2-langsmith-evaluation.ipynb`) |

> ⚠️ **Activa el interruptor "Notebook access" en cada secreto.** Si el secreto existe pero
> el interruptor está apagado, el notebook no puede leerlo y la variable queda vacía, con un
> error de credenciales más adelante. Es el error de configuración más habitual.

Los secrets se guardan en tu cuenta de Google, no en el notebook: **los configuras una sola vez
y sirven para todos los notebooks del curso**, incluso en sesiones futuras.

Si más adelante rotas una key, **borra el secreto y créalo de nuevo** en lugar de editar el
valor: editar sobre el texto existente suele dejar restos del valor anterior y produce un
`401 Invalid API Key` difícil de diagnosticar.

#### Cambiar de proveedor desde Colab (opcional)

Si te quedas sin cuota de Mistral, puedes cambiar de proveedor **sin tocar el código**,
agregando estos secretos adicionales. Si no los defines, todo sigue funcionando con Mistral:

| Name (exacto) | Value para usar Groq |
|---|---|
| `LLM_BASE_URL` | `https://api.groq.com/openai/v1` |
| `LLM_MODEL` | `openai/gpt-oss-120b` |
| `LLM_MODEL_SMALL` | `openai/gpt-oss-20b` |

Y en `LLM_API_KEY` pon tu key de Groq ([console.groq.com/keys](https://console.groq.com/keys),
gratuita). Los embeddings siguen usando Gemini en cualquier caso, así que `GOOGLE_API_KEY`
no cambia.

> ⚠️ **Sobre Groq:** retiró los modelos Llama de su catálogo gratuito. Lo que queda son
> modelos de razonamiento, que gastan parte del presupuesto de `max_tokens` en razonamiento
> interno que no ves: con valores muy bajos (≤10) devuelven una respuesta vacía. Los
> ejercicios ya usan valores seguros, pero tenlo en cuenta si experimentas con ese parámetro.

> Cualquier proveedor con API compatible con OpenAI sirve: basta apuntar `LLM_BASE_URL`
> a su endpoint y poner un `LLM_MODEL` que ese proveedor reconozca.

### Paso 5 — Ejecuta

`Entorno de ejecución` → `Ejecutar todas`. La primera celda instala las dependencias en Colab
(demora ~1 min) y la segunda lee tus keys desde los Secrets. Nunca escribas tus keys
directamente en una celda.

### Límites del plan gratuito

Las cuotas son **por cuenta**, así que cada quien tiene la suya. Los valores relevantes:

| Servicio | Modelo | Límite diario | Límite por minuto |
|---|---|---|---|
| Mistral | `mistral-small-latest` | plan gratuito, sin coste | según el plan |
| Groq | `openai/gpt-oss-120b` | 100.000 tokens · 1.000 peticiones | 12.000 tokens · 30 peticiones |
| Gemini | `gemini-embedding-001` | 1.000 peticiones | 100 peticiones |

Una pasada completa por los notebooks de RA1 consume del orden de **30.000 tokens**, así que
el límite diario da para unas tres corridas completas. Si te aparece un error `429`
`rate_limit_exceeded`, no está roto tu código: agotaste la cuota. El mensaje de error indica
cuántos segundos esperar, y la cuota se va liberando de a poco.

**Truco:** si estás iterando mucho sobre un ejercicio, usa `LLM_MODEL_SMALL`
(`ministral-8b-latest`), que es más rápido y barato en tokens que el modelo principal.

---

## 🔧 Si algo falla

El mensaje de error dice exactamente qué revisar:

| Mensaje | Qué significa | Solución |
|---|---|---|
| `Connection error.` | No se alcanza el servidor: red, firewall o proxy | Ver abajo |
| `401` / `Missing credentials` | La key no llegó al notebook | Revisa los Secrets de Colab (con "Notebook access" activado) o tu `.env` |
| `429 rate_limit_exceeded` | Agotaste la cuota gratuita | Espera los segundos que indica el error, o cambia a `LLM_MODEL_SMALL` |
| `404` | El modelo no existe en ese proveedor, o el `base_url` está equivocado | Comprueba que `LLM_MODEL` exista en el proveedor y que `LLM_BASE_URL` corresponda |
| `ModuleNotFoundError` | Falta instalar dependencias | Ejecuta la primera celda del notebook (o `pip install -r requirements.txt` en local) |

### Diagnóstico de `Connection error.`

Este error **no es de tu código**: significa que la máquina no pudo abrir la conexión.
Suele pasar en redes institucionales que bloquean dominios, o detrás de un proxy o VPN.
Pega esto en una celda para ubicar el punto exacto de la falla:

```python
import os, socket, httpx
print("LLM_BASE_URL:", os.getenv("LLM_BASE_URL"))
try:
    print("DNS api.groq.com ->", socket.gethostbyname("api.groq.com"))
except Exception as e:
    print("DNS FALLA ->", e, "  (dominio bloqueado por la red)")
try:
    print("HTTPS ->", httpx.get("https://api.groq.com/openai/v1/models", timeout=15).status_code)
except Exception as e:
    print("HTTPS FALLA ->", type(e).__name__, "  (firewall o proxy)")
```

- **Falla el DNS** → la red bloquea el dominio. Prueba con otra red (datos del celular)
  o pide a TI que habilite `api.groq.com`.
- **DNS bien pero falla HTTPS** → hay un proxy o firewall en medio.
- **Ambos bien pero el notebook falla** → reinicia el entorno de ejecución y vuelve a
  correr las celdas desde la primera.

> **Ejecutar en Google Colab evita este problema por completo**, porque el código corre
> en la infraestructura de Google y no en la red del instituto. Si estás en local y
> `Connection error.` persiste, abre el notebook en Colab con su badge.

---

## 💻 Alternativa: ejecución local

- Python 3.10+
- Instalar dependencias y configurar el entorno:

```bash
pip install -r requirements.txt
```

Luego copia `.env.example` a `.env` y completa `LLM_API_KEY` y `GOOGLE_API_KEY`
(mismas keys del Paso 1). Los notebooks detectan si están en Colab o en local y
leen las credenciales del lugar correcto sin que cambies nada.

`LLM_BASE_URL` ya viene configurado apuntando a Mistral, que expone una API compatible con OpenAI.
`LANGSMITH_API_KEY` es opcional y solo la necesita `RA1/IL1.4/2-langsmith-evaluation.ipynb`
(gratis en [smith.langchain.com](https://smith.langchain.com/settings)).

> **Las apps de Streamlit** (`RA1/IL1.3/2-text-chunking.py` y `RA1/IL1.4/1-evaluation-rag.py`)
> requieren ejecución local — Colab no sirve páginas de Streamlit de forma nativa:
> ```bash
> streamlit run RA1/IL1.3/2-text-chunking.py
> ```

---

## 🎥 Videotutoriales del Curso

Para un aprendizaje más visual, puedes seguir la lista de reproducción completa del curso en YouTube:

- [**Ver la lista de reproducción completa en YouTube**](https://www.youtube.com/playlist?list=PL2gz3vdpKdfVHQqH39oPu4mxLrmAUd2eX)

---

## 🧭 Navegación recomendada

- **Empieza por RA1** si eres nuevo en IA generativa y prompting.
- **RA2** es ideal para aprender a construir agentes inteligentes y documentar soluciones.
- **RA3** te prepara para llevar tus agentes a producción, monitorear, asegurar y escalar.
- Cada IL tiene ejemplos autocontenidos y README propio.

---

## 📑 Evaluaciones y entregables

- Quizzes teóricos en cada RA
- Proyectos prácticos y presentaciones
- Proyecto final transversal (40% de la nota)

---

## 📖 Recursos adicionales

- [LangChain Docs](https://python.langchain.com/)
- [CrewAI Docs](https://docs.crewai.com/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

## 📝 Sobre este repositorio

- Inspirado en buenas prácticas de ingeniería y educación en IA.
- Estructura y progresión pensadas para aprendizaje autónomo y colaborativo.
- Para dudas, sugerencias o mejoras, abre un issue o pull request.

---

¡Explora, experimenta y aprende a construir soluciones de IA listas para producción!
