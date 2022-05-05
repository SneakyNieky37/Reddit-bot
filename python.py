import json
import praw
import requests
subr = input('what subreddit would you like to post in?\n>')
credentials = "client_secrets.json"
with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])



subreddit = reddit.subreddit(subr)

title = input('title:')
selftext = input("text:")

subreddit.submit(title,selftext=selftext)