from panels.healthCheck import HealthCheck


class Panel():
    def __init__(self, name="DEFAULT_PANEL", url="localhost"):
        self.name = name
        self.url = url
        self.health_check: HealthCheck = HealthCheck("", 0)

    def getPanel(self):
        # GET HTML FROM SERVICE
        return self.health_check.check()
