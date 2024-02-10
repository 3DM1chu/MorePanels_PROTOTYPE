from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from panelManager import PanelManager
from panels.panel import Panel


app = FastAPI()
panelManager = PanelManager()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/panels")
def get_panels():
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
    return {'resp': 'OK'}


@app.delete("/panel")
def delete_panel(panelToRemove: PanelPostBody):
    panelManager.deletePanel(panelToRemove.name)
    return {"message": f"REMOVED {panelToRemove.name}"}
