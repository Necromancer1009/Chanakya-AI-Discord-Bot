# Contributing to Chanakya AI Discord Bot

Thank you for your interest in contributing to Chanakya AI Discord Bot! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/Necromancer1009/nexus-ai-bot/issues)
2. If not, create a new issue with:
   - Clear descriptive title
   - Detailed description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, GPU)
   - Error logs/screenshots

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its use case
3. Explain why it would be valuable
4. Consider implementation details

### Code Contributions

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m 'Add feature: XYZ'`
6. Push to your fork: `git push origin feature/YourFeature`
7. Open a Pull Request

## 📋 Development Setup

```bash
# Clone your fork
git clone https://github.com/YourUsername/chanakya-ai-discord-bot.git
cd chanakya-ai-discord-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy

# Set up pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

## 🎨 Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Use type hints where appropriate

### Example:

```python
async def generate_image(prompt: str, steps: int = 50) -> Image:
    """
    Generate an image from a text prompt using Stable Diffusion.
    
    Args:
        prompt: Text description of desired image
        steps: Number of inference steps (default: 50)
        
    Returns:
        PIL Image object
        
    Raises:
        RuntimeError: If CUDA is not available
    """
    # Implementation here
```

## 🧪 Testing

Before submitting:

```bash
# Run tests
pytest tests/

# Check code style
black src/
flake8 src/

# Type checking
mypy src/
```

## 📝 Commit Messages

Format:
```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Build/maintenance tasks

Example:
```
feat: Add image resolution parameter to /image command

- Added resolution parameter to image generation
- Supports 512x512, 768x768, 1024x1024
- Updated documentation

Closes #42
```

## 🔍 Pull Request Guidelines

### Before Submitting:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary dependencies added
- [ ] Tested on your system

### PR Description Should Include:

- What changed and why
- Related issue numbers
- Screenshots (if UI changes)
- Breaking changes (if any)

## 🏗️ Project Structure

```
src/           - Main source code
legacy/        - Historical versions (don't modify)
notebooks/     - Jupyter notebooks for experiments
docs/          - Documentation files
tests/         - Test files (future)
```

## 🌟 Areas for Contribution

### High Priority:
- [ ] Conversation history/context
- [ ] Error handling improvements
- [ ] Rate limiting
- [ ] Caching system
- [ ] Unit tests

### Medium Priority:
- [ ] Custom image parameters
- [ ] Multiple model support
- [ ] Admin commands
- [ ] Usage statistics

### Low Priority:
- [ ] Web dashboard
- [ ] Voice support
- [ ] Multi-language support

## 💬 Communication

- **GitHub Issues**: Bug reports and feature requests
- **Pull Requests**: Code discussions
- **Discord**: Real-time chat (link in README)

## 📜 Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on the issue, not the person
- Respect differing viewpoints
- Accept constructive criticism

## ❓ Questions?

Feel free to:
- Open a discussion on GitHub
- Ask in pull request comments
- Contact maintainers

## 🎉 Recognition

Contributors will be:
- Listed in README
- Credited in release notes
- Given contributor badge

Thank you for contributing! 🙏

---

**Maintainer:** [@Necromancer1009](https://github.com/Necromancer1009)
