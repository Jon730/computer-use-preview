import json



prompt = """
Using the url below as a starting point, please produce an up-to-date,
json formatted response that updates the information here:

# Prices in USD per 1 Million Tokens
# Source: https://cloud.google.com/vertex-ai/generative-ai/pricing
PRICING_RATES = 
"""

initial_url = "https://cloud.google.com/vertex-ai/generative-ai/pricing"
highlight_mouse = True
model_name = "gemini-2.5-computer-use-preview-10-2025"

PLAYWRIGHT_SCREEN_SIZE = (1440, 900)

__all__ = [
    "prompt", "initial_url", "highlight_mouse", "model_name",
    "PLAYWRIGHT_SCREEN_SIZE",
]