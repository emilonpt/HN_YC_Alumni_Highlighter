import requests
from bs4 import BeautifulSoup
import time
import random

def get_usernames_from_page(url):
    usernames = set()  # we don't need duplicates

    while url:
        time.sleep(random.random()*2) # throttling
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all launch subtext (subline)
        launch_posts = soup.find_all('span', class_='subline')  # auxselector to iretate through posts

        # Extract usernames from launch posts
        for post in launch_posts:
            username = post.find('a', class_='hnuser')  #hnuser selects usernames
            if username:
                usernames.add(username.text)

        # Find the "more" button and get the URL of the next page
        more_button = soup.find('a', class_='morelink')  #morelink selects more button
        url = "https://news.ycombinator.com/" + more_button['href'] if more_button else None

    return usernames

def save_usernames_to_file(usernames, filename):
    # Read existing usernames from the file
    existing_usernames = set()
    try:
        with open(filename, 'r') as file:
            existing_usernames = set(file.read().splitlines())
    except FileNotFoundError:
        # If the file doesn't exist, it will be created later
        pass

    # Append new usernames to the file
    with open(filename, 'a') as file:
        for username in usernames:
            if username not in existing_usernames:
                file.write(username + '\n')

def main():
    url = 'https://news.ycombinator.com/launches'  # starting point
    usernames = get_usernames_from_page(url)
    save_usernames_to_file(usernames, 'usernames.txt')

if __name__ == '__main__':
    main()
