import asyncio
import csv

from twikit import Client

USERNAME = ''
EMAIL = ''
PASSWORD = ''

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD,
        cookies_file='cookies.json'
    )
    
    # Use the numeric user id for @KingJames instead of the username string.
    user_id = 23083404  # Replace with the verified numeric user id for @KingJames.
    count = 1
    tweets = await client.get_user_tweets(user_id, 'Tweets', count)
    
    # Open CSV file for writing tweet texts
    with open("tweets.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow(["Tweet Text"])
        
        # Write tweets from the first batch
        for tweet in tweets:
            writer.writerow([tweet.text])
        
        # Continuously fetch next batches and write to CSV until no more tweets are available
        while True:
            tweets = await tweets.next()
            # If no tweets are returned, break out of the loop
            if not tweets:
                break
            for tweet in tweets:
                writer.writerow([tweet.text])

asyncio.run(main())
