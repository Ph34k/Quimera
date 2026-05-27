# 🚀 Getting Started

Welcome to the Quimera development environment. This guide will help you set up the project locally for development or run it via Docker.

## Prerequisites

*   **Python:** 3.10+
*   **Docker:** (Optional) For containerized execution.
*   **API Keys:** An OpenAI API key is required to test the NLP agents (`Analyst`, `Scribe`, `Persuasion`).

## Local Development Setup

1.  **Clone and Navigate**
    ```bash
    git clone <repo-url>
    cd projeto-quimera
    ```

2.  **Environment Variables**
    Copy the example environment file and add your actual keys:
    ```bash
    cp .env.example .env
    # Edit .env and set OPENAI_API_KEY="sk-..."
    ```

3.  **Install Dependencies**
    It is recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

4.  **Run the Server**
    Start the FastAPI application using `uvicorn`:
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

5.  **Access the API**
    *   API Base: `http://localhost:8000`
    *   Interactive Docs (Swagger): `http://localhost:8000/docs`

## Running Tests

To run the local test battery (mocked production testing):

```bash
pytest tests/ -v
```

## Docker Deployment

To build and run the entire ecosystem as an isolated container:

```bash
# Build the image
docker build -t quimera-api .

# Run the container (Make sure to pass the API key)
docker run -d \
  --name quimera \
  -p 8000:8000 \
  -e OPENAI_API_KEY="your_actual_key_here" \
  quimera-api
```
