import json

from incident_scorer import calculate_score, classify_priority
from prompt_builder import build_article_prompt
from content_generator import generate_content
from export_markdown import save_article_as_markdown


with open("data/sample_incidents.json", "r") as f:
    incidents = json.load(f)


for incident in incidents:
    score = calculate_score(incident)
    priority = classify_priority(score)

    prompt = build_article_prompt(
        incident=incident,
        score=score,
        priority=priority
    )

    print(f"Generating article for: {incident['title']}")
    print(f"Priority: {priority} | Score: {score}")

    article = generate_content(prompt)

    file_path = save_article_as_markdown(
        incident=incident,
        score=score,
        priority=priority,
        article=article
    )

    print(f"Saved to: {file_path}")
    print("=" * 80)