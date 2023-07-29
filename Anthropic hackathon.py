# Anthropic hackathon

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from secrets_api import *
import requests

def get_html(url):
    return requests.get(url).text

fichier = open("actions_prompt.txt", "r")
FILE_PROMPT = fichier.read()
fichier.close()

completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{get_html('https://www.google.com')}</file> {AI_PROMPT}",
)
print(completion.completion)