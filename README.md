# AI-Powered Health Risk Profiler

## Description
This project is a backend API that analyzes lifestyle survey data and generates
a structured health risk profile. It supports incomplete data handling and
produces non-diagnostic recommendations.

## Features
- Accepts health survey input (JSON)
- Detects missing fields
- Calculates risk level using rule-based logic
- Returns actionable health recommendations
- Includes guardrails for incomplete profiles

## Tech Stack
- Python
- FastAPI
- Pydantic

## Setup Instructions

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
