import praw
import json

def load_config():
    """Load the configuration from the config.json file."""
    with open("config.json") as config_file:
        return json.load(config_file)

def authenticate():
    """Authenticate with Reddit API using credentials from config.json."""
    config = load_config()

    reddit = praw.Reddit(
        client_id=config['reddit']['client_id'], 
        client_secret=config['reddit']['client_secret'], 
        user_agent=config['reddit']['user_agent'], 
        username=config['reddit']['username'], 
        password=config['reddit']['password']
    )

    print(f"Authenticated as: {reddit.user.me()}")  # Print the authenticated user
    return reddit

if __name__ == "__main__":
    authenticate()
