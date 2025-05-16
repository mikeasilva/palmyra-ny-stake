from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    program_template = "general.html"
    #program_template = "redirect.html"
    program_template = "adult.html"
    #program_template = "leadership.html"
    return templates.TemplateResponse(program_template, {"request": request})

@app.get("/conference/program/{meeting}", response_class=HTMLResponse)
def stake_conference_program(request: Request, meeting: str):
    if meeting == "sunday":
        program_template = "general.html"
    elif meeting == "leadership":
        program_template = "leadership.html"
    else:
        program_template = "adult.html"

    return templates.TemplateResponse(program_template, {"request": request})


"""
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
#"""
