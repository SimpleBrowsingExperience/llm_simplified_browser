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

Imagine that you would like to search for pancakes on Bing.

1. You first request the traditional URL: `bing.com/search?q=pancakes`
2. You will then be seeing the simple representation of the page.
```
    Requesting https://www.bing.com/search?q=pancakes
    
    Website: Bing: pancakes

    Summary: Search results page on Bing for the keyword "pancakes". Shows links to various pancake recipes and information pages.

    Elements
    Option 1: Good Old-Fashioned Pancakes Recipe (with Video)
    Option 2: How to Make Pancakes | Easy Homemade Pancakes Recipe
    Option 3: Easy Basic Pancakes Recipe (With Video and Step by Step)

    Actions
    Option 4: Search for pancakes
    Option 5: See pancake recipes
    Option 6: See pancake recipe tutorial
    Option 7: See classic pancake recipe
    Option 8: See basic pancake recipe

    q: quit

    Select an option:

```

3. If you select option 2 for instance, here is what you will see next
```
    Requesting https://www.foodnetwork.com/recipes/food-network-kitchen/pancakes-recipe-1913844

    Website: Food Network: Pancakes Recipe
    
    Summary: This page contains a recipe for homemade pancakes from Food Network. The recipe has a list of ingredients, instructions with photos and videos, and nutritional information.
    
    Elements
    Option 1: Pancakes Recipe - Food Network
    Option 2: How to Make Pancakes Video
    Option 3: Nutrition Information Per Serving

    Actions
    Option 4: Search for recipes
    Option 5: Watch Full Seasons
    Option 6: See All Recipes
    Option 7: See All Shows
    Option 8: See All Chefs

    q: quit

    Select an option:
```

4. You can then type `q` to exit the demonstration

## External documentation
- Figma: https://www.figma.com/file/NExOzeXMCJ4v1M5NQJULx4/BrowsingCompanion?type=design&node-id=1-3&mode=design
- Git: https://github.com/SimpleBrowsingExperience/llm_simplified_browser

## Future versions

In future versions, we are aiming at handling more and more standard items
appearing on a web page, such as search forms, authentication pages,
images and videos.
