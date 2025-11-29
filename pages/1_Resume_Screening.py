import streamlit as st
import os
import json
from agent.extractor import ResumeExtractor
from agent.scorer import ResumeScorer
from agent.vector_store import VectorStore
from tiny_db import LocalDB

st.title("📄 Resume Screening")

sheet_db = LocalDB()
vector_db = VectorStore()

st.markdown("Upload JD and Candidate Resumes. AI will screen and store results.")

st.markdown("---")

# ---------------- JD UPLOAD ----------------
st.header("📄 Step 1: Upload Job Description (JD)")

jd_file = st.file_uploader("Upload JD File (PDF/TXT)", type=["pdf", "txt"])
jd_text = ""

if jd_file:
    if jd_file.type == "application/pdf":
        jd_text = ResumeExtractor.extract_text(jd_file)
    else:
        jd_text = jd_file.read().decode("utf-8")

    st.success("JD Uploaded Successfully!")
    st.text_area("Extracted JD Text", jd_text, height=200)

    vector_db.add("job_description", jd_text, {"type": "jd"})

# ------------- RESUME UPLOAD ----------------
st.header("📚 Step 2: Upload Candidate Resumes")

resume_files = st.file_uploader("Upload Resumes", type=["pdf"], accept_multiple_files=True)
results = []

if resume_files and jd_text:
    for resume_file in resume_files:
        resume_text = ResumeExtractor.extract_text(resume_file)

        st.subheader(f"📌 Processing: {resume_file.name}")

        vector_db.add(resume_file.name, resume_text, {"type": "resume"})

        ai_json = ResumeScorer.score_resume(jd_text, resume_text)
        results.append(ai_json)

        st.write(f"### 🏆 Match Score: **{ai_json['match_score']}%**")
        st.write("#### 👍 Strengths:", ai_json["strengths"])
        st.write("#### 👎 Weaknesses:", ai_json["weaknesses"])
        st.write("#### 🎯 Missing Skills:", ai_json["missing_skills"])
        st.write("#### 📝 Summary:", ai_json["summary"])
        st.write("#### Final Decision:", ai_json["final_decision"])

        st.markdown("---")

        sheet_db.save({
            "resume": resume_file.name,
            "match_score": ai_json["match_score"],
            "strengths": ai_json["strengths"],
            "weaknesses": ai_json["weaknesses"],
            "missing_skills": ai_json["missing_skills"],
            "decision": ai_json["final_decision"]
        })

if results:
    st.success("Processing Complete! Saved to Local Database.")
