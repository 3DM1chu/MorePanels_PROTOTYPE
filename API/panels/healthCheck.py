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
        self.status = Status()


class HealthCheck:
    def __init__(self, ip, port: int):
        self.service_to_check: ServiceToCheck = ServiceToCheck(ip, port)
        self.iframe_data = ""

    def setServiceToCheck(self, ip, port: int):
        self.service_to_check.ip = ip
        self.service_to_check.port = port

    def check(self):
        # DO PING AND GET HTML
        print(f"Testing {self.service_to_check.ip}:{self.service_to_check.port}...")
        self.iframe_data = "TODO"
        return self.iframe_data
