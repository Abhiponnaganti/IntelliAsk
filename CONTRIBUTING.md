# 👋 Welcome to IntelliAsk Contributions!

Thanks for checking out IntelliAsk! We love seeing new ideas, bug fixes, and improvements from the community. Here’s how to get started:

---

## 🛠️ How to Contribute

- **Found a bug?**  
  [Open an issue](https://github.com/IntelliAsk/IntelliAsk/issues) and describe what’s wrong.

- **Have a feature idea?**  
  Open an issue and tell us what you’d like to see.

- **Want to code?**  
  - Fork this repo and clone your fork.
  - Make a new branch for your change.
  - Code, commit, and push.
  - Open a pull request (PR) with a short description.

---

## ⚡ Quick Setup

```sh
git clone https://github.com/your-username/IntelliAsk.git
cd IntelliAsk
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements_ultra_simple.txt
cp .env.example .env  # Add your API keys to .env
```

---

## 🧑‍💻 Coding Tips

- Format code with [Black](https://black.readthedocs.io/) (`black .`)
- Lint with [flake8](https://flake8.pycqa.org/) (`flake8 .`)
- Use clear names and add comments if something isn’t obvious
- Keep PRs focused—one thing at a time is best!

---

## 🚦 Before You Make a Pull Request

- [ ] Code is clean and focused
- [ ] Tests pass (if you added any)
- [ ] You’ve described your change in the PR

---

## 🏃 Running & Testing

```sh
black intelliask_app.py
flake8 intelliask_app.py
streamlit run intelliask_app.py
```

---

## 💬 Need Help?

- Open an issue or discussion on GitHub.

---

Thanks for helping make IntelliAsk better!  
— The IntelliAsk Team
- No question is too small!

---

Thanks for making IntelliAsk better!  
— The IntelliAsk Team
fix: resolve PDF parsing issue
docs: update installation instructions
style: format code with black
refactor: improve error handling
test: add unit tests for document processor
```

### Code Examples
```python
def process_document(file_path: str) -> tuple[str, dict]:
    """
    Process a document and extract its content.
    
    Args:
        file_path: Path to the document file
        
    Returns:
        tuple: (content, metadata) where content is the extracted text
               and metadata contains document information
               
    Raises:
        DocumentProcessingError: If the document cannot be processed
    """
    try:
        # Implementation here
        pass
    except Exception as e:
        logger.error(f"Failed to process {file_path}: {e}")
        raise DocumentProcessingError(f"Processing failed: {e}")
```

## 🔍 Pull Request Process

### Before Submitting
- [ ] Code follows the style guidelines
- [ ] Self-review of the code
- [ ] Comments added for hard-to-understand areas
- [ ] Documentation updated if needed
- [ ] Tests added for new functionality
- [ ] All tests pass

### PR Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass
- [ ] Manual testing performed
- [ ] Edge cases considered

## Screenshots (if applicable)
Add screenshots to help explain your changes
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Performance optimizations
- [ ] Better error handling
- [ ] Additional document formats
- [ ] Improved UI/UX
- [ ] Test coverage improvements

### Medium Priority
- [ ] Multi-language support
- [ ] Export functionality
- [ ] Advanced analytics
- [ ] API endpoints
- [ ] Documentation improvements

### Good First Issues
- [ ] Add tooltips and help text
- [ ] Improve error messages
- [ ] Add more example queries
- [ ] Update dependencies
- [ ] Fix typos and grammar

## 📋 Issue Templates

### Bug Report
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior

**Expected behavior**
What you expected to happen

**Environment**
- OS: [e.g. macOS 12.0]
- Python version: [e.g. 3.9.0]
- IntelliAsk version: [e.g. 1.0.0]

**Additional context**
Any other context about the problem
```

### Feature Request
```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Additional context**
Any other context or screenshots about the feature request.
```

## 🏆 Recognition

Contributors will be:
- Listed in the project's CONTRIBUTORS.md file
- Mentioned in release notes for significant contributions
- Given appropriate credit in documentation

## 📞 Getting Help

- **Questions**: Use GitHub Discussions
- **Email**: balaabhilashponnaganti@gmail.com (for sensitive issues)

## 📜 Code of Conduct

### Our Pledge
We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

---

Thank you for contributing to IntelliAsk! 🧠✨
