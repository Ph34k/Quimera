import os
import re
from app.main import app

def test_markdown_docs_endpoints_exist():
    """
    Checks all markdown files in the docs/agents directory.
    Extracts documented endpoints formatted like `HTTP_METHOD /api/v1/...`
    and verifies that they actually exist in the FastAPI application routes.
    """

    docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs", "agents")
    assert os.path.exists(docs_dir), f"Directory {docs_dir} does not exist."

    # Extract all routes loaded in the app
    app_routes = []
    for route in app.routes:
        if hasattr(route, "methods") and hasattr(route, "path"):
            for method in route.methods:
                app_routes.append(f"{method} {route.path}")

    # Regex to find endpoint definitions in Markdown
    # Looks for lines like: ### `POST /api/v1/scout/mission`
    endpoint_pattern = re.compile(r"### `([A-Z]+) (/api/v1/[a-zA-Z0-9_/-]+)`")

    missing_endpoints = []

    for filename in os.listdir(docs_dir):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(docs_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        matches = endpoint_pattern.findall(content)
        for method, path in matches:
            formatted_endpoint = f"{method} {path}"
            if formatted_endpoint not in app_routes:
                missing_endpoints.append(f"Documented in {filename}: {formatted_endpoint}")

    assert len(missing_endpoints) == 0, f"Found documented endpoints that do not exist in the code:\n" + "\n".join(missing_endpoints)
