# Resume Analyzer & Job Matcher 📝🔍

### 🚀 A Personal Project for Seamless Recruitment Analysis

**Resume Analyzer** is a powerful, ML-based tool designed to help job seekers and recruiters bridge the gap between resumes and job descriptions. Built using **Python**, **Streamlit**, and **Natural Language Processing (NLP)** techniques, this application analyzes a candidate's resume against a specific job description to provide a detailed match score, skill gap analysis, and improvement suggestions.

---

## ✨ Features

- **📄 PDF Parsing**: Effortlessly extract text from PDF resumes using `pdfplumber`.
- **🎯 Intelligent Matching**: Uses **NLTK** and **Scikit-learn** for keyword extraction and skill matching.
- **📊 Match Score**: Get a percentage-based score indicating how well your resume fits the job requirements.
- **🔍 Skill Gap Analysis**:
    - **Matched Skills**: Highlights the relevant skills already present in your resume.
    - **Missing Skills**: Identifies critical skills from the JD that are not in your resume.
- **📱 User-Friendly Dashboard**: A clean, interactive UI built with **Streamlit**.
- **📩 Info Extraction**: Automatically detects contact details (Email, Phone) and Education from the resume.

---

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Framework**: [Streamlit](https://streamlit.io/) (for the UI)
- **NLP Libraries**: `NLTK`, `Regex`
- **Data Handling**: `pdfplumber` (PDF text extraction)
- **Algorithm**: Keyword frequency analysis and set-based matching.

---

## ⚙️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Resume-Analyzer-Python.git
   cd Resume-Analyzer-Python
   ```

2. **Create a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate # On macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## 📂 Project Structure

```text
📁 Resume_Analyzer_Python
├── 📄 app.py               # Main Streamlit application
├── 📄 info_extractor.py    # Logic for NER and info extraction
├── 📄 matcher.py           # Skill matching algorithms
├── 📄 resume_parser.py     # PDF text extraction logic
├── 📄 utils.py             # Helper functions
├── 📄 requirements.txt     # List of dependencies
└── 📁 sample_data          # Test resumes and JDs
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/Resume-Analyzer-Python/issues).

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**[Your Name]**  
*Python & Machine Learning Enthusiast*  
[Your LinkedIn] | [Your Portfolio]

---
*If you find this project helpful, don't forget to ⭐ the repository!*
