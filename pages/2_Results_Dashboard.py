import streamlit as st
import pandas as pd
from tiny_db import LocalDB

st.title("📊 Results Dashboard")

db = LocalDB()
data = db.get_all()

if not data:
    st.warning("No results in database yet.")
    st.stop()

df = pd.DataFrame(data)

st.dataframe(df)

# --- Score Color Indicator ---
def score_color(score):
    if score >= 80: return "🟢 Strong Match"
    elif score >= 50: return "🟡 Moderate Match"
    else: return "🔴 Weak Match"

df["Score Level"] = df["match_score"].apply(score_color)

st.markdown("### 📥 Download Results as CSV")
st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False),
    file_name="resume_results.csv",
    mime="text/csv"
)
