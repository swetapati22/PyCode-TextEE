from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class JusticeEvent:
    pass

@dataclass
class ContactEvent:
    pass

@dataclass
class MovementEvent:
    pass

@dataclass
class ConflictEvent:
    pass

@dataclass
class LifeEvent:
    pass

@dataclass
class TransactionEvent:
    pass

@dataclass
class Attack(ConflictEvent):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Attack(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class ArrestJail(JusticeEvent):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, person: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"ArrestJail(mention='{self.mention}', place={self.place}, person={self.person}, agent={self.agent})"

@dataclass
class Die(LifeEvent):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Die(mention='{self.mention}', victim={self.victim}, instrument={self.instrument}, place={self.place}, agent={self.agent})"

@dataclass
class PhoneWrite(ContactEvent):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"PhoneWrite(mention='{self.mention}', entity={self.entity}, place={self.place})"

@dataclass
class Meet(ContactEvent):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Meet(mention='{self.mention}', entity={self.entity}, place={self.place})"

@dataclass
class Transport(MovementEvent):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Transport(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, agent={self.agent})"

@dataclass
class TransferMoney(TransactionEvent):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"TransferMoney(mention='{self.mention}', giver={self.giver}, recipient={self.recipient})"

@dataclass
class Demonstrate(ConflictEvent):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, place: Optional[List] = None, police: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.place = place if place is not None else []
        self.police = police if police is not None else []
    def __repr__(self):
        return f"Demonstrate(mention='{self.mention}', entity={self.entity}, place={self.place}, police={self.police})"

