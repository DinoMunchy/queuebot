import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Single queue for all players
queue = []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='join')
async def join_queue(ctx):
    """Add yourself to the queue"""
    if ctx.author in queue:
        await ctx.send(f"{ctx.author.mention} You are already in the queue!")
        return
    
    queue.append(ctx.author)
    await ctx.send(f"{ctx.author.mention} has joined the queue!")
    await display_queue(ctx)

@bot.command(name='leave')
async def leave_queue(ctx):
    """Remove yourself from the queue"""
    if ctx.author not in queue:
        await ctx.send(f"{ctx.author.mention} You are not in the queue!")
        return
    
    queue.remove(ctx.author)
    await ctx.send(f"{ctx.author.mention} has left the queue!")
    await display_queue(ctx)

@bot.command(name='queue')
async def display_queue(ctx):
    """Display the current queue"""
    if not queue:
        await ctx.send("No one is currently in the queue!")
        return
    
    queue_list = "\n".join([f"{i+1}. {member.mention}" for i, member in enumerate(queue)])
    embed = discord.Embed(
        title="Current Queue",
        description=queue_list,
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command(name='next')
async def next_player(ctx):
    """Get the next player from the queue"""
    if not queue:
        await ctx.send("No one is currently in the queue!")
        return
    
    next_player = queue.pop(0)
    await ctx.send(f"Next player up: {next_player.mention}")
    await display_queue(ctx)

@bot.command(name='clear')
async def clear_queue(ctx):
    """Clear the queue"""
    if not queue:
        await ctx.send("The queue is already empty!")
        return
    
    queue.clear()
    await ctx.send("The queue has been cleared!")

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 