# Anthropic hackathon

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from secrets_api import *
import requests
import re
import bs4

def get_html(url):
    return requests.get(url).text

def parse_actions(text):
  form_actions = re.findall(r'<action-form>(.*?)</action-form>', text)
  click_actions = re.findall(r'<action-click>(.*?)</action-click>', text)
  name = re.findall(r'<name>(.*?)</name>', text)
  return name, form_actions, click_actions

def fast_simplify_html(source_html):
   # Parse the HTML content using BeautifulSoup
    simplified_soup = bs4.BeautifulSoup(source_html, 'html.parser')
    
    # Remove attributes from all tags
    for tag in simplified_soup.find_all(True):
        tag.attrs = {}
    
    # Remove all script tags and their content
    for script_tag in simplified_soup.find_all('script'):
        script_tag.extract()   

    # Return the simplified HTML
    return str(simplified_soup)


def get_actions(url):
    fichier = open("actions_prompt.txt", "r")
    FILE_PROMPT = fichier.read()
    fichier.close()

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{get_html(url)}</file> {AI_PROMPT}",
    )
    print(completion.completion)
    return parse_actions(completion.completion)
