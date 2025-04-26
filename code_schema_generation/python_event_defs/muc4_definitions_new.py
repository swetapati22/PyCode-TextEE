from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class Dummy(Event):
    def __init__(self, mention: Optional[str] = None, perpind: Optional[List] = None, target: Optional[List] = None, perporg: Optional[List] = None, weapon: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.perpind = perpind if perpind is not None else []
        self.target = target if target is not None else []
        self.perporg = perporg if perporg is not None else []
        self.weapon = weapon if weapon is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Dummy(mention='{self.mention}', perpind={self.perpind}, target={self.target}, perporg={self.perporg}, weapon={self.weapon}, victim={self.victim})"

