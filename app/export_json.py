import json
from pathlib import Path


def save_json_output(
    incident,
    score,
    priority,
    article_data
):
    output_dir = Path(
        "outputs/generated_json"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = (
        output_dir /
        f"incident_{incident['id']}.json"
    )

    payload = {
        "incident": incident,
        "score": score,
        "priority": priority,
        "content": article_data
    }

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            payload,
            f,
            indent=4,
            ensure_ascii=False
        )

    return file_path