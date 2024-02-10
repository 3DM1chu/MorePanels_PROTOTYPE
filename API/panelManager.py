from typing import List

from panels.panel import Panel


class PanelManager:
    def __init__(self):
        self.panels: List[Panel] = []

    def addPanel(self, new_panel: Panel):
        self.panels.append(new_panel)

    def deletePanel(self, panelName: str):
        panelToDelete = None
        for panel in self.panels:
            if panel.name == panelName:
                panelToDelete = panel
                break
        if panelToDelete is not None:
            self.panels.remove(panelToDelete)

    def getPanels(self):
        return {"panels": self.panels}
