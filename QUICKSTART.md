# 🚀 Quick Start Guide

Get your Nexus AI Bot running in 5 minutes!

## ⚡ Express Setup (Chat Only)

Perfect if you just want to try the bot without GPU requirements.

### 1. Prerequisites
```powershell
# Check Python version (need 3.8+)
python --version
```

### 2. Install Ollama
Download from [ollama.ai](https://ollama.ai/download/windows)

```powershell
# After installation, pull the model
ollama pull llama3.1
```

### 3. Clone & Setup
```powershell
git clone https://github.com/Necromancer1009/chanakya-ai-discord-bot.git
cd chanakya-ai-discord-bot

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install discord.py ollama python-dotenv
```

### 4. Configure
```powershell
# Copy environment template
copy .env.example .env

# Edit .env and add your Discord token
# DISCORD_TOKEN=your_token_here
```

### 5. Run!
```powershell
python src/chat_bot.py
```

✅ **Done!** Your bot should be online. Try `/chat Hello!` in Discord.

---

## 🎨 Full Setup (Chat + Images)

For complete functionality with image generation.

### Additional Requirements
- NVIDIA GPU with 6GB+ VRAM
- CUDA Toolkit 11.7+

### Installation
```powershell
# Follow steps 1-4 above, then:

# Install PyTorch with CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# Install full requirements
pip install -r requirements.txt

# Get Hugging Face token from https://huggingface.co/settings/tokens
# Add to .env: HF_TOKEN=your_hf_token_here

# Run full bot
python src/main_bot.py
```

---

## 🎮 Test Commands

Once your bot is running:

```
/chat Tell me a joke
/chat What is Python?
/image A beautiful sunset over mountains
```

---

## ❌ Troubleshooting Quick Fixes

### Bot not responding?
```powershell
# Check bot is running in terminal
# Verify bot has permissions in Discord server
# Wait up to 1 hour for slash commands to sync
```

### Import errors?
```powershell
pip install --force-reinstall -r requirements.txt
```

### CUDA errors?
```python
# Edit src/main_bot.py line 27:
# Change: pipe = pipe.to("cuda")
# To:     pipe = pipe.to("cpu")
```

---

## 📚 Next Steps

1. Read [SETUP.md](docs/SETUP.md) for detailed configuration
2. Check [COMMANDS.md](docs/COMMANDS.md) for all features
3. See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) if issues arise

---

## 🆘 Still Stuck?

- Check if bot is online in Discord
- Review terminal output for errors
- Open an issue on GitHub

**Happy botting!** 🤖✨
