import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

def query_llm(prompt: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_predict": 200
                }
            },
            timeout=180  # ⬅️ increased
        )
        response.raise_for_status()
        return response.json().get("response", "No response from LLM")

    except requests.exceptions.Timeout:
        return "LLM is taking longer than expected. Please retry in a moment."

    except Exception as e:
        return f"LLM Error: {str(e)}"
