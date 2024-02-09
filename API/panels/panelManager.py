from panel import Panel


class PanelManager:
    def __init__(self):
        self.panels = []

    def addPanel(self, new_panel: Panel):
        self.panels.append(new_panel)

    def getPanels(self):
        return self.panels
