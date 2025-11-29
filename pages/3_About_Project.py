import streamlit as st

st.title("📘 About This Project")
st.markdown("---")

st.subheader("🤖 AI Resume Screening Agent")

st.write("""
This project is built for the **Rooman AI Internship Challenge**.
It automatically evaluates resumes using:

- 🔍 Text Extraction (PDF → Text)
- 🧠 NLP-based scoring system
- 📊 Similarity Matching
- 🎯 Rule-based evaluation
- 💾 Local TinyDB storage system
""")

st.markdown("---")

st.subheader("🎯 Key Features")

st.write("""
✔ Upload Job Description (JD)  
✔ Upload multiple resumes  
✔ Extract and process resume text  
✔ Identify strengths, weaknesses, and missing skills  
✔ Calculate match score  
✔ Save results to TinyDB  
✔ View results in dashboard  
✔ Fully offline — No API required  
""")

st.markdown("---")

st.subheader("🛠️ Technologies Used")

st.write("""
- **Python**
- **Streamlit**
- **TinyDB**
- **NLP techniques**
- **Custom rule-based scoring model**
- **Vector similarity search**
""")

st.markdown("---")

st.subheader("👨‍💻 Developer")
st.write("""
**Pradeep Aili**  
Built under guidance for the Rooman AI Internship Challenge 2025.
""")

st.success("This page is now complete and ready for submission! 🚀")
