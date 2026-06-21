import os
import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("SUMOPOD_API_KEY"),
    base_url=os.getenv("SUMOPOD_BASE_URL")
)


def generate_content(prompt: str) -> dict:
    response = client.chat.completions.create(
        model=os.getenv("SUMOPOD_MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(f"AI returned invalid JSON:\n{content}")