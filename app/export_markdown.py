import re
from pathlib import Path


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def save_article_as_markdown(incident, score, priority, article):
    output_dir = Path("outputs/generated_articles")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{incident['id']}-{slugify(incident['title'])}.md"
    file_path = output_dir / filename

    content = f"""# {incident['title']}

**Location:** {incident['location']}  
**Incident Type:** {incident['incident_type']}  
**Priority:** {priority}  
**Score:** {score}  
**Source:** {incident['source_url']}  

---

{article}
"""

    file_path.write_text(content, encoding="utf-8")

    return file_path