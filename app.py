import streamlit as st

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Resume Screening Agent")
st.write("Welcome! Use the left sidebar to navigate between:")
st.markdown("""
- 📄 **Resume Screening**
- 📊 **Results Dashboard**
- ℹ️ **About Project**
""")

st.markdown("---")

st.subheader("🚀 How this works")
st.write("""
This AI system evaluates resumes against a Job Description using NLP, vector similarity, and rule-based scoring.

It extracts:
- 🧠 Strengths  
- 👎 Weaknesses  
- 🎯 Missing Skills  
- 📝 Summary  
- 🏆 Match Score  

All results are stored in a local TinyDB database.
""")

st.success("Navigate using the sidebar to begin!")
