# %%
from actions_from_website import get_html
import bs4
import requests

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
    
    # Return the simplified HTML
    return str(simplified_soup)

def get_simplified_html(url):
    return fast_simplify_html(get_html(url))

google_query = "sunglasses"
# r = get_simplified_html(f"https://www.google.com/search?q={google_query}")
r = get_simplified_html(f"https://www.nytimes.com/wirecutter/reviews/best-cheap-sunglasses/")
print(r)
# %%
