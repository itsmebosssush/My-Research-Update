import streamlit as st
import requests
import datetime

# --- APP CONFIG ---
st.set_page_config(page_title="ScholarSphere", page_icon="🔬")

st.title("🔬 ScholarSphere")
st.subheader("Your Daily Research Brief")
st.write(f"Today's Date: {datetime.date.today()}")

# --- SEARCH ENGINE ---
# We use Semantic Scholar API (Free for researchers)
def fetch_research(query):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,abstract,url,year,authors"
    try:
        response = requests.get(url)
        return response.json().get('data', [])
    except:
        return []

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Research Interests")
topic = st.sidebar.selectbox("Select Focus", 
    ["Zirconium Corrosion AI", "Biomaterials Electrochemistry", "Self-healing Polymer Coatings"])

# --- MAIN INTERFACE ---
if st.button("Get Latest Updates"):
    with st.spinner("Analyzing the latest journals..."):
        results = fetch_research(topic)
        
        if results:
            for paper in results:
                with st.expander(f"📄 {paper['title']} ({paper['year']})"):
                    st.write(f"**Authors:** {', '.join([a['name'] for a in paper['authors'][:3]])} et al.")
                    st.write(f"**Abstract:** {paper['abstract'][:500]}...")
                    st.markdown(f"[Read Full Paper]({paper['url']})")
                    
                    # AI Synthesis Simulation (You can plug Perplexity API here later)
                    st.info(f"💡 **Scholar Insight:** This aligns with your PhD work on {topic}. Look for gaps in 'In-vitro' testing mentioned here.")
        else:
            st.error("No new papers found for this specific query today.")

st.sidebar.markdown("---")
st.sidebar.write("🎯 **Goal:** Perplexity Research Resident 2026")
