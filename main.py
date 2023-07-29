from actions_from_website import *

actual_site = "https://sfbay.craigslist.org/"
selection = ""

def submit_form(form):
    pass

def submit_click(click):
    pass

while True:
    website_name, forms, clicks = get_actions(actual_site)
    i = 1
    print(f"Website: {website_name[0]}")
    for form in forms:
        print(f"Option {i}: {form}")
        i += 1
    for click in clicks:
        print(f"Option {i}: {click}")
        i += 1
    print("q: quit")
    selection = input("Select an option: ")
    if selection == "q":
        break
    elif selection.isdigit():
        selection = int(selection)
    else:
        print("Invalid selection")
        continue
    if selection <= len(forms):
        form = forms[selection - 1]
        submit_form(form)
    elif selection <= len(forms) + len(clicks):
        click = clicks[selection - len(forms) - 1]
        submit_click(click)
    else:
        print("Invalid selection")
        continue

