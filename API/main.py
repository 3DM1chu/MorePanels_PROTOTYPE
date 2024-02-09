from fastapi import FastAPI

from panelManager import PanelManager
from panels.panel import Panel


app = FastAPI()
panelManager = PanelManager()


@app.get("/panels")
def get_panels():
    return panelManager.getPanels()


@app.get("/add_panel")
def add_new_panel():
    panelManager.addPanel(Panel("PANEL1"))
    return panelManager.getPanels()


@app.get("/panel1")
def get_panel1():
    return panelManager.getPanels()[0].getPanel()


@app.get("/test")
def testgoogle():
    return "<iframe src=https://google.com></iframe>"
