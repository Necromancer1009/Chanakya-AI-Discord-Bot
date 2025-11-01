# Detailed Setup Guide

## 📖 Table of Contents
- [System Requirements](#system-requirements)
- [Step-by-Step Installation](#step-by-step-installation)
- [Discord Bot Setup](#discord-bot-setup)
- [Hugging Face Setup](#hugging-face-setup)
- [Ollama Configuration](#ollama-configuration)
- [Running the Bot](#running-the-bot)

---

## System Requirements

### Minimum Requirements (Chat Only)
- **OS**: Windows 10/11, Linux, macOS
- **Python**: 3.8 or higher
- **RAM**: 8GB minimum
- **Storage**: 10GB free space

### Recommended Requirements (Chat + Image Generation)
- **OS**: Windows 10/11, Linux (Ubuntu 20.04+)
- **Python**: 3.10+
- **GPU**: NVIDIA GPU with 6GB+ VRAM (GTX 1060 or better)
- **CUDA**: 11.7 or higher
- **RAM**: 16GB minimum
- **Storage**: 20GB+ free space

---

## Step-by-Step Installation

### 1. Install Python
Download Python from [python.org](https://www.python.org/downloads/)

Verify installation:
```bash
python --version
```

### 2. Install CUDA Toolkit (For Image Generation)

**Windows:**
1. Download [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
2. Install with default options
3. Verify installation:
```bash
nvcc --version
```

**Linux:**
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update
sudo apt-get -y install cuda
```

### 3. Clone Repository
```bash
git clone https://github.com/Necromancer1009/chanakya-ai-discord-bot.git
cd chanakya-ai-discord-bot
```

### 4. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Install PyTorch with CUDA
Visit [PyTorch Get Started](https://pytorch.org/get-started/locally/) and select your configuration.

**Example for CUDA 11.8:**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## Discord Bot Setup

### 1. Create Discord Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Name your application (e.g., "Chanakya AI Bot")
4. Click "Create"

### 2. Create Bot User
1. Navigate to "Bot" section
2. Click "Add Bot"
3. Customize username and avatar
4. Enable these **Privileged Gateway Intents**:
   - ✅ Presence Intent
   - ✅ Server Members Intent
   - ✅ Message Content Intent

### 3. Get Bot Token
1. Click "Reset Token"
2. Copy the token (save it securely!)
3. **NEVER share this token publicly**

### 4. Invite Bot to Server
1. Go to "OAuth2" → "URL Generator"
2. Select scopes:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Select bot permissions:
   - ✅ Send Messages
   - ✅ Attach Files
   - ✅ Read Message History
   - ✅ Use Slash Commands
4. Copy generated URL and open in browser
5. Select your server and authorize

---

## Hugging Face Setup

### 1. Create Account
1. Go to [Hugging Face](https://huggingface.co/)
2. Sign up for free account

### 2. Generate Access Token
1. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Name: "Discord Bot"
4. Role: "Read"
5. Click "Generate"
6. Copy the token (starts with `hf_`)

### 3. Accept Model Licenses
1. Visit [Stable Diffusion v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
2. Click "Agree and access repository"

---

## Ollama Configuration

### 1. Install Ollama

**Windows:**
Download installer from [ollama.ai](https://ollama.ai/download/windows)

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**macOS:**
```bash
brew install ollama
```

### 2. Pull LLaMA Model
```bash
ollama pull llama3.1
```

This downloads ~4.7GB model. Wait for completion.

### 3. Verify Installation
```bash
ollama list
```

You should see `llama3.1` in the list.

---

## Running the Bot

### 1. Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` with your tokens:
```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
HF_TOKEN=YOUR_HUGGINGFACE_TOKEN_HERE
```

### 2. Run Chat-Only Bot
```bash
python src/chat_bot.py
```

### 3. Run Full Bot (Chat + Image)
```bash
python src/main_bot.py
```

### 4. Verify Bot is Online
- Check Discord - bot should show as online
- Console should show: `✅ Logged on as YourBotName!`

---

## Testing Commands

### In Discord:
```
/chat Hello! Can you introduce yourself?
/image A beautiful sunset over mountains
```

---

## Troubleshooting

### Bot Not Responding
- Check bot is online in Discord
- Verify slash commands are synced (wait up to 1 hour)
- Check bot has proper permissions

### CUDA Errors
```bash
# Check CUDA is available
python -c "import torch; print(torch.cuda.is_available())"
```

### Import Errors
```bash
# Reinstall requirements
pip install --force-reinstall -r requirements.txt
```

### Model Download Failures
- Check internet connection
- Verify Hugging Face token is valid
- Try manual download:
```bash
huggingface-cli login
huggingface-cli download runwayml/stable-diffusion-v1-5
```

---

## Performance Tuning

### Reduce Memory Usage
In `main_bot.py`, modify:
```python
# Lower precision
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

# CPU mode (slower but no GPU needed)
pipe = pipe.to("cpu")
```

### Faster Responses
- Use smaller model: `ollama pull llama3:8b-instruct-q4_0`
- Pre-warm models on startup
- Implement caching

---

## Next Steps

- [Commands Documentation](COMMANDS.md)
- [Troubleshooting Guide](TROUBLESHOOTING.md)
- [Contributing Guide](../README.md#contributing)

---

Need help? Open an issue on [GitHub](https://github.com/Necromancer1009/nexus-ai-bot/issues)!
