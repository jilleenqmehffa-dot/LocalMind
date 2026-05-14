from fastapi import FastAPI

app = FastAPI(title="LocalMind")


@app.get("/")
async def root() -> dict[str, str]:
    return {"status": "ok"}

