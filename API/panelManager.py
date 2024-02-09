from typing import List

from panels.panel import Panel


class PanelManager:
    def __init__(self):
        self.panels: List[Panel] = []

    def addPanel(self, new_panel: Panel):
        self.panels.append(new_panel)

    def getPanels(self):
        return self.panels
