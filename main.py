"""
Anthropic Hackathon
This is the main script that allows browsing with interactions
on SimpleBrowser
"""

from actions_from_website import *

actual_site = "" # Actual site to be browsed
selection = "" 


def generate_page(name, summary, elements, forms, clicks):
    """
    Generates HTML code for the simplified page
    and writes output in a file
    """
    # Headers
    html = f"<html>"
    html += f"<head><title>{name}</title>"
    html += """
    <link rel="stylesheet" type="text/css" href="style.css">"""

    # Adding name and summary
    html += f"</head><body><h1>{name}</h1>"
    html += f"<p>{summary}</p>"

    # Adding elements if they exist
    for url, text in elements:
        html += f"<div class='element'><a href='{url}'>{text}</a></div>"
    
    # Adding actions
    html += "<div>"
    for form in forms:
        html += f"<div class='action'>{form}</div>"

    for url, text in clicks:
        html += f"<br><div class='action'>>> <a href='{url}'>{text}</a></div>"

    html += "</div></body></html>"

    # Writing output in an HTML file
    fichier = open(f"pages/{name}.html", "w")
    fichier.write(html)
    fichier.close()


# Main code
actual_site = input("Enter keywords for your research: ")
actual_site = actual_site.replace(" ", "+")
actual_site = "https://www.bing.com/search?q=" + actual_site

same_site = False

while True:
    if not same_site:
        # Interactions with console mode
        print(f"Fetching URL: {actual_site}")

        # Getting simplified HTML code
        html = get_simplified_html(actual_site)

        # Retrieving name, summary, elements
        name, summary, elements = get_elements(html)

    print(f"Website: {name}")
    print(f"Summary: {summary}")

    # Showing elements and associated keys
    i = 1
    for element in elements:
        print(f"Option {i} : {element[1]}")
        i += 1

    if not same_site:
        # Retrieving actions
        forms, clicks = get_actions(html)

    # Showing actions and associated keys
    for form in forms:
        print(f"Option {i}: {form}")
        i += 1
    
    for click in clicks:
        print(f"Option {i}: {click[1]}")
        i += 1
    
    # Quit option
    print("a: ask something about the page \nq: quit")

    # Generates HTML code of the simplified page
    generate_page(name, summary, elements, forms, clicks)

    # Asking user for selection
    selection = input("Select an option: ")

    if selection == "q":
        # Quitting
        break
    elif selection.lower() == "a":
        # Custom prompt
        prompt = input("Please enter ask what you want to know: ")
        response = get_custom(html, prompt)
        print(response)
        same_site = True
        continue
    
    elif selection.isdigit():
        selection = int(selection) - 1 
    
    else:
        print("Invalid selection")
        same_site = True
        continue

    old_site = actual_site
    
    if selection < len(elements):
        # Clicking on an element
        actual_site = elements[selection][0]
    
    elif selection < len(forms):
        # Forms are not yet implemented
        print("Not implemented yet")
    
    elif selection < len(clicks):
        actual_site = clicks[selection - len(forms) - len(elements)][0]
    
    else:
        same_site = True
        print("Invalid selection")
        continue

    same_site = False
    # Some url are given relatively to the current one
    if not ("http" in actual_site):
        actual_site = old_site + actual_site
