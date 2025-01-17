### Synkrit AI Assignment

This repository contains a modular bot that integrates with Reddit and Groq AI APIs to automate content generation and posting, as well as commenting on trending posts. The project is organized into distinct components for clarity and maintainability.

## Project Structure
Synkrit AI_Assignment/
|
|-- bot/
|   |-- init.py
|   |-- auth.py                   
|   |-- automated_posting.py      
|   |-- comment_on_trending.py    
|   |-- groq_integration.py       
|   |-- reddit_bot.py             
|   |-- scheduler.py              
|
|-- config.json                   
|-- README.md                     
|-- requirements.txt              
|-- sample_output/                
|   |-- sample_post               


## Features
1. Automated Posting

Generates content using the Groq AI API.
Posts the generated content to a specified subreddit at a user-defined time.

2. Commenting on Trending Posts

Fetches top trending posts from a subreddit.
Comments on the posts with a customizable message.

3. Scheduler Integration

Uses the schedule library to run the bot scripts at specified intervals or times.

## Setup Instructions
Prerequisites

1.Install Python (>=3.8).
2.Set up a Reddit app via the Reddit App Console.
3.Obtain access to the Groq AI API.

Installation

1.Clone the repository:

git clone https://github.com/your-repo/synkrit-ai-assignment.git
cd Synkrit_AI_Assignment

2.Install dependencies:

pip install -r requirements.txt

3.Set up config.json:
Create a config.json file in the root directory and add your Reddit and Groq API credentials:

{
    "reddit": {
        "client_id": "your-client-id",
        "client_secret": "your-client-secret",
        "username": "your-reddit-username",
        "password": "your-reddit-password",
        "user_agent": "your-user-agent"
    },
    "groq": {
        "api_key": "your-groq-api-key"
    }
}

4.Verify the configuration:
Run the following to ensure all dependencies are correctly set up:
python -m bot.auth

## Usage

1. Automated Posting

Run the automated_posting.py script to schedule and post content:

python bot/automated_posting.py
You will be prompted to specify a time (in HH:MM format). The bot will generate and post content at the scheduled time.

2. Commenting on Trending Posts

Run the comment_on_trending.py script to comment on trending posts:

python bot/comment_on_trending.py
Customize the target subreddit and comment message within the script.

3. Integrating Scheduler

Run the scheduler.py script to automate both posting and commenting tasks:

python bot/scheduler.py
This script uses the schedule library to execute tasks based on the defined intervals.