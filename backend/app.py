"""
Backend flow simulation for Visa GenAI Assistant
"""

import json
from ai_engine import recommend_benefits

with open("benefit_rules.json") as f:
    rules = json.load(f)

def get_ai_response(category):
    return {
        "category": category,
        "benefits": recommend_benefits(category, rules)
    }

# Example run
if __name__ == "__main__":
    print(get_ai_response("travel"))
