from app.data_loader import load_data
from app.llm_client import query_llm

def run_agent(user_query: str):
    df = load_data()

    failed_by_city = (
        df[df["status"] == "Failed"]
        .groupby("city")
        .size()
        .sort_values(ascending=False)
        .head(3)
    )

    top_city = failed_by_city.index[0]
    count = failed_by_city.iloc[0]

    context = f"""
Failed Transactions Summary:
{failed_by_city.to_string()}
"""

    prompt = f"""
You are a banking analytics expert.

{context}

Question:
{user_query}

Answer in 2–3 concise sentences with business insight.
"""

    llm_response = query_llm(prompt)

    # fallback (VERY IMPORTANT)
    if "LLM" in llm_response:
        return f"{top_city} has the highest number of failed transactions ({count}), indicating potential payment or network issues."

    return llm_response
