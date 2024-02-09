from typing import List


class Status:
    def __init__(self, status_code = 0):
        self.status_code = status_code

    def changeStatus(self, new_status: int):
        if self.status_code != new_status:
            # Possible events
            self.status_code = new_status


class ServiceToCheck:
    def __init__(self, ip, port: int):
        self.ip = ip
        self.port = port


class HealthCheck:
    def __init__(self):
        self.status = Status()
        self.services_to_check : List[ServiceToCheck] = []

    def addServiceToCheck(self, ip, port: int):
        self.services_to_check.append(ServiceToCheck(ip, port))

    def check(self):
        for service in self.services_to_check:
            # DO PING
            print(f"Testing {service.ip}:{service.port}...")
