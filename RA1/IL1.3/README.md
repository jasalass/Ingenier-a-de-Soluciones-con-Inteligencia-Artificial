# RA1 - IL1.3: Infraestructura RAG (Retrieval-Augmented Generation)

En este módulo de aprendizaje, exploraremos la arquitectura de **Recuperación Aumentada por Generación (RAG)**, una técnica poderosa para conectar Modelos de Lenguaje Grandes (LLMs) con fuentes de conocimiento externas y actualizadas.

## ¿Qué es RAG?

RAG es un enfoque que mejora las respuestas de los LLMs al permitirles consultar una base de conocimiento externa antes de generar una respuesta. Esto reduce las "alucinaciones" y asegura que la información proporcionada sea relevante y precisa.

## Contenido del Módulo

Este módulo se divide en los siguientes cuadernos de Jupyter, diseñados para guiarte progresivamente a través de los conceptos de RAG:

1.  **`1-basic-rag.ipynb`**: Introduce los conceptos fundamentales de RAG con un ejemplo simple y práctico.
2.  **`2-text-chunking.py`**: Explora diferentes estrategias para dividir texto en fragmentos (chunks), un paso crucial para la eficiencia del recuperador.
3.  **`3-embeddings-simple-rag.ipynb`**: Muestra cómo generar embeddings a partir de fragmentos de texto y cómo utilizarlos para construir un sistema RAG básico.
4.  **`4-vector-rag.ipynb`**: Avanza hacia una implementación más robusta utilizando una base de datos vectorial para almacenar y consultar eficientemente los embeddings.

## Objetivos de Aprendizaje

Al finalizar este módulo, serás capaz de:

-   Comprender la arquitectura y los componentes de un sistema RAG.
-   Implementar un flujo RAG básico para responder preguntas basadas en un documento.
-   Aplicar técnicas de text chunking para procesar documentos.
-   Utilizar modelos de embeddings para convertir texto en representaciones vectoriales.
-   Integrar una base de datos vectorial para crear un sistema RAG escalable.

## Instrucciones

Para comenzar, abre y ejecuta los cuadernos en el orden listado. Asegúrate de tener las variables de entorno (`LLM_BASE_URL`, `LLM_API_KEY` y `GOOGLE_API_KEY`) configuradas como se describe en el `README.md` principal del repositorio.

> **Nota sobre embeddings:** el chat de estos cuadernos usa Groq, pero Groq no ofrece
> endpoint de embeddings. Por eso los notebooks 3 y 4 generan los vectores con
> **Gemini** (`gemini-embedding-001`) vía Google AI Studio, que es gratis y solo
> requiere la cuenta de Google que ya usas para Colab. De ahí viene `GOOGLE_API_KEY`.