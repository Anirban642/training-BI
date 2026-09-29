.PHONY: help install dev prod qa test clean

help:
	@echo "Available commands:"
	@echo "  make install    Install all dependencies"
	@echo "  make dev        Run server with .env.dev (Development mode)"

install:
	pip install -r requirements.txt

# Run Development Server (loads .env.dev)
dev:
	ENV=dev uvicorn app.main:app --reload --port 8000
