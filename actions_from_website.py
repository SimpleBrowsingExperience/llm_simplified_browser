"""
Anthropic hackathon
This file contains all auxiliary functions our simple browser needs
"""

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from secrets_api import *
import re
import bs4
from urllib.request import Request, urlopen
import time


DEBUG = False


def get_html(url):
    """
    Given a url as input, returns the raw HTML code
    """

    # Pretending to be a real browser eg Mozilla
    # To avoid being seen as a bot
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    # Debug mode
    if DEBUG:
        print(f"Requesting {url}")

    # Sleeping for 2 sec
    time.sleep(2)

    # Opening and reading HTML code
    mybytes = urlopen(req).read()
    mystr = mybytes.decode("utf8")
    return mystr


def fast_simplify_html(source_html):
    """
    This function preprocesses HTML code to avoid sending Claude
    too many tokens as context
    Recall that most of the tokens in an HTML code are actually useless
    to understand the meaning of a page
    """

    # Parse the HTML content using BeautifulSoup
    simplified_soup = bs4.BeautifulSoup(source_html, 'html.parser')
    
    # Remove attributes from all tags except href
    for tag in simplified_soup.find_all(True):
        # tag.attrs = {}
        tag.attrs = {} if 'href' not in tag.attrs else {'href': tag.attrs['href']}
    
    # Remove all script tags and their content
    for script_tag in simplified_soup.find_all('script'):
        script_tag.extract()
    
    # Remove all style tags and their content
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
    return str(simplified_soup)


def get_simplified_html(url):
    """
    This function is simply composing get_html with fast_simplify_html
    """
    return fast_simplify_html(get_html(url))


def parse_actions(text):
    """
    This is the parser for available actions, in a XML like format
    Distinguishing between form actions and click actions
    """
    form_actions = re.findall(r'<action-form>(.*?)</action-form>', text)
    click_actions = re.findall(r'<action-click url="(.*?)">(.*?)</action-click>', text)
    return form_actions, click_actions

def parse_elements(text):
    """
    This is the parser for the name of the website,
    the summary of the page and available elements, in a XML like format
    """
    name = re.findall(r'<name>(.*?)</name>', text)[0]
    elements = re.findall(r'<element url="(.*?)">(.*?)</element>', text)
    summary = re.findall(r'<summary>(.*?)</summary>', text)[0]
    return name, summary, elements

def get_actions(html):
    """
    This function submits the Claude query with the actions prompt
    to retrieve available actions in XML format
    """
    # Retrieving the actions prompt
    fichier = open("actions_prompt.txt", "r")
    FILE_PROMPT = fichier.read()
    fichier.close()

    # Debug mode
    if DEBUG:
        print("API request of actions")

    # API query
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{html}</file> {AI_PROMPT}",
    )

    # Debug mode
    if DEBUG:
            print(completion.completion)

    # Parsing actions
    return parse_actions(completion.completion)


def get_elements(html):
    """
    This function submits the Claude query with the elements prompt
    to retrieve available elments in XML format
    """
    # Retrieving the actions prompt
    fichier = open("elements_prompt.txt", "r")
    FILE_PROMPT = fichier.read()
    fichier.close()
    
    # Debug mode
    if DEBUG:
        print("API request for elements")
    
    # API query
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {FILE_PROMPT} <file>{html}</file> {AI_PROMPT}",
    )

    # Debug mode
    if DEBUG:
        print(completion.completion)

    # Parsing elements
    return parse_elements(completion.completion)
