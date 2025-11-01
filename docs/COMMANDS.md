# Commands Documentation

Complete guide to all Chanakya AI Discord Bot commands and features.

---

## 📝 Command List

### `/chat` - AI Conversation
Engage in natural conversation with LLaMA 3.1

**Syntax:**
```
/chat <prompt>
```

**Parameters:**
- `prompt` (required): Your message or question to the AI

**Examples:**
```
/chat What is the meaning of life?
/chat Explain quantum physics in simple terms
/chat Write a short story about a robot
/chat What are the best practices for Python programming?
/chat Translate "Hello World" to Spanish
```

**Features:**
- ✅ Natural language understanding
- ✅ Context-aware responses
- ✅ Code generation and explanation
- ✅ Multi-lingual support
- ✅ Long-form responses (auto-chunked)

**Response Time:** 5-30 seconds depending on prompt complexity

**Limitations:**
- Max prompt length: 2000 characters (Discord limit)
- Responses chunked at 1900 characters
- No conversation history (stateless)

---

### `/image` - AI Image Generation
Generate stunning images from text descriptions using Stable Diffusion

**Syntax:**
```
/image <prompt>
```

**Parameters:**
- `prompt` (required): Description of the image you want to create

**Examples:**
```
/image A majestic dragon flying over a medieval castle at sunset
/image Cyberpunk city street with neon signs, rainy night, detailed
/image Portrait of a wise old wizard with a long white beard
/image Futuristic spaceship interior, sci-fi, high detail
/image Serene Japanese garden with cherry blossoms and koi pond
```

**Pro Tips for Better Images:**
- 🎨 Be specific and descriptive
- 🌟 Add style keywords: "realistic", "anime", "oil painting", "photorealistic"
- 💡 Include lighting: "golden hour", "dramatic lighting", "soft light"
- 🎭 Add quality modifiers: "highly detailed", "4k", "masterpiece"
- 📸 Specify view: "close-up", "wide angle", "aerial view"

**Example of a Great Prompt:**
```
/image A hyperrealistic portrait of a cyberpunk hacker, neon blue hair, 
augmented reality glasses, dark futuristic clothing, city lights background, 
cinematic lighting, 8k, highly detailed
```

**Response Time:** 10-60 seconds depending on GPU

**Output Format:**
- Format: PNG
- Resolution: 512x512 (default)
- File size: ~500KB - 2MB

**Limitations:**
- Requires CUDA GPU (6GB+ VRAM recommended)
- One image per request
- Max prompt length: 2000 characters

---

## 🎯 Usage Patterns

### Research & Learning
```
/chat Explain machine learning algorithms for beginners
/chat What are the key differences between React and Vue?
/chat Summarize the history of the Roman Empire
```

### Creative Writing
```
/chat Write a haiku about autumn
/chat Create a character description for a fantasy novel
/chat Generate ideas for a sci-fi short story
```

### Programming Help
```
/chat How do I implement a binary search in Python?
/chat Explain async/await in JavaScript
/chat Debug this code: [paste code]
/chat Best practices for SQL optimization
```

### Image Creation Scenarios

**Fantasy Art:**
```
/image Ancient elven city in a giant tree, magical atmosphere, 
glowing crystals, fantasy art, detailed architecture
```

**Character Design:**
```
/image Concept art of a female knight in ornate armor, 
confident pose, castle courtyard, Renaissance style
```

**Landscapes:**
```
/image Alien planet landscape, purple sky, twin moons, 
exotic flora, dramatic mountains, sci-fi concept art
```

**Abstract/Artistic:**
```
/image Abstract representation of music, flowing colors, 
dynamic composition, digital art, vibrant
```

---

## ⚙️ Advanced Features

### Auto-Message Chunking
Responses longer than 2000 characters are automatically split:
- First chunk mentions the user
- Subsequent chunks sent as follow-up messages
- Code blocks are preserved across chunks

### Error Handling
Bot gracefully handles:
- Network timeouts
- Model loading errors
- Invalid prompts
- Permission issues

Example error message:
```
❌ An error occurred: CUDA out of memory
```

---

## 🚫 Content Filtering

The bot includes basic content safety:
- Offensive content may be rejected by AI models
- NSFW content is not explicitly supported
- Respect Discord's Terms of Service

---

## 💡 Best Practices

### For Chat:
1. **Be Clear**: Specific questions get better answers
2. **Break Down Complex Requests**: Ask in steps
3. **Provide Context**: Give background information when needed
4. **Iterate**: Refine your prompts based on responses

### For Images:
1. **Describe Details**: More details = better results
2. **Use Art Styles**: "photorealistic", "anime", "watercolor"
3. **Specify Mood**: "dark", "cheerful", "mysterious"
4. **Add Technical Terms**: "depth of field", "volumetric lighting"
5. **Experiment**: Try different phrasings

---

## 🔧 Technical Details

### Rate Limits
- No built-in rate limiting
- Respect Discord's API limits (varies by server)
- Consider adding cooldowns for production use

### Resource Usage
- **Chat**: ~2-4GB RAM, <1GB VRAM (CPU fallback available)
- **Image**: ~6-8GB VRAM, ~4GB RAM
- **Response Caching**: Not implemented (all requests are fresh)

### Model Specifications

**Chat (LLaMA 3.1):**
- Parameters: 8B
- Context Length: 8192 tokens
- Quantization: Default Ollama quantization
- Speed: ~20-50 tokens/second

**Image (Stable Diffusion v1.5):**
- Parameters: 860M
- Training: 512x512 images
- Steps: 50 (default)
- Scheduler: PNDM

---

## 📊 Example Workflows

### Creating a Character Design
```
1. /chat Create a detailed character description for a fantasy warrior
2. (Review the description)
3. /image [Use the description from step 1]
4. (Iterate with refined prompts if needed)
```

### Learning a New Topic
```
1. /chat What is Docker and how does it work?
2. /chat Give me an example Docker configuration
3. /chat Explain the difference between Docker and VMs
```

---

## 🆘 Common Issues

**Problem:** Command not showing up
**Solution:** Wait up to 1 hour for Discord to sync commands globally

**Problem:** "An error occurred" message
**Solution:** Check bot logs, verify API tokens, ensure models are loaded

**Problem:** Slow image generation
**Solution:** Use smaller model variant or upgrade GPU

**Problem:** Chat responses cut off
**Solution:** Responses >2000 chars are auto-chunked, check follow-up messages

---

## 🔮 Upcoming Features

Planned additions:
- [ ] Conversation history/context
- [ ] Custom image parameters (size, steps, guidance)
- [ ] Voice command support
- [ ] Multi-image generation
- [ ] Image-to-image transformation
- [ ] Custom model selection

---

## 💬 Feedback

Found a bug or have a suggestion? [Open an issue](https://github.com/Necromancer1009/nexus-ai-bot/issues)!

---

[Back to README](../README.md) | [Setup Guide](SETUP.md) | [Troubleshooting](TROUBLESHOOTING.md)
