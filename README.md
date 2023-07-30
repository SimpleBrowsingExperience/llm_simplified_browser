# SimpleBrowser

This project is the result of the collaboration between Nathan, Fabien, Elie,
and Joachim for Anthropic Hackathon Claude 2 (July 29 - 30, 2023).

## Description

The goal of the project is to design a simplified browser, naturally called
**SimpleBrowser**, initially destined to users that are either visually 
impaired, technologically illiterate. More generally, we are also targetting 
users willing to seamlessly browse with a pure, accessible and homogeneous 
design across websites.

With SimpleBrowser, all websites are always appearing in the exact same format, 
with the exact same design, achieving full consistency and responsiveness on all
devices.

The visualization of pages is structured around the following items:
- name of the page
- summary of the content
- available elements (if the main purpose of the page is to display a list of
elements such as the results of a Google search query)
- available actions, distinguishing between links to click on and forms (field)
to fill in

To ensure accessibilility for all our users, no more than 3 elements or 5 actions
are displayed on a given page!

## Contents

At this stage, the Git repository contains:
- `actions_prompt.txt`: Claude prompt to retrieve available actions
- `elements_prompt.txt`: Claude prompt to retrieve available elements,
as well as name and summary for the web page
- `actions_from_website.py`: Python script for auxiliary functions to query
the HTML code of a website, preprocess it locally, sending simplified
code to Claude for analysis and parsing the output
- `main.py`: main Python script for the project, allowing a simplified browsing
on a console-like mode and a light graphical implementation

## Demonstration

If time allows it, demonstration with images!

## External documentation
- Figma: https://www.figma.com/file/NExOzeXMCJ4v1M5NQJULx4/BrowsingCompanion?type=design&node-id=1-3&mode=design
- Git: https://github.com/SimpleBrowsingExperience/llm_simplified_browser

## Future versions

In future versions, we are aiming at handling more and more standard items
appearing on a web page, such as search forms, authentication pages,
images and videos.
