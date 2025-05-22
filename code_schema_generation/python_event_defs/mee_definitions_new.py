from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class JusticeEvent:
    pass

@dataclass
class PersonnelEvent:
    pass

@dataclass
class BusinessEvent:
    pass

@dataclass
class ContactEvent:
    pass

@dataclass
class ConflictEvent:
    pass

@dataclass
class LifeEvent:
    pass

@dataclass
class MovementEvent:
    pass

@dataclass
class TransactionEvent:
    pass

@dataclass
class EndPosition(PersonnelEvent):
    def __init__(self, mention: Optional[str] = None, time: Optional[List] = None, entity: Optional[List] = None, position: Optional[List] = None, place: Optional[List] = None, person: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.time = time if time is not None else []
        self.entity = entity if entity is not None else []
        self.position = position if position is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
    def __repr__(self):
        return f"EndPosition(mention='{self.mention}', time={self.time}, entity={self.entity}, position={self.position}, place={self.place}, person={self.person})"

@dataclass
class StartPosition(PersonnelEvent):
    def __init__(self, mention: Optional[str] = None, time: Optional[List] = None, entity: Optional[List] = None, position: Optional[List] = None, place: Optional[List] = None, person: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.time = time if time is not None else []
        self.entity = entity if entity is not None else []
        self.position = position if position is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
    def __repr__(self):
        return f"StartPosition(mention='{self.mention}', time={self.time}, entity={self.entity}, position={self.position}, place={self.place}, person={self.person})"

@dataclass
class Die(LifeEvent):
    def __init__(self, mention: Optional[str] = None, time: Optional[List] = None, place: Optional[List] = None, instrument: Optional[List] = None, victim: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.time = time if time is not None else []
        self.place = place if place is not None else []
        self.instrument = instrument if instrument is not None else []
        self.victim = victim if victim is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Die(mention='{self.mention}', time={self.time}, place={self.place}, instrument={self.instrument}, victim={self.victim}, agent={self.agent})"

@dataclass
class Transport(MovementEvent):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, time: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.time = time if time is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Transport(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, time={self.time}, artifact={self.artifact}, destination={self.destination}, agent={self.agent})"

@dataclass
class STARTORG(BusinessEvent):
    def __init__(self, mention: Optional[str] = None, time: Optional[List] = None, organization: Optional[List] = None, place: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.time = time if time is not None else []
        self.organization = organization if organization is not None else []
        self.place = place if place is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"STARTORG(mention='{self.mention}', time={self.time}, organization={self.organization}, place={self.place}, agent={self.agent})"

@dataclass
class Attack(ConflictEvent):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, time: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.time = time if time is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Attack(mention='{self.mention}', target={self.target}, attacker={self.attacker}, time={self.time}, instrument={self.instrument}, place={self.place})"

@dataclass
class BeBorn(LifeEvent):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, person: Optional[List] = None, time: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
        self.time = time if time is not None else []
    def __repr__(self):
        return f"BeBorn(mention='{self.mention}', place={self.place}, person={self.person}, time={self.time})"

@dataclass
class TransferMoney(TransactionEvent):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, money: Optional[List] = None, time: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.money = money if money is not None else []
        self.time = time if time is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"TransferMoney(mention='{self.mention}', giver={self.giver}, money={self.money}, time={self.time}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class TransferOwnership(TransactionEvent):
    def __init__(self, mention: Optional[str] = None, time: Optional[List] = None, price: Optional[List] = None, artifact: Optional[List] = None, beneficiary: Optional[List] = None, buyer: Optional[List] = None, place: Optional[List] = None, seller: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.time = time if time is not None else []
        self.price = price if price is not None else []
        self.artifact = artifact if artifact is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.buyer = buyer if buyer is not None else []
        self.place = place if place is not None else []
        self.seller = seller if seller is not None else []
    def __repr__(self):
        return f"TransferOwnership(mention='{self.mention}', time={self.time}, price={self.price}, artifact={self.artifact}, beneficiary={self.beneficiary}, buyer={self.buyer}, place={self.place}, seller={self.seller})"

@dataclass
class Meet(ContactEvent):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, place: Optional[List] = None, time: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.place = place if place is not None else []
        self.time = time if time is not None else []
    def __repr__(self):
        return f"Meet(mention='{self.mention}', entity={self.entity}, place={self.place}, time={self.time})"

@dataclass
class Marry(LifeEvent):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, person: Optional[List] = None, time: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
        self.time = time if time is not None else []
    def __repr__(self):
        return f"Marry(mention='{self.mention}', place={self.place}, person={self.person}, time={self.time})"

@dataclass
class Demonstrate(ConflictEvent):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, place: Optional[List] = None, time: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.place = place if place is not None else []
        self.time = time if time is not None else []
    def __repr__(self):
        return f"Demonstrate(mention='{self.mention}', entity={self.entity}, place={self.place}, time={self.time})"

@dataclass
class Injure(LifeEvent):
    def __init__(self, mention: Optional[str] = None, time: Optional[List] = None, place: Optional[List] = None, instrument: Optional[List] = None, victim: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.time = time if time is not None else []
        self.place = place if place is not None else []
        self.instrument = instrument if instrument is not None else []
        self.victim = victim if victim is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Injure(mention='{self.mention}', time={self.time}, place={self.place}, instrument={self.instrument}, victim={self.victim}, agent={self.agent})"

@dataclass
class PhoneWrite(ContactEvent):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, time: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.time = time if time is not None else []
    def __repr__(self):
        return f"PhoneWrite(mention='{self.mention}', entity={self.entity}, time={self.time})"

@dataclass
class ArrestJail(JusticeEvent):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, time: Optional[List] = None, place: Optional[List] = None, person: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.time = time if time is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"ArrestJail(mention='{self.mention}', crime={self.crime}, time={self.time}, place={self.place}, person={self.person}, agent={self.agent})"

@dataclass
class Divorce(LifeEvent):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, person: Optional[List] = None, time: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.person = person if person is not None else []
        self.time = time if time is not None else []
    def __repr__(self):
        return f"Divorce(mention='{self.mention}', place={self.place}, person={self.person}, time={self.time})"

