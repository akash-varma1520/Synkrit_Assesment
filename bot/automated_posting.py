import praw
import requests
import schedule
import time
import logging
import os
from comment_on_trending import comment_on_trending_posts

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define user input for posting time
post_time = input("Enter the time to post (in HH:MM format, 24-hour clock): ")

# Configure Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

# Define Groq API
groq_api_key = os.getenv("GROQ_API_KEY")
groq_url = "https://api.groq.com/openai/v1/chat/completions"  # Change this if necessary

# Function to generate content using Groq API
def generate_content():
    try:
        headers = {
            "Authorization": f"Bearer {groq_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mixtral-8x7b-32768",  # Replace with available model
            "messages": [{"role": "system", "content": "Generate a Reddit post about AI advancements."}]
        }

        response = requests.post(groq_url, headers=headers, json=data)

        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            logging.info("Generated content successfully.")
            return content
        else:
            logging.error(f"Failed to generate content. Status code: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error during content generation: {e}")
        return None

# Function to post to Reddit
def post_to_reddit(content):
    try:
        subreddit = reddit.subreddit("your_subreddit")  # Replace with your subreddit name
        subreddit.submit("AI Advancements in 2025", selftext=content)
        logging.info("Posted to Reddit successfully.")
    except Exception as e:
        logging.error(f"Failed to post to Reddit: {e}")

# Job function that combines content generation and posting
def job():
    logging.info("Generating content...")
    content = generate_content()
    if content:
        logging.info("Posting content to Reddit...")
        post_to_reddit(content)

# Schedule the job at user-specified time
schedule.every().day.at(post_time).do(job)

# Function to run the scheduler
def run_scheduler():
    logging.info(f"Bot is running. Waiting to post at {post_time}.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduling process
if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        logging.info("Bot interrupted. Exiting...")
        

schedule.every(1).hour.do(comment_on_trending_posts)