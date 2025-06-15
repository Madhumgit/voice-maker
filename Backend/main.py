from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import re

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

@app.post("/interact")
async def interact(request: Request):
    data = await request.json()
    user_input = data.get("user_input", "").lower()

    try:
     
        if any(greet in user_input for greet in ["hi", "hello", "hey"]):
            return {"message": "Hello! How can I assist you today?"}
        elif "how are you" in user_input:
            return {"message": "I'm an AI assistant — always running at 100%! How can I help you today?"}
        elif "thank you" in user_input or "thanks" in user_input:
            return {"message": "You're welcome! I'm always here to help."}
        else:
           
            search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={user_input}&format=json"
            response = requests.get(search_url)
            response.raise_for_status()
            result_json = response.json()

            search_results = result_json.get('query', {}).get('search', [])

            if search_results:
                raw_summary = search_results[0]['snippet']
                summary = clean_html(raw_summary)
                return {"message": summary}
            else:
                return {"message": f"Sorry, I couldn't find information on '{user_input}'."}

    except Exception as e:
        print(e)
        return {"error": str(e)}
