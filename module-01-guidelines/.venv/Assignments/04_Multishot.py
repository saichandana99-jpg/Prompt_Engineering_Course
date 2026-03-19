import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion
prompt= """
Summarize the text in one sentence.

Examples:
Text: "Artificial Intelligence is transforming industries by automating tasks and improving efficiency."
Summary: "AI is improving efficiency by automating tasks."

Text: "Online education platforms allow students to learn from anywhere in the world."
Summary: "Online platforms enable global learning."

Now summarize:
Text: "Electric vehicles reduce carbon emissions and are becoming more popular due to environmental concerns."
Summary:
"""
response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("Response:")
print("-" * 50)
print(response)