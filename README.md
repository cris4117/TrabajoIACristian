# Sistema RAG para Question Answering

## Descripción

Este proyecto implementa un sistema **RAG (Retrieval-Augmented Generation)** capaz de responder preguntas utilizando información recuperada de un conjunto de documentos. El sistema combina recuperación de información, reranking y generación de texto para producir respuestas fundamentadas y reducir alucinaciones.

## Arquitectura

El sistema sigue el siguiente flujo:

1. **Pregunta del usuario**
2. Generación de **embeddings** con `multi-qa-mpnet-base-dot-v1`
3. Recuperación de documentos con **FAISS**
4. **Reranking** con `cross-encoder/ms-marco-MiniLM-L-6-v2`
5. Construcción de contexto
6. Generación de respuesta con `google/flan-t5-base`
7. Evaluación de **grounding**

## Configuración del sistema

- Documentos recuperados: **k = 5**
- Documentos usados como contexto: **rerank = 3**

## Métricas de evaluación

El sistema se evalúa utilizando:

- **Grounding Score**: mide si la respuesta está respaldada por el contexto.
- **BERTScore F1**: mide la similitud semántica entre la respuesta generada y el texto de referencia.
- **Porcentaje de respuestas útiles**.

## Resultados

- Grounding promedio: **0.80**
- BERTScore F1: **0.798**
- Respuestas útiles: **100%**

Estos resultados indican que las respuestas generadas están mayormente fundamentadas en los documentos recuperados.