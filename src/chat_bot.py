"""
Chanakya AI Discord Bot - Chat Only Version
A lightweight Discord bot with only LLaMA 3.1 chat capabilities.
Perfect for systems without CUDA GPU or for chat-only deployment.

Author: Necromancer1009
License: MIT
"""

import discord
from discord.ext import commands
from discord import app_commands
import os
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Ollama
print("Initializing Ollama and pulling llama3.1...")
ollama.pull('llama3.1')
print("✅ Model loaded successfully!")

# Initialize the bot
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    """Event handler for when bot is ready"""
    print(f'✅ Logged on as {bot.user}!')
    try:
        await bot.tree.sync()
        print("✅ Slash commands synced!")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")


@bot.tree.command(name="chat", description="Chat with LLaMA 3.1 AI")
@app_commands.describe(prompt="Your message to the AI")
async def chat(interaction: discord.Interaction, prompt: str):
    """Chat with LLaMA 3.1 through Ollama"""
    await interaction.response.defer()
    try:
        # Get response from Ollama
        response = ollama.chat(model='llama3.1', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        
        response_content = response['message']['content']
        
        # Handle long responses by chunking
        message_chunks = []
        current_chunk = ""
        max_chars = 1900
        
        for line in response_content.split('\n'):
            if len(current_chunk) + len(line) + 1 > max_chars:
                if current_chunk:
                    message_chunks.append(current_chunk)
                current_chunk = line
            else:
                if current_chunk:
                    current_chunk += "\n" + line
                else:
                    current_chunk = line
        
        # Append the last chunk
        if current_chunk:
            message_chunks.append(current_chunk)
        
        # Send messages
        for i, chunk in enumerate(message_chunks):
            if i == 0:
                await interaction.followup.send(content=f"💬 {interaction.user.mention}\n{chunk}")
            else:
                await bot.get_channel(interaction.channel_id).send(f"{interaction.user.mention}\n{chunk}")
                
    except Exception as e:
        await interaction.followup.send(f"❌ An error occurred: {e}")


@bot.event
async def on_command_error(ctx, error):
    """Global error handler"""
    if isinstance(error, commands.CommandNotFound):
        return
    print(f"Error: {error}")


# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("❌ Error: DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with your Discord bot token.")
    else:
        print("🚀 Starting Chanakya AI Discord Bot (Chat Only)...")
        bot.run(token)
