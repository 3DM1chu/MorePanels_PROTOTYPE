from typing import List
from healthCheck import HealthCheck


class Panel:
    def __init__(self, name="DEFAULT_PANEL"):
        self.name = name
        self.health_checks: List[HealthCheck] = []

    def healthChecksCycle(self):
        for healthCheck in self.health_checks:
            healthCheck.check()

    def getPanel(self):
        # GET HTML FROM SERVICE
        return None
