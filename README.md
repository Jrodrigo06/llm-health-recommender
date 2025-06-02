# LLM Health Recommender (WIP)

## Project Overview
A FastAPI-based backend that uses an LLM to generate personalized health recommendations based on user biomarker and lifestyle data.

## System Design
- FastAPI for backend
- LLM handles prompt-based recommendations
- MongoDB stores user input and logs
- Docker & GitHub Actions for environment and automation
- Using Pydantic for Data Validation and for typechecking
- Using RAG (Retrieval Augmented Generation) for Responses

## Why RAG
Known challenges of LLMs include:

- Presenting false information when it is not the answer.
- Presenting out-of-date or generic information when the user expects a specific response.
- Creating a response from non-authoritative sources.
- Creating inaccurate responses due to terminology confusion, wherein different training sources use the same terminology to talk about different things.

For a health recommendation system, these issues are dangerous, so using RAG helps to eliminate these issues


## Tech Stack
FastAPI · Python · MongoDB · Docker · GitHub Actions · TinyLlama

## Development Status
- [x] Project initialized
- [x] Basic FastAPI setup
- [x] Dummy LLM integration
- [x] LLM integration
- [x] MongoDB logging
- [ ] React Frontend
- [ ] RAG integration
- [ ] Docker containerization
- [ ] CI setup (GitHub Actions)

## Planned Features
- CI/CD Pipelines
- React FrontEnd
