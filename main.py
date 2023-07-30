from actions_from_website import *

actual_site = "https://www.bing.com/search?q=pancakes"
selection = ""

def submit_form(form):
    pass

def submit_click(click):
    pass

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

