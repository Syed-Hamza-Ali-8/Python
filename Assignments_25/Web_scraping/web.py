import requests
from bs4 import BeautifulSoup

def get_github_profile_image(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to retrieve the page.")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        img_tag = soup.find('img', {'alt': 'Avatar'})  
        if img_tag:
            profile_img_url = img_tag['src']
            print(f"Profile Image URL: {profile_img_url}")
        else:
            print("Profile image not found.")
            
    except Exception as e:
        print("An error occurred:", e)

github_url = input("Enter GitHub Profile URL: ")

get_github_profile_image(github_url)
