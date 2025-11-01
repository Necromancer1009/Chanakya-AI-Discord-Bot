# Project Organization

This document describes the organization and purpose of each directory and file in the Nexus AI Bot project.

## 📁 Directory Structure

```
nexus-ai-bot/
├── 📂 src/                      # Source code (production-ready)
│   ├── main_bot.py              # Full bot (chat + image generation)
│   ├── chat_bot.py              # Lightweight chat-only version
│   └── utils.py                 # Utility functions (future)
│
├── 📂 legacy/                   # Historical bot versions
│   ├── bot.py                   # v1.0 - Basic image generation
│   ├── bot_2.py                 # v2.0 - Added chat with GPT-J
│   ├── bot_3.py                 # v3.0 - Ollama integration
│   ├── bot_4.py                 # v4.0 - Slash commands
│   ├── bot_with_option_2.py     # v4.1 - Slash commands refinement
│   └── bot_with_options_*.py    # v4.x - Various iterations
│
├── 📂 notebooks/                # Jupyter notebooks for experiments
│   ├── bot.ipynb                # Initial Discord bot testing
│   ├── code.ipynb               # Model comparisons (GPT-J, LLaMA)
│   ├── llama_3.ipynb            # LLaMA 3 integration testing
│   ├── stable_diff.ipynb        # Stable Diffusion experiments
│   ├── stable_diff_high.ipynb   # High-res SD testing
│   └── test.ipynb               # General testing notebook
│
├── 📂 docs/                     # Documentation
│   ├── SETUP.md                 # Detailed setup instructions
│   ├── COMMANDS.md              # Command reference guide
│   ├── TROUBLESHOOTING.md       # Common issues and solutions
│   └── ORGANIZATION.md          # This file
│
├── 📂 .github/                  # GitHub-specific files
│   └── workflows/               # CI/CD (future)
│
├── 📄 README.md                 # Main project documentation
├── 📄 LICENSE                   # MIT License
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env.example              # Environment variable template
├── 📄 .gitignore                # Git ignore rules
└── 📄 organize.ps1              # Organization helper script
```

## 📝 File Descriptions

### Source Code (`src/`)

#### `main_bot.py`
**Purpose:** Production-ready bot with full features
**Features:**
- LLaMA 3.1 chat via Ollama
- Stable Diffusion image generation
- Slash command interface
- Message chunking for long responses
- Error handling and logging

**Use Case:** Deploy this for full bot functionality with GPU support

#### `chat_bot.py`
**Purpose:** Lightweight chat-only bot
**Features:**
- LLaMA 3.1 chat only
- No GPU requirements
- Lower resource usage
- Slash command interface

**Use Case:** Deploy when you don't have a GPU or only need chat functionality

---

### Legacy Versions (`legacy/`)

#### Evolution Timeline:

**v1.0 - `bot.py`**
- Basic message-based bot
- Stable Diffusion image generation only
- Required @mention to trigger
- No command parsing

**v2.0 - `bot_2.py`**
- Added `/image` and `/chat` commands
- Integrated GPT-J for chat
- Message parsing improvements
- Ollama integration started

**v3.0 - `bot_3.py`**
- Full Ollama LLaMA 3 integration
- Removed GPT-J dependency
- Improved response handling
- Better error management

**v4.0 - `bot_4.py`**
- Migrated to slash commands
- User mentions in responses
- Code cleanup and organization

**v4.x - `bot_with_option_*.py`**
- Various experiments with:
  - Message chunking algorithms
  - File-based chunking vs in-memory
  - Code block preservation
  - Different chat models (llama3 vs llama3.1)

**Stable Diffusion Variants:**
- `bot_with_options_stable_diff.py` - Chat only (SD commented out)
- `bot_with_options_stable_diff_mod.py` - Message chunking v1
- `bot_with_options_stable_diff_mod_2.py` - File-based chunking
- `bot_with_options_stable_diff_mod_3.py` - Improved chunking
- `bot_with_options-stable_diff_clll.py` - Alternative implementation

