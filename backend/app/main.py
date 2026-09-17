from fastapi import FastAPI

app = FastAPI(
    title="Portfolio Analytics API",
    version="0.1.0",
)


@app.get("/api/v1/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
