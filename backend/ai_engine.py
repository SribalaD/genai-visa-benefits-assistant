"""
AI Reasoning Engine (Prototype)

Simulates how a Gen-AI system selects
Visa benefits based on user intent.
"""

def recommend_benefits(category, rules):
    if category in rules:
        return rules[category]["benefits"]
    return ["No matching benefits found"]
