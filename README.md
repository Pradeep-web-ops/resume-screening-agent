-> AI Resume Screening Agent : 
    A smart AI-powered tool that evaluates resumes automatically using job descriptions.  
    Built for the Rooman Technologies AI Internship Challenge.

-> Project Overview  :
    The AI Resume Screening Agent compares multiple resumes against a job description (JD) and generates:
    - Match Score (0–100%)
    - Strengths
    - Weaknesses
    - Missing Skills
    - Summary of the candidate
    - Final Hiring Decision (Strong Fit / Moderate Fit / Weak Fit)
All results are stored locally using **TinyDB** and can be viewed through the dashboard.

-> Key Features  :
    1. Upload Job Description  
    Upload PDF/TXT JD → system extracts skills automatically
    2. Upload Candidate Resumes :
    Upload one or multiple PDFs → AI evaluates them immediately.
    3. AI-Based Scoring :
    Offline scoring algorithm (no API needed) that matches skills between JD & Resume.
    4. Local Database (TinyDB) :
    All results are stored in:  db.json file
    5. Dashboard View :
    - All past scores  
    - Candidate details  
    - Trends & insights (match score, skills missing etc.)
    6. Multi-Page Streamlit App  
    - Resume Screening  
    - Results Dashboard  
    - About Project  

-> Tech Stack :
    **Frontend / UI** - Streamlit
    **Frontend / UI** - Python, PDF text extraction, Skill matching algorithm
    **Database** - TinyDB (local JSON-based lightweight DB)
    **Other Tools** - ChromaDB (local vector storage), Regular expressions for skill extraction

-> 📁 Project Structure :
    resume-screening-agent/
    │
    ├── pages/
    │ ├── 1_Resume_Screening.py
    │ ├── 2_Results_Dashboard.py
    │ └── 3_About_Project.py
    │
    ├── agent/
    │ ├── extractor.py
    │ ├── scorer.py
    │ └── vector_store.py
    │
    ├── data/
    │ └── db.json
    │
    ├── tiny_db.py
    ├── requirements.txt
    └── README.md

-> ⚙️ Installation & Running Locally :
    **Clone the repository** - git clone https://github.com/Pradeep-web-ops/resume-screening-agent.git
    **Create virtual environment** - python -m venv venv
    **Activate** - windows(venv\Scripts\activate)
    **Install dependencies** - pip install -r requirements.txt

-> 📊 Architecture Diagram
    User → Streamlit UI
    ↓
    Upload JD → Extract Skills → Save to Vector Store
    Upload Resume → Extract Skills → AI Scoring
    ↓
    Score, Missing Skills, Summary
    ↓
    TinyDB Storage
    ↓
    Dashboard Visualization

-> 📈 Future Improvements (for Jury)
    - Add cloud database (MongoDB / Firebase)
    - Add compatibility score using ML models
    - Add ATS-style resume formatting check
    - Add PDF report download
    - Deploy on Streamlit Cloud

-> 👤 Developed By  
      **Pradeep Aili**  
      AI & Python Developer 


    

