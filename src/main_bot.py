"""
Chanakya AI Discord Bot - Main Application
A Discord bot with AI chat (LLaMA 3.1) and image generation (Stable Diffusion) capabilities.

Author: Necromancer1009
License: MIT
"""

import discord
from discord.ext import commands
from discord import app_commands
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
from PIL import Image
from huggingface_hub import login
import os
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Ollama
print("Initializing Ollama and pulling llama3.1...")
ollama.pull('llama3.1')

# Login to Hugging Face
print("Logging into Hugging Face...")
login(os.getenv("HF_TOKEN"))

# Load the Stable Diffusion model
print("Loading Stable Diffusion model...")
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
print("Models loaded successfully!")

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


@bot.tree.command(name="image", description="Generate an AI image using Stable Diffusion")
@app_commands.describe(prompt="The description of the image you want to generate")
async def image(interaction: discord.Interaction, prompt: str):
    """Generate an image from text prompt using Stable Diffusion"""
    await interaction.response.defer()
    try:
        # Clear CUDA cache to prevent OOM errors
        torch.cuda.empty_cache()
        
        # Generate image
        response = pipe(prompt).images[0]
        
        # Convert to bytes
        image_buffer = BytesIO()
        response.save(image_buffer, format='PNG')
        image_buffer.seek(0)
        
        # Send image
        await interaction.followup.send(
            content=f"🎨 {interaction.user.mention} Here is your generated image!",
            file=discord.File(fp=image_buffer, filename='generated_image.png')
        )
    except Exception as e:
        await interaction.followup.send(content=f"❌ An error occurred: {e}")


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
                await interaction.followup.send(content=f"{interaction.user.mention}\n{chunk}")
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
        print("🚀 Starting Chanakya AI Discord Bot...")
        bot.run(token)
