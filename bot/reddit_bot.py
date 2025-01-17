from bot.auth import authenticate
from bot.groq_integration import generate_content

def main():
    
    reddit = authenticate()

    
    print(f"Authenticated as: {reddit.user.me()}")

    subreddit = reddit.subreddit('test')
    subreddit.submit('Hello from Reddit Bot!', selftext='This is a test post.')

if __name__ == "__main__":
    main()

content = generate_content()
if content:
    print("Generated Content:", content)
