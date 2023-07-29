# Anthropic hackathon

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from secrets_api import *
import requests

def get_html(url):
    return requests.get(url).text

FILE_PROMPT = "Can you tell me what are the main possible action on this webpage? I give you the raw HTML file between file XML tags."

completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{get_html('https://www.google.com/search?q=hello')}</file> {AI_PROMPT}",
)
print(completion.completion)