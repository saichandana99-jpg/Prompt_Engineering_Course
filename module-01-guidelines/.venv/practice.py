from helper import  get_completion

prompt =""" 
Summarize the following on in one simple sentence:

Prompt engineering helps us write clear instructions for AI models.
"""
    
response = get_completion(prompt)
print(response)