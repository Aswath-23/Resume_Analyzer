import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from utils import clean
from info_extractor import KNOWN_SKILLS

nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))


def jd_skills(jd_text):
    # use NLTK to tokenize JD and strip stop words before matching
    tokens = word_tokenize(jd_text.lower())
    jd_tokens = set(t for t in tokens if t not in stop_words)

    found = []
    cleaned = clean(jd_text)

    for skill in KNOWN_SKILLS:
        if " " in skill:
            if re.search(r"\b" + re.escape(skill) + r"\b", cleaned):
                found.append(skill)
        else:
            if skill in jd_tokens:
                found.append(skill)

    return found


def match(resume_skills, jd_skills):
    if not jd_skills:
        return {"matched": [], "missing": [], "score": 0}

    r = set(resume_skills)
    j = set(jd_skills)

    matched = sorted(r & j)
    missing = sorted(j - r)
    score = round((len(matched) / len(j)) * 100, 1)

    return {"matched": matched, "missing": missing, "score": score}


def check_score(score):
    if score >= 75:
        return "Strong Match"
    elif score >= 50:
        return "Good Match"
    elif score >= 25:
        return "Partial Match"
    else:
        return "Low Match - Needs Improvement"
