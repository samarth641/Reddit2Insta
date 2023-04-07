# Instagram Reddit Meme Bot

This bot scrapes memes from random subreddits and posts them to Instagram. It uses PRAW to scrape memes from Reddit and InstagramAPI to post memes to Instagram. 

## Prerequisites

- Python 3.8 or higher
- pip
- virtualenv
- Instagram account
- Reddit account

## Installation

1. Clone the repository and navigate into the directory:
```sh
git clone https://github.com/samarth641/Reddit2Insta.git
```


2. Install the required modules by Running this code In terminal:

 ```sh 
 pip install -r requirements.txt 
 ```

3. Create a Reddit application and a corresponding client ID and client secret. Instructions can be found [Here](https://github.com/reddit-archive/reddit/wiki/OAuth2).


4. Create an Instagram account and generate an API key. You can skip this step and only use your instagram account username and password as we are only using that to connect to `InstagramAPI`  [Documentation Here](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started).

3. Go to `.env` file in the root of the directory and add the following variables with your own credentials:


```python
REDDIT_CLIENT_ID=<your_reddit_client_id>
REDDIT_CLIENT_SECRET=<your_reddit_client_secret>
REDDIT_USERNAME=<your_reddit_username>
REDDIT_PASSWORD=<your_reddit_password>
REDDIT_USER_AGENT=<your_reddit_user_agent>
INSTA_USERNAME=<your_instagram_username>
INSTA_PASSWORD=<your_instagram_password>
```

# Changing subreddits

To change the subreddits that the bot scrapes memes from, edit the subreddits variable in the reddit2insta.py file. Add or remove subreddits as needed, and separate them by commas. For example:

```python
subreddits = ['subreddit1', 'subreddit2', 'subreddit3', 'subreddit']

```

6.  Run the bot: 

```python 
python reddit2insta.py
```


## Configuration

- `subreddits`: A list of subreddits to scrape memes from. Replace the default subreddits with your own.
- `directory`: The directory where the downloaded memes will be saved.
- `posted_memes.json`: A JSON file that keeps track of the memes that have been posted to Instagram.

## Contributing

Contributions are welcome! Please open an issue or pull request for any changes you would like to make.


## 🔗 Social Links
[![Buy me a Coffee ](https://img.shields.io/badge/buymeacoffee-FFBF00?style=for-the-badge&logo=buymeacoffee&logoColor=white)](hhttps://www.buymeacoffee.com/SamarthVerulkar)

[![instagram](https://img.shields.io/badge/Instagram-bc2a8d?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/samarth_verulkar/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarth-verulkar-89255a227/)

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/samarthverulkar)


## Authors

- [@Samarth Verulkar ](https://www.github.com/samarth641)

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.


