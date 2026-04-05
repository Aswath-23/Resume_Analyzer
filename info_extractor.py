import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from utils import clean_text

nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

KNOWN_SKILLS = [
    # programming languages
    "python", "java", "javascript", "typescript", "c", "c++", "c#",
    "r", "go", "ruby", "swift", "kotlin", "php", "scala", "rust",
    "matlab", "bash", "shell",

    # web
    "html", "css", "react", "angular", "vue", "node", "nodejs",
    "express", "django", "flask", "fastapi", "spring", "springboot",
    "bootstrap", "jquery", "redux", "graphql", "rest", "api",

    # data / ml
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "keras", "pytorch", "scikit-learn", "sklearn",
    "pandas", "numpy", "matplotlib", "seaborn", "opencv",
    "data analysis", "data science", "statistics", "regression",
    "classification", "clustering", "neural network",

    # databases
    "sql", "mysql", "postgresql", "mongodb", "sqlite", "redis",
    "firebase", "cassandra", "oracle", "nosql",

    # cloud and devops
    "aws", "azure", "gcp", "docker", "kubernetes", "jenkins",
    "git", "github", "gitlab", "ci/cd", "linux", "terraform",

    # tools
    "excel", "power bi", "tableau", "jira", "figma",
    "postman", "vscode", "jupyter", "hadoop", "spark",
    "blockchain", "cybersecurity", "agile", "scrum",
]

stop_words = set(stopwords.words('english'))


def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else "Not found"


def extract_phone(text):
    match = re.search(
        r"(\+?\d{1,3}[\s\-]?)?(\(?\d{3}\)?[\s\-]?)?\d{3}[\s\-]?\d{4}", text
    )
    return match.group(0).strip() if match else "Not found"


def extract_skills(text):
    # tokenize and remove stop words using NLTK
    tokens = word_tokenize(text.lower())
    token_set = set(t for t in tokens if t not in stop_words)

    found = []
    cleaned = clean_text(text)

    for skill in KNOWN_SKILLS:
        if " " in skill:
            # multi-word skills need regex since token set won't help here
            if re.search(r"\b" + re.escape(skill) + r"\b", cleaned):
                found.append(skill)
        else:
            if skill in token_set:
                found.append(skill)

    return found


def extract_education(text):
    keywords = [
        "b.tech", "btech", "b.e", "be ", "m.tech", "mtech", "mba",
        "m.sc", "msc", "b.sc", "bsc", "bachelor", "master", "phd",
        "university", "college", "institute", "school", "10th", "12th",
        "ssc", "hsc", "degree", "diploma"
    ]
    lines = text.lower().split("\n")
    edu_lines = []
    for line in lines:
        if any(kw in line for kw in keywords):
            line = line.strip()
            if line and len(line) > 5:
                edu_lines.append(line)
    return edu_lines if edu_lines else ["Not detected"]


def extract_projects(text):
    lines = text.split("\n")
    project_lines = []
    in_projects = False

    for line in lines:
        lower = line.lower().strip()

        if re.search(r"\bprojects?\b", lower) and len(lower) < 30:
            in_projects = True
            continue

        # stop when we hit any other major section heading
        if in_projects and re.search(
            r"\b(experience|education|skills|certifications|achievements|contact)\b", lower
        ) and len(lower) < 30:
            in_projects = False

        if in_projects and line.strip():
            project_lines.append(line.strip())

    return project_lines[:6] if project_lines else ["Not detected"]


def get_resume_info(text):
    return {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "projects": extract_projects(text),
    }
