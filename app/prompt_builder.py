# app/prompt_builder.py

def build_article_prompt(incident, score, priority):
    prompt = f"""
You are an AI content assistant for a personal injury law firm.

Create a publication-ready legal education draft based on the incident below.

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

Generate the following sections:

1. SEO Title
2. Meta Description
3. Article Summary
4. Full Blog Article
5. Frequently Asked Questions
6. Suggested Internal Links
7. Suggested External Citations
8. Social Media Post Variations
"""
    return prompt.strip()