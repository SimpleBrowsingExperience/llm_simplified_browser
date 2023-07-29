# Anthropic hackathon

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from secrets_api import *
import requests
import re

def get_html(url):
    return requests.get(url).text

def parse_actions(text):
  form_actions = re.findall(r'<action-form>(.*?)</action-form>', text)
  click_actions = re.findall(r'<action-click>(.*?)</action-click>', text)

  return form_actions, click_actions

def get_actions(url):
    fichier = open("actions_prompt.txt", "r")
    FILE_PROMPT = fichier.read()
    fichier.close()

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{get_html(url)}</file> {AI_PROMPT}",
    )
    return parse_actions(completion.completion)

print(get_actions("https://google.com/"))