---

### Notebooks (`notebooks/`)

#### `bot.ipynb`
**Purpose:** Initial Discord bot experimentation
**Contents:**
- Basic Discord client setup
- Message event handlers
- Token testing

#### `code.ipynb`
**Purpose:** Model testing and comparison
**Contents:**
- GPT-Neo 1.3B testing
- LLaMA 2 integration attempts
- Model loading experiments
- Ollama API testing

#### `llama_3.ipynb`
**Purpose:** LLaMA 3/3.1 integration research
**Contents:**
- Various LLaMA model tests
- Hugging Face transformers pipeline
- GPTQ quantized model testing
- Falcon model comparison

#### `stable_diff.ipynb` & `stable_diff_high.ipynb`
**Purpose:** Stable Diffusion experimentation
**Contents:**
- Model loading and optimization
- Different SD versions testing
- VRAM optimization techniques
- Image generation parameters

#### `test.ipynb`
**Purpose:** General testing and debugging
**Contents:** Quick experiments and proof-of-concepts

---

## 🎯 Which File to Use?

### For Production Use:
✅ **`src/main_bot.py`** - Full featured bot (recommended)
✅ **`src/chat_bot.py`** - Chat-only lightweight version

### For Learning/Reference:
📚 **`legacy/`** - See how the bot evolved
📚 **`notebooks/`** - Understand model integration

### For Development:
🔧 **`src/main_bot.py`** - Start here for new features
🔧 **`notebooks/`** - Test new models/features first

---

## 🔄 Version History

| Version | File | Date | Key Changes |
|---------|------|------|-------------|
| 1.0 | `bot.py` | Early 2024 | Initial release - image only |
| 2.0 | `bot_2.py` | Mid 2024 | Added chat with GPT-J |
| 3.0 | `bot_3.py` | Mid 2024 | Switched to Ollama |
| 4.0 | `bot_4.py` | Late 2024 | Slash commands |
| 5.0 | `src/main_bot.py` | Current | Production ready |

---

## 📦 Dependencies by File

### `main_bot.py`:
- discord.py
- diffusers
- torch (CUDA)
- ollama
- huggingface-hub
- PIL

### `chat_bot.py`:
- discord.py
- ollama
- python-dotenv

### Legacy files:
- Various combinations of above
- Some include unused imports (historical)

---

## 🗑️ Cleaned Files

The following temporary files were removed during organization:
- `chunk_1.txt`, `chunk_2.txt`, `chunk_3.txt` - Testing artifacts
- `my.txt` - Temporary response storage

These were used for file-based chunking experiments (v4.x) but are no longer needed.

---

## 🔮 Future Structure

Planned additions:

```
src/
├── commands/           # Command handlers
│   ├── chat.py
│   └── image.py
├── models/            # Model management
│   ├── llama.py
│   └── stable_diffusion.py
├── utils/             # Utilities
│   ├── chunking.py
│   └── logging.py
└── config.py          # Configuration management
```

---

## 🤝 Contributing Guidelines

When adding new features:

1. **Experiment in notebooks first** - Use `notebooks/test.ipynb`
2. **Create a new file** - Don't modify `main_bot.py` directly
3. **Test thoroughly** - Ensure no breaking changes
4. **Update documentation** - Add to relevant docs
5. **Submit PR** - Include description of changes

---

## 📊 Project Statistics

- **Total Bot Versions:** 10+
- **Main Dependencies:** 7 major libraries
- **Lines of Code (main_bot.py):** ~130
- **Documentation Pages:** 4
- **Supported Commands:** 2 (chat, image)

---

## 📞 Support

Questions about organization?
- Open an issue on GitHub
- Check `docs/TROUBLESHOOTING.md`
- Review legacy code for reference

---

**Last Updated:** November 2025
**Maintained by:** Necromancer1009
