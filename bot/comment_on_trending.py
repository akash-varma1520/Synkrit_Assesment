import praw
import logging
import schedule
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id="iS2zAEt74uzoMJ8HGftd0Q",
    client_secret="AS7iqK7TOzH-nIbGcRJbjecs3-znig",
    user_agent="Groq AI Bot by /u/Leather-Zucchini-852",
    username="Leather-Zucchini-852",
    password="Akash123"
)

# Function to comment on trending posts
def comment_on_trending_posts():
    try:
        subreddit = reddit.subreddit("technology")  # Replace with a valid subreddit
        hot_posts = subreddit.hot(limit=5)  # Fetch top 5 hot posts
        for post in hot_posts:
            post.reply("Interesting discussion! AI is evolving fast.")  # Custom comment
            logging.info(f"Commented on post: {post.title}")
    except Exception as e:
        logging.error(f"Error in commenting on trending posts: {e}")

# Schedule the function to run daily
schedule.every().day.at("09:00").do(comment_on_trending_posts)  # Set desired time

# Run the scheduler
def run_scheduler():
    logging.info("Scheduler is running. Waiting for the next job...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
