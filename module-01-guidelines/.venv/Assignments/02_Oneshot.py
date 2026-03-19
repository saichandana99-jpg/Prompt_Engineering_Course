import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt =""" 
Classify the sentiment of the sentence.
Example:
Input: "I like this course!"
Output:Positive

Now do the same for:

Input:"I Like this course but I do not have the proper time for practice"

Output:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse")
print("-" * 50)
print(response)