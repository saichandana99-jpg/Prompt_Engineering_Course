import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt="""
Classify the support ticket into the correct category.

Categories: Billing Issue, Technical Issue, Account Management, General Inquiry

Examples:
Ticket: "I was charged twice for my subscription."
Category: Billing Issue

Ticket: "App crashes when I try to open it."
Category: Technical Issue

Ticket: "How do I reset my password?"
Category: Account Management

Now classify:
Ticket: "What are your business hours?"
Category:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)