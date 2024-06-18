import asyncio

from curl_cffi import requests
from loguru import logger

from config import config
from data.Account import Twitter
from modules.twitter_account import TwitterAccount
from modules.twitter_tweet import TwitterTweet
from utils.file_system import load_file


session = requests.Session(impersonate='chrome120')
resp = session.get('https://travel-eye.org/ip.json?token=zhegemeiyouyongde')
print(resp)