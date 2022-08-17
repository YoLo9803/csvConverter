from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Api():
    name: str
    statusCodes: Dict[str, int]

    def __init__(self, name: str, statusCode: str):
        self.name = name
        self.statusCodes = {}
        self.statusCodes[statusCode] = 1

    def addStatusCode(self, statusCode: str):
        self.statusCodes[statusCode] = 1

    def increaseStatusCodeCount(self, statusCode: str):
        self.statusCodes[statusCode] = self.statusCodes[statusCode] + 1