# Anthropic hackathon

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from secrets_api import *
import re
import bs4
from urllib.request import Request, urlopen
import time

DEBUG = False

def get_html(url):
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    if DEBUG:
        print(f"Requesting {url}")
    time.sleep(2)
    mybytes = urlopen(req).read()
    mystr = mybytes.decode("utf8")
    return mystr

def fast_simplify_html(source_html):
   # Parse the HTML content using BeautifulSoup
    simplified_soup = bs4.BeautifulSoup(source_html, 'html.parser')
    
    # Remove attributes from all tags except href
    for tag in simplified_soup.find_all(True):
        # tag.attrs = {}
        tag.attrs = {} if 'href' not in tag.attrs else {'href': tag.attrs['href']}
    
    # Remove all script tags and their content
    for script_tag in simplified_soup.find_all('script'):
        script_tag.extract()
    
    for style_tag in simplified_soup.find_all('style'):
        style_tag.extract()

    # Replace elements with only one child with their child element
    # except for <a> tags and <html> tags
    for tag in simplified_soup.find_all(True):
        if len(tag.contents) == 1 and tag.name != 'a' and tag.name != 'html':
            tag.replace_with(tag.contents[0])
            
    # Remove all comments from the HTML
    comments = simplified_soup.find_all(text=lambda text: isinstance(text, bs4.Comment))
    for comment in comments:
        comment.extract()
    
    # Return the simplified HTML
    #print(str(simplified_soup))
    return str(simplified_soup)


def get_simplified_html(url):
    return fast_simplify_html(get_html(url))

###

def parse_actions(text):
  form_actions = re.findall(r'<action-form>(.*?)</action-form>', text)
  click_actions = re.findall(r'<action-click url="(.*?)">(.*?)</action-click>', text)
  return form_actions, click_actions

def parse_elements(text):
  name = re.findall(r'<name>(.*?)</name>', text)[0]
  elements = re.findall(r'<element url="(.*?)">(.*?)</element>', text)
  summary = re.findall(r'<summary>(.*?)</summary>', text)[0]
  return name, summary, elements

def get_actions(html):
    fichier = open("actions_prompt.txt", "r")
    FILE_PROMPT = fichier.read()
    fichier.close()
    if DEBUG:
        print("API request of actions")
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{html}</file> {AI_PROMPT}",
    )
    if DEBUG:
            print(completion.completion)
    return parse_actions(completion.completion)

def get_elements(html):
    fichier = open("elements_prompt.txt", "r")
    FILE_PROMPT = fichier.read()
    fichier.close()
    if DEBUG:
        print("API request for elements")
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{html}</file> {AI_PROMPT}",
    )
    if DEBUG:
        print(completion.completion)
    return parse_elements(completion.completion)
