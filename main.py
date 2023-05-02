from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
from utils import get_html
import random
app = FastAPI()

# Ruta a los archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para las plantillas HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    if(query == 'hommies'):
        url = random.choice([
            'https://drive.google.com/file/d/1qaC68HjQv6ROiCvjlHhSdlf5Kn5W0QhV/view?usp=sharing',
            'https://drive.google.com/file/d/1r3AVTwVI2o3ctvKGhrtBx-FCrrPSIXpp/view?usp=sharing',
            'https://drive.google.com/file/d/1rBHf65OiaMAPBvp8KAzaDCGgPaS6HgZX/view?usp=sharing',
            'https://drive.google.com/file/d/1qgRvrNPUK9eFrj7zPOcDTW253i37Cgu1/view?usp=sharing',
            'https://drive.google.com/file/d/1qoRjEa5hzLGNWhMf5eqNGBO8RkagY0Ch/view?usp=sharing',
            'https://drive.google.com/file/d/1qqVFtEcb7WscQ42Ki4C50tJjKAM3NEtv/view?usp=sharing',
            'https://drive.google.com/file/d/1qsTE6EXRyE3dOD0KbgCsNNtz0zZnWJ0e/view?usp=sharing',
            'https://drive.google.com/file/d/1q_rwPkkBVRhc_kbf4cEXNb6uJMXNOk7q/view?usp=sharing'
        ])
        html_content='''
        <!DOCTYPE html>
        <head>
            <title>Hommies</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="/static/style.css">
            <meta name="generator" content="ASCII Magic 2.1 - https://github.com/LeandroBarone/python-ascii_magic/" />
        </head>
        <body>
        <h1 ><a href="/">Hommies </a> <a onclick="location.reload()">Random</a> </h1>
        <pre style="display: inline-block; border-width: 4px 6px; border-color: black; border-style: solid; background-color:black; font-size: 8px; ">
        '''
        html_content += get_html(url)
        
        html_content += '''
        <footer>
            <p>Mis redes:</p>
            <ul>
                <li>Email: <a href="mailto:lucasmvegap@gmail.com" target="_blank"> lucasmvegap@gmail.com</a></li>
                <li>Twitter: <a href="https://twitter.com/lucasvegap">@lucasvegap</a></li>
                <li>Instagram: <a href="https://www.instagram.com/lucas_vegap/">@lucas_vegap</a></li>
                <li>Repl.it: <a href="https://replit.com/@LucasVega777">@LucasVega777</a></li>
                <li>LinkedIn: <a href="https://www.linkedin.com/in/lucasmvegap/">Lucas Vega</a></li>
                <li>Github: <a href="https://github.com/LucasVega777">@LucasVega777</a></li>
            </ul>
        </footer>
        </body>
        </html>
        '''
        return HTMLResponse(content=html_content, status_code=200)
    else:
        return templates.TemplateResponse("search.html", {"request": request, "query": "No se encontro imagen"})

    # return templates.TemplateResponse("search.html", {"request": request, "query": query})

# Redirecciona la página principal a la página de búsqueda
@app.post("/", response_class=RedirectResponse)
async def home_redirect(query: str = Form(...)):
    return RedirectResponse(url=f"/search?query={query}")

