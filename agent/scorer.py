from sentence_transformers import SentenceTransformer, util
import re

class ResumeScorer:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    @staticmethod
    def clean(text):
        return re.sub(r'\s+', ' ', text.lower())

    @staticmethod
    def extract_skills(text):
        skill_keywords = [
            "python", "java", "c++", "machine learning", "deep learning",
            "pandas", "numpy", "tensorflow", "pytorch",
            "sql", "mongodb", "git", "aws", "gcp",
            "communication", "problem solving", "data visualization"
        ]

        text = text.lower()
        found = [skill for skill in skill_keywords if skill in text]
        return list(set(found))

    @staticmethod
    def score_resume(jd_text, resume_text):

        jd_clean = ResumeScorer.clean(jd_text)
        resume_clean = ResumeScorer.clean(resume_text)

        # Embeddings similarity score
        jd_emb = ResumeScorer.model.encode(jd_clean)
        res_emb = ResumeScorer.model.encode(resume_clean)

        similarity = util.cos_sim(jd_emb, res_emb).item()
        match_score = round(similarity * 100, 2)

        # Skills extraction
        jd_skills = ResumeScorer.extract_skills(jd_clean)
        res_skills = ResumeScorer.extract_skills(resume_clean)

        missing_skills = [s for s in jd_skills if s not in res_skills]

        strengths = res_skills[:3] if res_skills else ["Good technical background"]
        weaknesses = missing_skills[:3] if missing_skills else ["None"]

        summary = (
            f"The candidate shows knowledge in {', '.join(res_skills)}. "
            f"They are missing skills such as {', '.join(missing_skills)}."
        )

        final_decision = "Strong Fit" if match_score > 70 else "Moderate Fit"

        return {
            "match_score": match_score,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "missing_skills": missing_skills,
            "summary": summary,
            "final_decision": final_decision
        }
