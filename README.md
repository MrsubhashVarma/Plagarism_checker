# PlagCheck AI 2.0 - Advanced Plagiarism & Document Similarity Platform

PlagCheck AI is a full-stack, Vercel-deployable web application for detecting plagiarism and textual similarity across documents using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🌟 Key Features & Architecture

- **Multi-Format File Support**: Upload `.txt`, `.pdf`, `.docx`, `.md`, and code files (`.py`, `.js`, etc.).
- **Interactive Heatmap Matrix**: Pairwise visual grid displaying similarity percentages across all uploaded files with color-coded risk scales (**High $\ge$ 50%**, **Moderate 20–49%**, **Low < 20%**).
- **Sentence-Level Match Inspector**: Line-by-line sentence similarity detection with side-by-side text highlighting.
- **Quick Text Comparator**: Direct side-by-side text editors with live character counting.
- **Report Export**: Download complete analysis reports in JSON format or generate printable PDF summaries.
- **Vercel Serverless Architecture**: Built with a FastAPI backend serverless handler (`@vercel/python`) and glassmorphic frontend (`public/`).

---

## 📁 Project Structure

```
Plagiarism-checker-Python-master/
├── api/
│   └── index.py            # FastAPI Serverless Engine (TF-IDF, Cosine Similarity, Parsers)
├── public/
│   ├── index.html          # Modern Glassmorphic Dark-Mode UI
│   ├── style.css           # Styling system & responsive animations
│   └── app.js              # Client-side interactive application logic
├── vercel.json             # Vercel deployment configuration
├── requirements.txt        # Backend dependencies
├── app.py                  # Local development server runner
├── ROADMAP.md              # 5-Week development breakdown
└── README.md               # Main project documentation
```

---

## 🚀 How to Run Locally

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Development Server**:
   ```bash
   python app.py
   ```

3. **Access Web Application**:
   Open **`http://127.0.0.1:8000`** in your web browser.

---

## ☁️ Deployment to Vercel

1. Push this repository to GitHub / GitLab / Bitbucket.
2. Log into [Vercel](https://vercel.com) and click **"Add New" -> "Project"**.
3. Import the repository. Vercel will automatically detect `vercel.json` and `api/index.py` to deploy your application.

---

## 🗓️ 5-Week Project Roadmap Summary

- **Week 1**: Problem Definition, TF-IDF Vectorization Research & Cosine Similarity Engine.
- **Week 2**: Multi-Format File Parsers (`.pdf`, `.docx`) & Sentence-Level NLP Matching.
- **Week 3**: FastAPI REST Architecture, Endpoints & Serverless Integration.
- **Week 4**: Glassmorphic UI/UX Frontend Development, Heatmap Matrix & Sentence Match Inspector.
- **Week 5**: QA Verification, UTF-8 Encoding Compatibility, Vercel Deployment & Documentation.

*(See [`ROADMAP.md`](file:///c:/PROJECTS/Slashmark_Intern_-main/Plagiarism-checker-Python-master/Plagiarism-checker-Python-master/ROADMAP.md) for the detailed week-by-week task breakdown).*
