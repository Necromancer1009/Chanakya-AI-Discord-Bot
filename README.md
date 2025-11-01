# 🤖 Chanakya AI Discord Bot

<div align="center">

![Discord Bot](https://img.shields.io/badge/Discord-Bot-7289DA?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI Powered](https://img.shields.io/badge/AI-Powered-FF6B6B?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A powerful Discord bot that brings AI image generation and conversational AI directly to your server!**

[Features](#-features) • [Installation](#-installation) • [Commands](#-commands) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

### 🎨 AI Image Generation
- **Stable Diffusion Integration**: Generate stunning images from text prompts
- **High-Quality Output**: Powered by `runwayml/stable-diffusion-v1-5`
- **GPU Accelerated**: Optimized for CUDA-enabled devices

### 💬 Conversational AI
- **LLaMA 3.1 Integration**: Engage in natural conversations with cutting-edge AI
- **Context-Aware Responses**: Smart message chunking for long responses
- **User-Friendly**: Mentions users in responses for better engagement

### ⚡ Modern Discord Integration
- **Slash Commands**: Easy-to-use modern Discord interface
- **Async Operations**: Non-blocking operations for smooth performance
- **Deferred Responses**: Handles long-running AI tasks gracefully

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **CUDA-capable GPU** (for Stable Diffusion - optional for chat-only mode)
- **Ollama** (for LLaMA models)
- **Discord Bot Token** (from [Discord Developer Portal](https://discord.com/developers/applications))
- **Hugging Face Token** (from [Hugging Face](https://huggingface.co/settings/tokens))

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Necromancer1009/chanakya-ai-discord-bot.git
cd chanakya-ai-discord-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download and install [Ollama](https://ollama.ai/) for your operating system.

Pull the LLaMA model:
```bash
ollama pull llama3.1
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
DISCORD_TOKEN=your_discord_bot_token_here
HF_TOKEN=your_huggingface_token_here
GUILD_ID=your_guild_id_here  # Optional
```

### 5. Run the Bot

```bash
python src/main_bot.py
```

---

## 🎮 Commands

### `/chat <prompt>`
Engage in conversation with LLaMA 3.1 AI

**Example:**
```
/chat What is quantum computing?
/chat Write me a poem about space
/chat Explain machine learning in simple terms
```

### `/image <prompt>` *(Stable Diffusion Mode)*
Generate AI-powered images from text descriptions

**Example:**
```
/image A majestic dragon flying over a medieval castle at sunset
/image Cyberpunk city with neon lights
/image A serene Japanese garden with cherry blossoms
```

---

## 📁 Project Structure

```
chanakya-ai-discord-bot/
├── src/
│   ├── main_bot.py              # Latest production-ready bot (chat + image)
│   ├── chat_bot.py              # Chat-only version
│   └── utils.py                 # Helper functions
├── legacy/
│   ├── bot.py                   # Original versions
│   ├── bot_2.py                 # Version 2
│   ├── bot_3.py                 # Version 3
│   └── ...                      # Other legacy versions
├── notebooks/
│   ├── bot.ipynb                # Initial experiments
│   ├── llama_3.ipynb            # LLaMA testing
│   ├── stable_diff.ipynb        # Stable Diffusion experiments
│   └── code.ipynb               # Model comparisons
├── docs/
│   ├── SETUP.md                 # Detailed setup guide
│   ├── COMMANDS.md              # Command documentation
│   └── TROUBLESHOOTING.md       # Common issues and fixes
├── .env.example                 # Example environment file
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## 🛠️ Technical Details

### Technologies Used

- **Discord.py**: Discord API wrapper for Python
- **Transformers**: Hugging Face's transformer models
- **Diffusers**: Stable Diffusion pipeline
- **PyTorch**: Deep learning framework
- **Ollama**: Local LLM runtime
- **aiofiles**: Async file operations

### Models

- **Chat**: `llama3.1` via Ollama
- **Image Generation**: `runwayml/stable-diffusion-v1-5`

### Performance Optimizations

- ✅ CUDA GPU acceleration
- ✅ FP16 precision for faster inference
- ✅ Message chunking for long responses
- ✅ VRAM cleanup after image generation
- ✅ Async operations throughout

---

## 🔧 Configuration

### Chat-Only Mode
If you don't have a CUDA GPU or want to run chat-only:

```bash
python src/chat_bot.py
```

### Custom Cache Directories
Modify cache paths in the bot files:

```python
os.environ['HF_HOME'] = "your/custom/path"
os.environ['TRANSFORMERS_CACHE'] = "your/custom/path/models"
```

---

## 📝 Development History

This bot evolved through multiple iterations:

1. **v1.0**: Basic message-based image generation
2. **v2.0**: Added chat functionality with GPT-J
3. **v3.0**: Migrated to Ollama and LLaMA 3
4. **v4.0**: Implemented slash commands
5. **v5.0**: Advanced message chunking and error handling
6. **Current**: Production-ready with optimized performance

All legacy versions are preserved in the `legacy/` directory for reference.

---

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔨 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 🐛 Known Issues & Solutions

### Out of Memory Errors
- Reduce batch size in Stable Diffusion
- Use `torch.cuda.empty_cache()` after generation
- Consider using CPU for image generation

### Slow Response Times
- Pre-load models on bot startup
- Use smaller model variants
- Implement response caching

See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for more details.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Necromancer1009**
- GitHub: [@Necromancer1009](https://github.com/Necromancer1009)
- Discord: Add your Discord handle here

---

## 🙏 Acknowledgments

- [Discord.py](https://github.com/Rapptz/discord.py) - Amazing Discord API wrapper
- [Hugging Face](https://huggingface.co/) - AI model hosting and tools
- [Ollama](https://ollama.ai/) - Local LLM runtime
- [Stability AI](https://stability.ai/) - Stable Diffusion models

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

---

<div align="center">

**Made with ❤️ and AI**

[Report Bug](https://github.com/Necromancer1009/chanakya-ai-discord-bot/issues) • [Request Feature](https://github.com/Necromancer1009/chanakya-ai-discord-bot/issues)

</div>
