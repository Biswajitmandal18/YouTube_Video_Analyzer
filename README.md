# 📽️ AI YouTube Video Analyzer

An intelligent YouTube video analysis tool powered by **Agno**, **Groq LLM** (`qwen/qwen3.8-27b`), and **Streamlit**. It extracts transcripts and generates detailed, structured summaries, key takeaways, and timestamped outlines for any YouTube video.

---

## ✨ Features

- **📊 Comprehensive Video Overview**: Identifies video category, metadata, and general content outline.
- **⏱️ Precise Timestamps**: Automatically marks major topic transitions with format `[start_time, end_time, summary]`.
- **💡 Key Insights & Takeaways**: Highlights essential points, practical demonstrations, and references.
- **🎨 Visual Categorization**: Tags content using category emojis (Educational 📚, Technical 💻, Gaming 🎮, Reviews 📱, etc.).
- **⚡ Fast Inference**: Powered by Groq's high-speed LPU inference engine.
- **🖥️ Clean Web Interface**: Simple and intuitive UI built with Streamlit.

---

## 🛠️ Tech Stack

- **Framework**: [Agno](https://github.com/agno-agi/agno) (formerly Phidata)
- **LLM**: Groq (`qwen/qwen3.8-27b`)
- **Tools**: Agno `YouTubeTools` (via `youtube-transcript-api`)
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Language**: Python 3.10+

---

## 📁 Project Structure

```plaintext
├── .env.example          # Environment variable template
├── .gitignore            # Git ignore file (keeps .env and cache secure)
├── LICENSE               # MIT License
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
├── ui.py                 # Streamlit web interface
└── youtube_analyzer.py   # Agno agent definition and instructions
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd "Agentic Ai Project"
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Create a `.env` file from the example template:
   ```bash
   cp .env.example .env     # On Linux/macOS
   copy .env.example .env   # On Windows
   ```
2. Get your Groq API key from the [Groq Console](https://console.groq.com/keys).
3. Open `.env` and paste your API key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

---

## 💻 Running the Application

Launch the Streamlit web app:

```bash
streamlit run ui.py
```

After starting, navigate to `http://localhost:8501` in your browser.

1. Paste any public YouTube URL (with available captions/transcripts).
2. Click **"Analyze Video"**.
3. View the generated breakdown and timestamped notes!

---

## 🔒 Security Note

Never commit your `.env` file or expose your API keys. The included `.gitignore` is pre-configured to keep your credentials safe.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
