# LLM Health Recommender

## Project Overview
A FastAPI-based backend that uses an LLM to generate personalized health recommendations with a rag system to get context from a vector database created from health documents and answers the question based on user biomarker and lifestyle data.



https://github.com/user-attachments/assets/685bd844-66d4-4326-b1a8-b7bec61009e4



# Current Progress
- Working on refactoring code
    - Adjusting MongoDB for UserLogin
        - Code to throw errors for incorrect login credentials and non-existent user IDs
    - Making a user login page where the user also puts in info, and that's stored in the db
    - Using JWT for stateless authentication

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
- [x] React Frontend
    - [x] About Page
    - [x] Handling Authentication on frontend with local storage
- [X] RAG integration
- [ ] CI setup (GitHub Actions)

## Planned Features
- CI/CD Pipelines
- Finish React FrontEnd
