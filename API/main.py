import json

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from panelManager import PanelManager
from panels.panel import Panel


panelManager = PanelManager()


def loadPanels():
    with open("panels.json", "r") as file:
        panels_from_file = json.loads(file.read())["panels"]
        for panel in panels_from_file:
            panelManager.addPanel(Panel(panel["name"], panel["url"]))


def savePanels():
    for panel in panelManager.panels:
        with open("panels.json", "w") as file:
            panels_to_json = {"panels": []}
            panels_to_json["panels"].append({"name": panel.name, "url": panel.url})
            file.write(json.dumps(panels_to_json, indent=4))


loadPanels()

origins = [
    "http://localhost:3000",
]

app = FastAPI()
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
    savePanels()
    return {'resp': 'OK'}


@app.delete("/panel")
def delete_panel(panelToRemove: PanelPostBody):
    panelManager.deletePanel(panelToRemove.name)
    savePanels()
    return {"message": f"REMOVED {panelToRemove.name}"}
