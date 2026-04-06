# Resume Analyzer 



---
## Features

- **PDF Parsing**: Effortlessly extract text from PDF resumes using `pdfplumber`.
- **Intelligent Matching**: Uses **NLTK** and **Scikit-learn** for keyword extraction and skill matching.
- **Match Score**: Get a percentage-based score indicating how well your resume fits the job requirements.
- **Skill Gap Analysis**:
    - **Matched Skills**: Highlights the relevant skills already present in your resume.
    - **Missing Skills**: Identifies critical skills from the JD that are not in your resume.
- **User-Friendly Dashboard**: A clean, interactive UI built with **Streamlit**.
- **Info Extraction**: Automatically detects contact details (Email, Phone) and Education from the resume.

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
