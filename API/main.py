from fastapi import FastAPI
from pydantic import BaseModel

from panelManager import PanelManager
from panels.panel import Panel


app = FastAPI()
i = 1

panelManager = PanelManager()


@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.get("/panels")
def get_panels():
    global i
    if i == 1:
        panelManager.addPanel(Panel("DASHBOARD " + str(i), "http://192.168.0.38:5000/"))
    else:
        panelManager.addPanel(Panel("DASHBOARD " + str(i), "http://localhost:4200"))
    i = i + 1
    print(panelManager.getPanels())
    return panelManager.getPanels()


@app.get("/panel1")
def get_panel1():
    return panelManager.getPanels()[0].getPanel()


class PanelPostBody(BaseModel):
    name: str
    url: str


@app.post("/panel")
def add_new_panel(panel: PanelPostBody):
    panelManager.addPanel(Panel(panel.name, panel.url))
    return panelManager.getPanels()


@app.delete("/panel")
def delete_panel(name: str):
    return {"message": f"TODO {name}"}
