from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def searcher():
    pass