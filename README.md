# GenAI Visa Benefits Assistant

This project is a prototype of a GenAI-based Visa Benefits Assistant
that helps users understand and utilize their Visa card benefits
in a simple and personalized way.

The system separates user interaction (frontend) and intelligence
logic (backend) to demonstrate a scalable AI-driven architecture.

---

## Frontend Overview

The frontend provides the user-facing interface of the application.

### Purpose
- Collect basic user information through a login page
- Display Visa card details and benefit recommendations
- Act as the interaction layer for AI-generated outputs

### Pages
- Login Page  
  Collects user details and simulates authentication

- Dashboard Page  
  Displays Visa card information and AI-recommended benefits

### Technologies Used
- HTML
- CSS
- JavaScript

The frontend is intentionally lightweight and does not contain
any AI or decision-making logic.

---

## Backend Overview

The backend represents the intelligence and reasoning layer
of the GenAI Visa Benefits Assistant.

### Backend Components
- `benefit_rules.json`  
  Contains structured Visa benefit rules used as input data

- `ai_engine.py`  
  Implements GenAI-inspired reasoning logic to select
  relevant benefits based on user intent

- `app.py`  
  Simulates backend flow and acts as an API layer between
  frontend and AI logic

### Gen-AI Approach
- Rule-based logic used as a GenAI placeholder
- Mimics how Large Language Models reason over policy text
- Designed to be easily replaceable with GPT / Azure OpenAI

---

## How the System Works

1. User interacts with the frontend
2. User intent (travel, dining, shopping) is identified
3. Backend reads structured benefit rules
4. AI reasoning logic selects applicable benefits
5. Simplified recommendations are shown on the frontend

---

## Current Status

- Prototype / academic-level implementation
- No real Visa APIs or transaction data used
- Focus on architecture, reasoning flow, and explainability

---

## Future Scope

- LLM integration (GPT / Azure OpenAI)
- Machine learning models for benefit prediction
- Real-time transaction analysis
- Multilingual support

---

## Disclaimer

This project is created for educational and demonstration purposes.
