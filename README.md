# LLM Health Recommender (WIP)

## Project Overview
A FastAPI-based backend that uses an LLM to generate personalized health recommendations based on user biomarker and lifestyle data.

## System Design
- FastAPI for backend
- LLM handles prompt-based recommendations
- MongoDB stores user input and logs
- Docker & GitHub Actions for environment and automation
- Using Pydantic for Data Validation and for typechecking

## Tech Stack
FastAPI · Python · MongoDB · Docker · GitHub Actions · TinyLlama

## Development Status
- [x] Project initialized
- [x] Basic FastAPI setup
- [ ] LLM integration
- [ ] MongoDB logging
- [ ] Docker containerization
- [ ] CI setup (GitHub Actions)

## Planned Features
- /predict endpoint
- /history/{user_id} endpoint
- Prompt tuning module
- Logging to MongoDB
- React FrontEnd
