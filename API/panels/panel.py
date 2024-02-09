from panels.healthCheck import HealthCheck


class Panel:
    def __init__(self, name="DEFAULT_PANEL"):
        self.name = name
        self.health_check: HealthCheck = HealthCheck("", 0)

    def getPanel(self):
        # GET HTML FROM SERVICE
        return self.health_check.check()
