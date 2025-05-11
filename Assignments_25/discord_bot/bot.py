import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv  

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command(name="hello", help="Replies with a greeting")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}! 👋")

@bot.command(name="add", help="Adds two numbers: !add 2 3")
async def add(ctx, a: float, b: float):
    result = a + b
    await ctx.send(f"{a} + {b} = {result}")

@bot.command(name="8ball", help="Magic 8-ball answers your yes/no question")
async def eight_ball(ctx, *, question: str):
    responses = [
        "It is certain.", "Without a doubt.", "You may rely on it.",
        "Ask again later.", "Cannot predict now.", "Don't count on it.",
        "My reply is no.", "Very doubtful."
    ]
    answer = random.choice(responses)
    await ctx.send(f"🎱 {answer}")

# ✅ Run the bot
bot.run(TOKEN)
