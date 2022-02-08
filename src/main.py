from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class='HTMLResponse')
async def searcher(request: Request):
    return templates.TemplateResponse('search.html', {'request': request})

@app.post('/', response_class='HTMLResponse')
async def search_answer(requset: Request, search_request: str = Form()):
    pass