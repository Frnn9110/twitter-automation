import asyncio

from loguru import logger

from config import config
from data.Account import Twitter
from modules.twitter_account import TwitterAccount
from modules.twitter_tweet import TwitterTweet
from utils.file_system import load_file


# if __name__ == '__main__':
#     # accounts = ['a_1', 'a_2', 'a_3', 'a_4', 'a_5']
#     # proxies = ['p_1', 'p_2', 'p_3', 'p_4', 'p_5']
#     # user_agents = ['u_1', 'u_2', 'u_3', 'u_4', 'u_5']
#     # data = list(zip(accounts, proxies, user_agents))
#     # for id, (auth_token, proxy, user_agent) in enumerate(data, start=1):
#     #     print(id, data)
async def async_run():
    r = await tweet.run()
    print(r)


if __name__ == '__main__':
    twitter = Twitter()
    cookie_list = twitter.twitter_auth_v2_cookies
    del (cookie_list[0])
    data = list(zip(cookie_list, config.PROXIES, config.USER_AGENTS))

    accounts = []

    for id, (cookies, proxy, user_agent) in enumerate(data, start=1):
        if id not in [7]:
            continue
        for cookie in cookies:
            if cookie['name'] == 'auth_token':
                auth_token = cookie['value']
        try:
            account = TwitterAccount(
                id=id, auth_token=auth_token, user_agent=user_agent, proxy=proxy
            )
        except Exception as e:
            logger.error(f"Error while creating Account #{id}: {e}")
            continue

        accounts.append(account)

    tweet = TwitterTweet(accounts[0], accounts)
    asyncio.run(async_run())
