from fastapi import FastAPI, Request
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    df = pd.read_csv('wellness_dataset.csv')
    print(df)
    print(df.iloc[1][1])
    return templates.TemplateResponse("test.html", {"request": request, "data": df.iloc[1][1]})
