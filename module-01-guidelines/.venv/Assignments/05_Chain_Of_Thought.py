import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion
prompt= """
A person invested Rupees 10000 per month from Jan 1st 2026 till date in silver stock.
It is increasingly monthly on an average of 2%

Think and suggest me the following
1.Total invested
2.Total Returns
3.whether he should hold the stock or sell it
"""
response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("Response:")
print("-" * 50)
print(response)