import praw
import urllib.request
import os
import json
import random
import uuid
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot

# Load credentials from .env file
load_dotenv()
# Reddit credentials
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_username = os.getenv("REDDIT_USERNAME")
reddit_password = os.getenv("REDDIT_PASSWORD")
reddit_user_agent = os.getenv("REDDIT_USER_AGENT")

# Instagram credentials Go To .env to change it 
instagram_username = os.getenv("INSTA_USERNAME")
instagram_password = os.getenv("INSTA_PASSWORD")

# List of subreddits to scrape memes from
subreddits = ['subreddit1', 'subreddit2', 'subreddit3', 'subreddit']


# Creating Reddit instance here
reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, username=reddit_username, password=reddit_password, user_agent=reddit_user_agent)

directory = "./memes"
files = os.listdir(directory)

for file_name in files:
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        # do something with the file
        print(file_name) 

# Creating Instagram instance here
bot = Bot()
bot.login(username=instagram_username, password=instagram_password)

# Load previously posted memes from JSON file
if os.path.isfile("posted_memes.json"):
    with open("posted_memes.json", "r") as f:
        posted_memes = json.load(f)
else:
    posted_memes = []

# Makes a squre Background in Black color if your want to change color of the square you can by Changing Fill color to any RGB Value 
def make_square(im, min_size=1080, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    print("Original size "+str(x)+" X "+str(y))
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)    
    if(x > y):
        mod = size/x
        x = int(x * mod)
        y = int(y * mod)
    elif(x < y):
        mod = size/y
        x = int(x * mod)
        y = int(y * mod)

    new_im.paste(im.resize((x,y)), (int((size - x) / 2), int((size - y) / 2)))
    x, y = new_im.size
    print("New size "+str(x)+" X "+str(y))
    return new_im

# Loop through subreddits
while True:
    subreddit = random.choice(subreddits)
    # Get random post from subreddit
    post = random.choice(list(reddit.subreddit(subreddit).new(limit=100)))
    # Check if post is an image
    if post.url.endswith(".jpg") or post.url.endswith(".jpeg") or post.url.endswith(".png") or post.url.endswith(".gif") or post.url.endswith(".mp4"):
        # Check if post is not a video
        if not post.is_video:
            # Check if post has already been posted
            if post.id not in posted_memes:
                # Generate unique filename
                filename = os.path.join('memes', str(uuid.uuid4()) + os.path.splitext(post.url)[-1])
                # Download image
                urllib.request.urlretrieve(post.url, filename)
                image_path = os.path.join('.', filename)
                print(f"Downloaded {os.path.join('.', filename)}")
                # Add post ID to posted_memes list
                posted_memes.append(post.id)

                # Check if image_path is not empty
                if not image_path:
                    continue

                # Check if file has a valid image extension
                valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.mp4'}
                if not any(file_name.endswith(ext) for ext in valid_extensions for file_name in os.listdir("memes")):
                    print(f"Unknown file extension, skipping: {post.title}")
                    continue


                # Check image size and resize if necessary
                with Image.open(image_path) as img:
                    new_image = make_square(img)
                    new_image.save(image_path)
                    print("Resized image:", post.title)

                # Post image to Instagram
                try:
                    bot.upload_photo(image_path, caption=post.title)
                except Exception as e:
                    print("Error posting to Instagram:", str(e))
                    continue

                # Save posted memes to JSON file
                with open("posted_memes.json", "w") as f:
                    json.dump(posted_memes, f)

                print("Posted to Instagram:", post.title)

                # Exit loop after posting one meme
                break
            else:
                print("Post already posted:", post.title)
        else:
            print("Post is a video:", post.title)
    else:
        print("Unknown file extension, skipping:", post.title)

    # Add the current subreddit back to the list of subreddits
    subreddits.append(subreddit)


