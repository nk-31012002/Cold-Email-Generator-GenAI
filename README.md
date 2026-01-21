# 🚀 Personal AI Job Outreach Assistant

An automated cold email generator designed to help software engineers land interviews. This tool scrapes job postings directly from company career pages, analyzes the required tech stack, and crafts a highly personalized cold email. 

To ensure the email is persuasive, the system uses a **Vector Database (ChromaDB)** to query your specific projects (like Companion.ai or CodeCraft) and includes the most relevant GitHub links that match the job's requirements.

**The Workflow:**
- **Scrape:** Extracts job roles and skills from any career URL using LangChain.
- **Match:** Uses semantic search to find which of your personal projects best fit the job description.
- **Generate:** Uses Llama 3.3 (via Groq) to write a professional email from **Nagendra Kumar**, emphasizing your experience at Amnic and your competitive programming achievements.



## 🛠️ Tech Stack
- **LLM:** Llama-3.3-70b-versatile (via Groq)
- **Orchestration:** LangChain
- **Vector Database:** ChromaDB
- **Frontend:** Streamlit
- **Web Scraping:** LangChain Community WebBaseLoader

## 🚀 Set-up

1. **Get your API Key:**
   Obtain an API_KEY from the [Groq Console](https://console.groq.com/keys). Create a file at `app/.env` and add:
   ```text
   GROQ_API_KEY=your_api_key_here