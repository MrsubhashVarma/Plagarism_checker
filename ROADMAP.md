# 🗓️ 5-Week Development Roadmap

This document outlines the week-by-week process of engineering the Plagiarism & Document Similarity Platform from a basic CLI script into a Vercel-deployed web application.

---

### **Week 1: Problem Definition, Algorithm Research & Core Engine**
- **Project Scope & Architecture Setup**: Defined project requirements for document similarity detection and set up the Python development environment.
- **Feature Extraction Implementation**: Used `TfidfVectorizer` from `scikit-learn` to convert raw text into numerical term frequency-inverse document frequency vectors.
- **Vector Similarity Calculations**: Implemented `cosine_similarity` to calculate mathematical distance scores between document vectors.
- **CLI Prototype**: Verified pairwise comparisons on basic `.txt` files in the command line environment.

---

### **Week 2: Multi-Format File Parsing & Sentence-Level NLP**
- **Multi-Format Document Extraction**: Integrated `pypdf` for `.pdf` text extraction and `python-docx` for `.docx` word processing files.
- **Sentence-Level Match Inspector**: Designed a custom sentence-splitting algorithm to analyze document passages line-by-line.
- **N-Gram Tokenization**: Configured unigram and bigram (`ngram_range=(1, 2)`) vectorization to detect phrase-level paraphrasing.
- **Preprocessing & Normalization**: Added stop-word filtering, lowercase conversion, and UTF-8 encoding sanitization.

---

### **Week 3: REST API Architecture & Serverless Integration**
- **FastAPI Backend Setup**: Transitioned standalone scripts into a modular FastAPI application (`api/index.py`).
- **API Endpoints Creation**: 
  - `POST /api/check-files`: Multipart upload handler for batch file analysis.
  - `POST /api/check-text`: Direct JSON text string comparison payload handler.
  - `GET /api/sample-data`: Pre-configured demo dataset endpoint.
- **Validation & Error Handling**: Implemented robust HTTP exceptions for unreadable files, corrupt payloads, and invalid file formats.
- **CORS & Middleware**: Configured Cross-Origin Resource Sharing (CORS) for seamless frontend integration.

---

### **Week 4: Frontend Development & Interactive UI/UX**
- **Modern Design System**: Created a glassmorphic dark-mode web application using HTML5, CSS3, and JavaScript (`public/index.html`, `public/style.css`).
- **Drag-and-Drop File Picker**: Built an intuitive upload interface for multi-file batch scanning.
- **Interactive Heatmap Matrix**: Designed a visual similarity grid with color-coded risk scales (Green -> Yellow -> Red).
- **Side-by-Side Sentence Inspector**: Developed a split-pane inspector with highlighted sentence matches.
- **Report Export Capabilities**: Added 1-click **Export to JSON** and **Printable PDF** report functionality.

---

### **Week 5: Quality Assurance, Vercel Cloud Deployment & Documentation**
- **Vercel Cloud Configuration**: Authored `vercel.json` to deploy backend serverless functions (`@vercel/python`) and static assets (`@vercel/static`).
- **Empirical End-to-End Testing**: Conducted endpoint stress testing, verified UTF-8 terminal encoding compatibility, and checked cross-browser responsiveness.
- **Performance Optimization**: Minified asset delivery and optimized TF-IDF vector matrix computations.
- **Project Documentation**: Updated codebase files, deployment instructions, and system architecture guides.
