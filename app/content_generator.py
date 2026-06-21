import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("SUMOPOD_API_KEY"),
    base_url=os.getenv("SUMOPOD_BASE_URL")
)


def generate_content(prompt: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("SUMOPOD_MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content