import streamlit as st
from resume_parser import parse_resume
from info_extractor import get_resume_info
from matcher import get_jd_skills, match_resume, get_score_label
from utils import extract_jd_from_pdf

st.set_page_config(page_title="Resume Analyzer", page_icon="", layout="wide")

st.title("Resume Analyzer and Job Matcher")
st.markdown("Upload your resume and provide a job description to see how well they match.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload Resume")
    st.caption("PDF format only")
    resume_file = st.file_uploader("Choose your resume file", type=["pdf"], key="resume_upload")

with col2:
    st.subheader("Job Description")
    jd_type = st.radio("How to provide JD?", ["Paste Text", "Upload PDF"], horizontal=True)
    
    jd_text = ""
    if jd_type == "Paste Text":
        jd_text = st.text_area(
            "Paste Job Description here",
            height=200,
            placeholder="e.g. We are looking for a Python developer..."
        )
    else:
        jd_file = st.file_uploader("Upload JD PDF", type=["pdf"], key="jd_upload")
        if jd_file:
            jd_text = extract_jd_from_pdf(jd_file)
            st.success("JD PDF loaded successfully!")


st.divider()

analyze_btn = st.button("Analyze Resume", type="primary", use_container_width=True)

if analyze_btn:

    if not resume_file:
        st.error("Please upload a resume file.")
        st.stop()

    if not jd_text.strip():
        st.error("Please paste a job description.")
        st.stop()

    with st.spinner("Reading resume..."):
        resume_text = parse_resume(resume_file)

    if not resume_text.strip():
        st.error("Could not extract text from the resume. Make sure it's a text-based PDF.")
        st.stop()

    info = get_resume_info(resume_text)
    jd_skills = get_jd_skills(jd_text)
    result = match_resume(info["skills"], jd_skills)

    st.success("Done!")
    st.divider()

    st.subheader("Resume Details")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**Email:** {info['email']}")
        st.markdown(f"**Phone:** {info['phone']}")
    with c2:
        edu = " | ".join(info["education"][:2]) if info["education"] else "Not detected"
        st.markdown(f"**Education:** {edu}")

    st.divider()

    st.subheader("Match Score")
    score = result["score"]
    label = get_score_label(score)

    sc1, sc2 = st.columns([1, 2])
    with sc1:
        st.metric("Match Score", f"{score}%")
        st.markdown(f"**Status:** {label}")
    with sc2:
        st.progress(int(score) if score <= 100 else 100)
        st.caption(f"Matched {len(result['matched'])} out of {len(jd_skills)} skills from the job description.")

    st.divider()

    st.subheader("Matched Skills")
    if result["matched"]:
        for i in range(0, len(result["matched"]), 5):
            chunk = result["matched"][i:i+5]
            cols = st.columns(len(chunk))
            for col, skill in zip(cols, chunk):
                col.success(skill)
    else:
        st.info("No matching skills found. Try updating your resume with relevant technologies.")

    st.divider()

    st.subheader("Missing Skills")
    if result["missing"]:
        st.markdown("These were in the JD but not found in your resume:")
        missing = result["missing"]
        for i in range(0, len(missing), 5):
            chunk = missing[i:i+5]
            cols = st.columns(len(chunk))
            for col, skill in zip(cols, chunk):
                col.error(skill)
        top = missing[:5]
        st.info(f"Suggestion: Consider adding {', '.join(top)} to your resume to improve your match score.")
    else:
        st.success("Your resume covers all the skills mentioned in the job description.")


    st.divider()

    with st.expander("All Skills Found in Resume"):
        if info["skills"]:
            st.write(", ".join(sorted(info["skills"])))
        else:
            st.write("No recognizable skills found.")


st.divider()
st.caption("Note: Matching uses NLTK for core skills and keyword-matching for multi-word phrases.")

