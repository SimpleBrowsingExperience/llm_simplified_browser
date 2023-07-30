from actions_from_website import *

actual_site = "https://www.bing.com/search?q=pancakes"
selection = ""

def generate_page(name, summary, elements, forms, clicks):

  html = f"<html>"
  html += f"<head><title>{name}</title>"
  html += """
  <link rel="stylesheet" type="text/css" href="style.css">"""

  html += f"</head><body><h1>{name}</h1>"
  html += f"<p>{summary}</p>"

  for url, text in elements:
    html += f"<div class='element'><a href='{url}'>{text}</a></div>"
  
  html += "<div>"
  for form in forms:
    html += f"<div class='action'>{form}</div>"

  for url, text in clicks:
    html += f"<br><div class='action'>>> <a href='{url}'>{text}</a></div>"

  html += "</div></body></html>"

  fichier = open(f"pages/{name}.html", "w")
  fichier.write(html)
  fichier.close()

while True:
    html = get_simplified_html(actual_site)
    name, summary, elements = get_elements(html)

    print(f"Website: {name}")
    print(f"Summary: {summary}")

    i = 1
    for element in elements:
        print(f"Option {i} : {element[1]}")
        i += 1

    forms, clicks = get_actions(html)

    for form in forms:
        print(f"Option {i}: {form}")
        i += 1
    for click in clicks:
        print(f"Option {i}: {click[1]}")
        i += 1
    print("q: quit")
    generate_page(name, summary, elements, forms, clicks)
    selection = input("Select an option: ")
    if selection == "q":
        break
    elif selection.isdigit():
        selection = int(selection) - 1 
    else:
        print("Invalid selection")
        continue
    if selection < len(elements):
        actual_site = elements[selection][0]
    elif selection < len(forms):
        print("Not implemented yet")
    elif selection < len(clicks):
        actual_site = clicks[selection][0]
    else:
        print("Invalid selection")

