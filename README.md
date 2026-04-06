# Resume Analyzer 📝🔍



**Resume Analyzer** is a powerful, ML-based tool designed to help job seekers and recruiters bridge the gap between resumes and job descriptions. Built using **Python**, **Streamlit**, and **Natural Language Processing (NLP)** techniques, this application analyzes a candidate's resume against a specific job description to provide a detailed match score, skill gap analysis, and improvement suggestions.

---

## Features

- ** PDF Parsing**: Effortlessly extract text from PDF resumes using `pdfplumber`.
- ** Intelligent Matching**: Uses **NLTK** and **Scikit-learn** for keyword extraction and skill matching.
- ** Match Score**: Get a percentage-based score indicating how well your resume fits the job requirements.
- ** Skill Gap Analysis**:
    - **Matched Skills**: Highlights the relevant skills already present in your resume.
    - **Missing Skills**: Identifies critical skills from the JD that are not in your resume.
- ** User-Friendly Dashboard**: A clean, interactive UI built with **Streamlit**.
- ** Info Extraction**: Automatically detects contact details (Email, Phone) and Education from the resume.

---

## Tech Stack

- **Language**: Python 3.9+
- **Framework**: [Streamlit](https://streamlit.io/) (for the UI)
- **NLP Libraries**: `NLTK`, `Regex`
- **Data Handling**: `pdfplumber` (PDF text extraction)
- **Algorithm**: Keyword frequency analysis and set-based matching.

---

## Installation & Setup
   
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   
```

*If you find this project helpful, don't forget to ⭐ the repository!*
