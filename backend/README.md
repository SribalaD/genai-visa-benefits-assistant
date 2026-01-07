# Backend – GenAI Visa Benefit Engine

This backend implements the decision and reasoning layer of the
GenAI-based Visa Benefits Assistant.

---

## Backend Structure

- benefit_rules.json  
  Structured dataset containing Visa benefit rules

- ai_engine.py  
  GenAI-inspired reasoning logic for benefit selection

- app.py  
  Backend flow and API simulation connecting frontend to AI logic

---

## How It Works

1. Frontend sends user intent (category)
2. Backend reads benefit rules
3. AI reasoning engine selects relevant benefits
4. Simplified response is returned to frontend

---

## Gen-AI Design

- Rule-based logic used as a Gen-AI placeholder
- Architecture is LLM-ready (GPT / Azure OpenAI)
- Focus on explainability and personalization

---

## Current Status

- Prototype implementation
- No real transaction data
- Designed for academic and hackathon use
