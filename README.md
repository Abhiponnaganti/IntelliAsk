# 🧠 IntelliAsk

Chat with your documents. Upload a file, ask questions, and get answers—instantly.

---

## What is IntelliAsk?

IntelliAsk is a simple app that lets you talk to your PDFs, DOCX, or TXT files. Just upload a document, type your question, and get clear, sourced answers.

---

## Features

- Works with PDF, DOCX, and TXT files
- Ask questions in plain English
- Answers include document sources
- Runs locally on your computer
- Clean, dark-themed interface

---

## Quick Start

**Requirements:**  
- Python 3.8 or newer  
- [Groq API key](https://console.groq.com/) or OpenAI key

**Setup:**
```sh
git clone https://github.com/yourusername/IntelliAsk.git
cd IntelliAsk
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements_ultra_simple.txt
cp .env.example .env  # Add your API key to .env
```

**Run:**
```sh
streamlit run intelliask_app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Project Structure

```
IntelliAsk/
├── intelliask_app.py
├── requirements_ultra_simple.txt
├── .env.example
└── README.md
```

---

## Need Help?

- Open an issue on GitHub if you have questions or run into problems.

---

## Contributing

Pull requests are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for a quick guide.

---

## License

MIT License

---

*Made with ❤️ by the IntelliAsk team*
