import re
from pathlib import Path


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def save_article_as_markdown(incident, score, priority, article_data):
    output_dir = Path("outputs/generated_articles")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{incident['id']}-{slugify(incident['title'])}.md"
    file_path = output_dir / filename

    faq_text = "\n".join(
        [
            f"### {item['question']}\n\n{item['answer']}"
            for item in article_data.get("faq", [])
        ]
    )

    social_posts = "\n".join(
        [
            f"### {item.get('platform', 'Social')}\n\n{item.get('content', '')}"
            for item in article_data.get("social_media_posts", [])
        ]
    )

    internal_links = "\n".join(
        [f"- {link}" for link in article_data.get("suggested_internal_links", [])]
    )

    external_citations = "\n".join(
        [f"- {citation}" for citation in article_data.get("suggested_external_citations", [])]
    )

    content = f"""# {article_data.get("seo_title", incident["title"])}

**Location:** {incident['location']}  
**Incident Type:** {incident['incident_type']}  
**Priority:** {priority}  
**Score:** {score}  
**Source:** {incident['source_url']}  

## Meta Description

{article_data.get("meta_description", "")}

## Article Summary

{article_data.get("article_summary", "")}

## Full Article

{article_data.get("full_article", "")}

## FAQ

{faq_text}

## Suggested Internal Links

{internal_links}

## Suggested External Citations

{external_citations}

## Social Media Posts

{social_posts}
"""

    file_path.write_text(content, encoding="utf-8")

    return file_path