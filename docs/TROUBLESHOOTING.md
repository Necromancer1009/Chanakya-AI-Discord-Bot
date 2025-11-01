# Troubleshooting Guide

Common issues and solutions for Chanakya AI Discord Bot

---

## 🔍 Quick Diagnostics

Run these checks first:

```bash
# Check Python version
python --version  # Should be 3.8+

# Check CUDA availability
python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}')"

# Check installed packages
pip list | grep -E "discord|torch|diffusers|ollama"

# Test Ollama
ollama list
```

---

## 🚨 Common Errors

### 1. Bot Won't Start

#### Error: `DISCORD_TOKEN not found`
**Cause:** Missing or incorrect .env file

**Solution:**
```bash
# Create .env file
cp .env.example .env

# Edit with your token
# DISCORD_TOKEN=your_actual_token_here
```

**Verify:**
```bash
# Windows PowerShell
Get-Content .env

# Linux/macOS
cat .env
```

---

#### Error: `ModuleNotFoundError: No module named 'discord'`
**Cause:** Dependencies not installed

**Solution:**
```bash
pip install -r requirements.txt

# If that fails, install individually
pip install discord.py
pip install torch
pip install diffusers
```

---

### 2. CUDA / GPU Issues

#### Error: `CUDA out of memory`
**Cause:** GPU VRAM exhausted

**Solutions:**

**Option 1: Clear cache in code**
Add to `main_bot.py`:
```python
torch.cuda.empty_cache()
gc.collect()  # import gc at top
```

**Option 2: Reduce model precision**
```python
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float32  # Change from float16
)
```

**Option 3: Use CPU (slower)**
```python
pipe = pipe.to("cpu")  # Instead of "cuda"
```

**Option 4: Close other GPU applications**
- Close games, video editors, other ML applications
- Check GPU usage: `nvidia-smi`

---

#### Error: `RuntimeError: CUDA error: no kernel image available`
**Cause:** PyTorch CUDA version mismatch

**Solution:**
```bash
# Check CUDA version
nvcc --version

# Reinstall PyTorch for your CUDA version
# Example for CUDA 11.8
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

#### Error: `torch.cuda.is_available()` returns False
**Cause:** CUDA not properly installed or detected

**Diagnosis:**
```bash
# Check NVIDIA driver
nvidia-smi

# Check CUDA installation
nvcc --version

