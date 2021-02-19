# Made by Morigan LETOURNEAU, student in Game Programming x)
import requests
from bs4 import BeautifulSoup
import random

# Used to identify which url we are using for what the user asked for
def choose_url(x):
    if 'hello' in x:
        return hello_url
    elif 'common' in x:
        return common_phrases_url
    else:
        return "404 not found"

# Function which returns the all the content sections in a list
def get_wiki_how_sections():
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("div", class_="section steps sticky")
    return result

# Function which returns all the titles of the content sections in a list
def get_wiki_how_titles(sections):
    if sections == None:
        sections = get_wiki_how_sections()

    result = []
    for section in sections:
        result.append(section.find("span", class_="mw-headline"))
    return result

# Function used to print the content sections' titles in a readable way with an index
def print_titles():
    temp = 0
    for title in titles:
        print(str(temp) + "\t" + title.text)
        temp += 1
    print("\n")


hello_url = "https://www.wikihow.com/Say-Hello-in-Different-Languages"
common_phrases_url = "https://www.wikihow.com/Say-Common-Phrases-in-Multiple-Languages"

sections = []
titles = []

print("Hello!")
user_input = input("What do you want to learn ? 'hello' / 'common' / 'nothing' / 'help' >\t").lower()

if 'hello' in user_input or 'common' in user_input:
    print("Let's go ! Here what I can offer you : \n")
    url = choose_url(user_input)
    response = requests.get(url)

    if response.ok:
        # Get the different content sections of the page
        sections = get_wiki_how_sections()
        # Get the titles of each one
        titles = get_wiki_how_titles(sections)

        # Show the title to the user with an index next to each title so user can choose
        print_titles()

        # Ask the user which content does he want
        user_input = int(input("What does interest you for today ? (give negative value for a random one) :) >\t"))
        # If the given value is negative take a random index
        if user_input < 0:
            user_input = random.randint(0, len(sections) - 1)
        # Select the content chosen by the user
        section_content = sections[user_input]

        # The two website pages are not identically made
        # So I've to identify which one we're using
        # So I know how to get the information
        if url == hello_url:
            # Each section has a different step for each language
            # So I'm getting all these steps
            steps = section_content.find_all("div", class_="step")

            # We choose a random index to choose a random step
            # That is to say a random language
            random_integer = random.randint(0, len(steps) - 1)

            # Getting the bolded text on the website
            # To identify the chosen language
            message = steps[random_integer].find("b").text

            # Splitting the bolded text to get the last word (language)
            messages = message.split()
            language = messages[len(messages) - 1]
            # Splitting it again to remove the ':'
            language = language.split(":")
            language = language[0]

            # Ask if user want to learn in this language
            # Just asking an input so the player can try to guess or remember the information
            user_input = input("Do you want to learn hello in " + language + " ? >\t").lower()
            if 'y' in user_input:
                # Getting the entire text of the step
                message = steps[random_integer].text

                # Splitting the text with ':' so I can pick the last part of the content
                message = message.split(":")
                message = message[len(message) - 1]

                # Print the learning of the day
                print(message)

        elif url == common_phrases_url:
            # Get the unordered list of the HTML
            section_content = section_content.find("ul")

            # Get all the elements of this list
            section_content = section_content.find_all("li")

            # Choose a random index to choose a random element of the list
            random_integer = random.randint(0, len(section_content) - 1)

            # Removing the ':' and splitting the chosen language and the information
            message = section_content[random_integer].text
            message = message.split(":")

            # Identify the chosen language and removing '\n'
            language = message[0]
            if "\n" in language:
                language = language.split("\n")
                language = language[1]

            # Ask if user want to learn in this language
            # Just asking an input so the player can try to guess or remember it
            user_input = input("Do you want to learn something in " + language).lower()
            if 'y' in user_input:
                # Print the learning of the day
                print("It is: " + message[1])
    # If the internet connection doesn't work or any other possibilities
    else:
        print("Couldn't access to the website sorry :( ")
# If the player put help
elif 'help' in user_input:
    print(f"""
        All the given information given by this program are picked up on these urls:
        - {hello_url}
        - {common_phrases_url}
        """)

# If something else than 'common', 'hello' or 'help' is given by the user
else:
    print("""
    Sad, hoping you're having a good day !
    See you soon!!
    """)
