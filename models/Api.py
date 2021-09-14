from dataclasses import dataclass, field
from typing import List

@dataclass
class Api():
    name: str
    statusCodes: List[str]

    def __init__(self, name: str, statusCode: str):
        self.name = name                                    
        self.statusCodes = []
        self.statusCodes.append(statusCode)

    def addStatusCode(self, statusCode: str):
        self.statusCodes.append(statusCode)