# Check PyTorch CUDA build
python -c "import torch; print(torch.version.cuda)"
```

**Solutions:**
1. **Update NVIDIA drivers**: [Download here](https://www.nvidia.com/download/index.aspx)
2. **Reinstall CUDA Toolkit**: [Download here](https://developer.nvidia.com/cuda-downloads)
3. **Reinstall PyTorch with CUDA**: See command above

---

### 3. Discord Bot Issues

#### Error: Commands not appearing
**Cause:** Commands not synced or permissions issue

**Solutions:**

**Wait for global sync (up to 1 hour):**
Discord can take time to propagate commands globally.

**Use guild-specific sync (instant):**
```python
# In main_bot.py, modify on_ready:
@bot.event
async def on_ready():
    guild = discord.Object(id=YOUR_GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
```

**Clear and re-sync:**
```python
@bot.event
async def on_ready():
    # Clear all commands
    bot.tree.clear_commands(guild=None)
    await bot.tree.sync()
```

---

#### Error: `403 Forbidden` or `Missing Permissions`
**Cause:** Bot lacks necessary permissions

**Solution:**
1. Go to Discord Developer Portal
2. OAuth2 → URL Generator
3. Select:
   - ✅ `bot`
   - ✅ `applications.commands`
4. Bot Permissions:
   - ✅ Send Messages
   - ✅ Attach Files
   - ✅ Use Slash Commands
5. Re-invite bot using new URL

---

#### Error: Bot online but not responding
**Diagnosis:**
```python
# Add debug logging to on_message
@bot.event
async def on_message(message):
    print(f"Message received: {message.content}")
    await bot.process_commands(message)
```

**Common Causes:**
- Intents not enabled (check code: `intents.message_content = True`)
- Bot account instead of user (correct)
- Command name typo
- Bot blocked or banned in channel

---

### 4. Model Loading Issues

#### Error: `OSError: Can't load tokenizer`
**Cause:** Hugging Face authentication failed

**Solution:**
```bash
# Login via CLI
huggingface-cli login

# Or set token in .env
HF_TOKEN=hf_your_token_here
```

---

#### Error: `HTTPError: 401 Unauthorized`
**Cause:** Invalid Hugging Face token or model access denied

**Solutions:**
1. **Verify token**: Check [HF Settings](https://huggingface.co/settings/tokens)
2. **Accept model license**: Visit model page and accept terms
3. **Regenerate token**: Create new token with READ access

---

#### Error: Download speed very slow / stuck
**Cause:** Large model download

**Solutions:**
```bash
# Pre-download models
huggingface-cli download runwayml/stable-diffusion-v1-5

# Or use Ollama CLI
ollama pull llama3.1

# Set custom cache location
export HF_HOME=/path/to/large/drive
```

---

### 5. Ollama Issues

#### Error: `Connection refused` to Ollama
**Cause:** Ollama service not running

**Solution:**

**Windows:**
- Start Ollama from Start Menu
- Or run: `ollama serve`

**Linux:**
```bash
sudo systemctl start ollama
sudo systemctl enable ollama  # Auto-start on boot
```

**macOS:**
```bash
brew services start ollama
```

---

#### Error: Model not found
**Cause:** Model not pulled

**Solution:**
```bash
# List available models
ollama list

# Pull required model
ollama pull llama3.1

# Verify
ollama list | grep llama3.1
```

---

### 6. Runtime Errors

#### Error: `Message too long` (>2000 characters)
**Cause:** Discord message limit exceeded

**Solution:**
The bot should auto-chunk messages. If not, update chat command:

```python
# Implement chunking (already in provided code)
max_chars = 1900
# ... chunking logic
```

---

#### Error: `asyncio` or `coroutine` errors
**Cause:** Blocking operations in async context

**Solution:**
```python
# Use aiofiles for file operations
import aiofiles

async with aiofiles.open('file.txt', 'r') as f:
    content = await f.read()

# Or run blocking code in executor
import asyncio
result = await asyncio.to_thread(blocking_function, args)
```

---

### 7. Performance Issues

#### Problem: Slow response times

**Solutions:**

**For Chat:**
```bash
# Use smaller/faster model
ollama pull llama3:8b-instruct-q4_0

# Increase Ollama threads (in code)
ollama.chat(model='llama3.1', options={'num_thread': 8}, messages=...)
```

**For Image Generation:**
```python
# Reduce inference steps (faster but lower quality)
pipe(prompt, num_inference_steps=25)  # Default is 50

# Use smaller model
model_id = "CompVis/stable-diffusion-v1-4"  # Slightly smaller
```

---

#### Problem: High memory usage

**Solutions:**
```python
# Enable attention slicing
pipe.enable_attention_slicing()

# Enable CPU offloading
pipe.enable_sequential_cpu_offload()

# Use float32 instead of float16 (paradoxically uses less VRAM)
torch_dtype=torch.float32
```

---

## 🔧 Advanced Troubleshooting

### Enable Debug Logging

Add to bot file:
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
```

### Check System Resources

**Windows:**
```powershell
# GPU usage
nvidia-smi

# RAM usage
Get-Process | Sort-Object -Property WS -Descending | Select-Object -First 10
```

**Linux:**
```bash
# GPU
watch -n 1 nvidia-smi

# RAM
htop

# Disk space
df -h
```

### Test Models Independently

**Test Ollama:**
```bash
ollama run llama3.1 "Hello, test message"
```

**Test Stable Diffusion:**
```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda")
image = pipe("test prompt").images[0]
image.save("test.png")
```

---

## 📋 Checklist for Clean Reinstall

If all else fails:

```bash
# 1. Remove virtual environment
rm -rf venv/  # Linux/macOS
rmdir /s venv  # Windows

# 2. Clear Python cache
find . -type d -name __pycache__ -exec rm -rf {} +  # Linux/macOS
# Windows: manually delete __pycache__ folders

# 3. Recreate environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 4. Reinstall everything
pip install --upgrade pip
pip install -r requirements.txt

# 5. Re-pull models
ollama pull llama3.1

# 6. Verify .env file
cat .env  # Check tokens are correct

# 7. Run bot
python src/main_bot.py
```

---

## 🆘 Still Having Issues?

1. **Check the logs**: Look at console output when error occurs
2. **Search existing issues**: [GitHub Issues](https://github.com/Necromancer1009/nexus-ai-bot/issues)
3. **Create new issue**: Include:
   - Error message (full traceback)
   - Python version
   - OS and GPU info
   - Steps to reproduce

---

## 📚 Additional Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [PyTorch CUDA Setup](https://pytorch.org/get-started/locally/)
- [Hugging Face Hub](https://huggingface.co/docs/huggingface_hub/)
- [Ollama Documentation](https://github.com/ollama/ollama)

---

[Back to README](../README.md) | [Setup Guide](SETUP.md) | [Commands](COMMANDS.md)
