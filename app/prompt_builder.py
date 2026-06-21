# app/prompt_builder.py

def build_article_prompt(incident, score, priority):
    return f"""
You are an AI content assistant for a personal injury law firm.

Create a structured JSON response only.
Do not include markdown outside the JSON.
Do not wrap the JSON in code blocks.

Important rules:
- Do not copy or rewrite the news story.
- Use the incident only as a starting point.
- Focus mostly on legal education.
- Do not provide legal advice.
- Mention that every case depends on specific facts.
- Keep the tone professional, helpful, and localized.

Incident:
Title: {incident["title"]}
Location: {incident["location"]}
Incident Type: {incident["incident_type"]}
Severity: {incident["severity"]}
Fatalities: {incident["fatalities"]}
Injuries: {incident["injuries"]}
Commercial Vehicle Involved: {incident["commercial_vehicle"]}
Child Involved: {incident["child_involved"]}
DUI Suspected: {incident["dui_suspected"]}
Summary: {incident["summary"]}
Source URL: {incident["source_url"]}

Priority Score: {score}
Priority Level: {priority}

Return this exact JSON structure:

{{
  "seo_title": "",
  "meta_description": "",
  "article_summary": "",
  "full_article": "",
  "faq": [
    {{
      "question": "",
      "answer": ""
    }}
  ],
  "suggested_internal_links": [],
  "suggested_external_citations": [],
  "social_media_posts": [
    {{
      "platform": "",
      "content": ""
    }}
  ]
}}
""".strip()