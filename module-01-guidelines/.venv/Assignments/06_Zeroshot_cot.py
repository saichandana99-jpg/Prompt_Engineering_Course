import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion
prompt= """

Example 1:
Give me a plan for completing AI Mastery course in 60 days.
Consider the following points while giving me the plan.
1.As a mother of two kids I have 3 hours per day 
2.I had Good Knowledge in python

"""
response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("Response:")
print("-" * 50)
print(response)