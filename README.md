# LLM Health Recommender (WIP)

## Project Overview
A FastAPI-based backend that uses an LLM to generate personalized health recommendations with a rag system to get context from a vector database created from health documents and answers the question based on user biomarker and lifestyle data.

# Current Progress
- Working on refactoring code
    - Adjusting MongoDB for UserLogin
        - Code to throw errors for incorrect login creds and for no existent user_ids
    - Making user login page where the user also puts in info and thats stored in the db
    - Using JWT for stateless authenication

## System Design
- FastAPI for backend
- LLM handles prompt-based recommendations
- MongoDB stores user input and logs
- Docker & GitHub Actions for environment and automation
- Using Pydantic for Data Validation and for typechecking
- Using RAG (Retrieval Augmented Generation) for Responses


## Why I chose to use a RAG system
Known challenges of LLMs include:

- Presenting false information when it is not the answer.
- Presenting out-of-date or generic information when the user expects a specific response.
- Creating a response from non-authoritative sources.
- Creating inaccurate responses due to terminology confusion, wherein different training sources use the same terminology to talk about different things.

For a health recommendation system, these issues are dangerous, so using RAG helps to eliminate these issues


## Tech Stack
FastAPI · Python · MongoDB · Docker · GitHub Actions · TinyLlama · LangChain

## Development Status
- [x] Project initialized
- [x] Basic FastAPI setup
- [x] Dummy LLM integration
- [x] LLM integration
- [x] MongoDB logging
- [ ] React Frontend
- [X] RAG integration
- [ ] Docker containerization
- [ ] CI setup (GitHub Actions)

## Planned Features
- CI/CD Pipelines
- Finish React FrontEnd
