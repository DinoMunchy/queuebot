# Discord Queue Bot

A Discord bot that helps manage a single queue for players to join and leave, maintaining fair rotation.

## Features

- Join the queue
- Leave the queue
- View current queue status
- Get next player in queue
- Clear queue
- Players can only add/remove themselves
- No ability to remove others from queue

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with your Discord bot token:
```
DISCORD_TOKEN=your_bot_token_here
```

3. Run the bot:
```bash
python bot.py
```

## Commands

- `!join` - Join the queue
- `!leave` - Leave the queue
- `!queue` - Display the current queue
- `!next` - Get the next player from the queue
- `!clear` - Clear the queue

## Example Usage

```
!join
!queue
!next
!leave
```

## Getting a Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section and create a bot
4. Copy the bot token and paste it in your `.env` file
5. Invite the bot to your server using the OAuth2 URL generator in the Developer Portal # queuebot
