from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class government_agreements_violateagreement(Event):
    def __init__(self, mention: Optional[str] = None, violator: Optional[List] = None, place: Optional[List] = None, otherparticipant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.violator = violator if violator is not None else []
        self.place = place if place is not None else []
        self.otherparticipant = otherparticipant if otherparticipant is not None else []
    def __repr__(self):
        return f"government_agreements_violateagreement(mention='{self.mention}', violator={self.violator}, place={self.place}, otherparticipant={self.otherparticipant})"

@dataclass
class personnel_elect_Na(Event):
    def __init__(self, mention: Optional[str] = None, voter: Optional[List] = None, candidate: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.voter = voter if voter is not None else []
        self.candidate = candidate if candidate is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"personnel_elect_Na(mention='{self.mention}', voter={self.voter}, candidate={self.candidate}, place={self.place})"

@dataclass
class movement_transportperson_preventexit(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, preventer: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.preventer = preventer if preventer is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_preventexit(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, preventer={self.preventer}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class personnel_endposition_firinglayoff(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, place: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.place = place if place is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"personnel_endposition_firinglayoff(mention='{self.mention}', placeofemployment={self.placeofemployment}, place={self.place}, employee={self.employee})"

@dataclass
class movement_transportperson_hide(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, hidingplace: Optional[List] = None, vehicle: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.hidingplace = hidingplace if hidingplace is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_hide(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, hidingplace={self.hidingplace}, vehicle={self.vehicle}, transporter={self.transporter})"

@dataclass
class contact_commitmentpromiseexpressintent_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commitmentpromiseexpressintent_correspondence(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class justice_judicialconsequences_Na(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_judicialconsequences_Na(mention='{self.mention}', crime={self.crime}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class transaction_transferownership_purchase(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, artifact: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.artifact = artifact if artifact is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transferownership_purchase(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, artifact={self.artifact}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class contact_commitmentpromiseexpressintent_meet(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commitmentpromiseexpressintent_meet(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class personnel_endposition_Na(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, place: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.place = place if place is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"personnel_endposition_Na(mention='{self.mention}', placeofemployment={self.placeofemployment}, place={self.place}, employee={self.employee})"

@dataclass
class contact_discussion_Na(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_discussion_Na(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class contact_commandorder_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commandorder_correspondence(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class contact_threatencoerce_meet(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_threatencoerce_meet(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class conflict_attack_Na(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_Na(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class justice_initiatejudicialprocess_chargeindict(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, prosecutor: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.prosecutor = prosecutor if prosecutor is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_initiatejudicialprocess_chargeindict(mention='{self.mention}', crime={self.crime}, prosecutor={self.prosecutor}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class contact_prevarication_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_prevarication_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class justice_investigate_investigatecrime(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, investigator: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.investigator = investigator if investigator is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_investigate_investigatecrime(mention='{self.mention}', crime={self.crime}, investigator={self.investigator}, defendant={self.defendant}, place={self.place})"

@dataclass
class transaction_transfermoney_payforservice(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, money: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.money = money if money is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transfermoney_payforservice(mention='{self.mention}', giver={self.giver}, money={self.money}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class justice_arrestjaildetain_arrestjaildetain(Event):
    def __init__(self, mention: Optional[str] = None, jailer: Optional[List] = None, crime: Optional[List] = None, place: Optional[List] = None, detainee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.jailer = jailer if jailer is not None else []
        self.crime = crime if crime is not None else []
        self.place = place if place is not None else []
        self.detainee = detainee if detainee is not None else []
    def __repr__(self):
        return f"justice_arrestjaildetain_arrestjaildetain(mention='{self.mention}', jailer={self.jailer}, crime={self.crime}, place={self.place}, detainee={self.detainee})"

@dataclass
class conflict_attack_selfdirectedbattle(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_selfdirectedbattle(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class inspection_sensoryobserve_physicalinvestigateinspect(Event):
    def __init__(self, mention: Optional[str] = None, inspector: Optional[List] = None, place: Optional[List] = None, inspectedentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.inspector = inspector if inspector is not None else []
        self.place = place if place is not None else []
        self.inspectedentity = inspectedentity if inspectedentity is not None else []
    def __repr__(self):
        return f"inspection_sensoryobserve_physicalinvestigateinspect(mention='{self.mention}', inspector={self.inspector}, place={self.place}, inspectedentity={self.inspectedentity})"

@dataclass
class life_die_Na(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"life_die_Na(mention='{self.mention}', victim={self.victim}, place={self.place})"

@dataclass
class contact_commandorder_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commandorder_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class movement_transportartifact_Na(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_Na(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class life_injure_illnessdegradationhungerthirst(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"life_injure_illnessdegradationhungerthirst(mention='{self.mention}', victim={self.victim}, place={self.place})"

@dataclass
class life_injure_illnessdegradationphysical(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"life_injure_illnessdegradationphysical(mention='{self.mention}', victim={self.victim})"

@dataclass
class conflict_demonstrate_Na(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, demonstrator: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.demonstrator = demonstrator if demonstrator is not None else []
    def __repr__(self):
        return f"conflict_demonstrate_Na(mention='{self.mention}', place={self.place}, demonstrator={self.demonstrator})"

@dataclass
class contact_threatencoerce_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_threatencoerce_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class transaction_transfermoney_Na(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, money: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.money = money if money is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transfermoney_Na(mention='{self.mention}', giver={self.giver}, money={self.money}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class transaction_transaction_embargosanction(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, preventer: Optional[List] = None, place: Optional[List] = None, artifactmoney: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.preventer = preventer if preventer is not None else []
        self.place = place if place is not None else []
        self.artifactmoney = artifactmoney if artifactmoney is not None else []
    def __repr__(self):
        return f"transaction_transaction_embargosanction(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, preventer={self.preventer}, place={self.place}, artifactmoney={self.artifactmoney})"

@dataclass
class contact_funeralvigil_meet(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, deceased: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.deceased = deceased if deceased is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_funeralvigil_meet(mention='{self.mention}', participant={self.participant}, deceased={self.deceased}, place={self.place})"

@dataclass
class conflict_attack_bombing(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_bombing(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class disaster_fireexplosion_fireexplosion(Event):
    def __init__(self, mention: Optional[str] = None, instrument: Optional[List] = None, place: Optional[List] = None, fireexplosionobject: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
        self.fireexplosionobject = fireexplosionobject if fireexplosionobject is not None else []
    def __repr__(self):
        return f"disaster_fireexplosion_fireexplosion(mention='{self.mention}', instrument={self.instrument}, place={self.place}, fireexplosionobject={self.fireexplosionobject})"

@dataclass
class government_agreements_acceptagreementcontractceasefire(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_agreements_acceptagreementcontractceasefire(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class movement_transportperson_smuggleextract(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, vehicle: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_smuggleextract(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, vehicle={self.vehicle}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class government_agreements_rejectnullifyagreementcontractceasefire(Event):
    def __init__(self, mention: Optional[str] = None, rejecternullifier: Optional[List] = None, place: Optional[List] = None, otherparticipant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.rejecternullifier = rejecternullifier if rejecternullifier is not None else []
        self.place = place if place is not None else []
        self.otherparticipant = otherparticipant if otherparticipant is not None else []
    def __repr__(self):
        return f"government_agreements_rejectnullifyagreementcontractceasefire(mention='{self.mention}', rejecternullifier={self.rejecternullifier}, place={self.place}, otherparticipant={self.otherparticipant})"

@dataclass
class contact_requestadvise_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_requestadvise_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class government_legislate_legislate(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, law: Optional[List] = None, governmentbody: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.law = law if law is not None else []
        self.governmentbody = governmentbody if governmentbody is not None else []
    def __repr__(self):
        return f"government_legislate_legislate(mention='{self.mention}', place={self.place}, law={self.law}, governmentbody={self.governmentbody})"

@dataclass
class manufacture_artifact_createmanufacture(Event):
    def __init__(self, mention: Optional[str] = None, manufacturer: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.manufacturer = manufacturer if manufacturer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"manufacture_artifact_createmanufacture(mention='{self.mention}', manufacturer={self.manufacturer}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class life_injure_injurycausedbyviolentevents(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None, injurer: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
        self.injurer = injurer if injurer is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"life_injure_injurycausedbyviolentevents(mention='{self.mention}', victim={self.victim}, injurer={self.injurer}, instrument={self.instrument}, place={self.place})"

@dataclass
class life_injure_Na(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, victim: Optional[List] = None, injurer: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.victim = victim if victim is not None else []
        self.injurer = injurer if injurer is not None else []
    def __repr__(self):
        return f"life_injure_Na(mention='{self.mention}', place={self.place}, victim={self.victim}, injurer={self.injurer})"

@dataclass
class government_spy_spy(Event):
    def __init__(self, mention: Optional[str] = None, spy: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None, observedentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.spy = spy if spy is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
        self.observedentity = observedentity if observedentity is not None else []
    def __repr__(self):
        return f"government_spy_spy(mention='{self.mention}', spy={self.spy}, beneficiary={self.beneficiary}, place={self.place}, observedentity={self.observedentity})"

@dataclass
class transaction_transfermoney_embargosanction(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, money: Optional[List] = None, recipient: Optional[List] = None, preventer: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.money = money if money is not None else []
        self.recipient = recipient if recipient is not None else []
        self.preventer = preventer if preventer is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transfermoney_embargosanction(mention='{self.mention}', giver={self.giver}, money={self.money}, recipient={self.recipient}, preventer={self.preventer}, place={self.place})"

@dataclass
class contact_commandorder_meet(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commandorder_meet(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class justice_initiatejudicialprocess_trialhearing(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, prosecutor: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.prosecutor = prosecutor if prosecutor is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_initiatejudicialprocess_trialhearing(mention='{self.mention}', crime={self.crime}, prosecutor={self.prosecutor}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class personnel_startposition_hiring(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, place: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.place = place if place is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"personnel_startposition_hiring(mention='{self.mention}', placeofemployment={self.placeofemployment}, place={self.place}, employee={self.employee})"

@dataclass
class contact_discussion_meet(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_discussion_meet(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class conflict_yield_surrender(Event):
    def __init__(self, mention: Optional[str] = None, surrenderer: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.surrenderer = surrenderer if surrenderer is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"conflict_yield_surrender(mention='{self.mention}', surrenderer={self.surrenderer}, place={self.place}, recipient={self.recipient})"

@dataclass
class movement_transportperson_evacuationrescue(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, vehicle: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_evacuationrescue(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, vehicle={self.vehicle}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class life_die_deathcausedbyviolentevents(Event):
    def __init__(self, mention: Optional[str] = None, killer: Optional[List] = None, victim: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.killer = killer if killer is not None else []
        self.victim = victim if victim is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"life_die_deathcausedbyviolentevents(mention='{self.mention}', killer={self.killer}, victim={self.victim}, instrument={self.instrument}, place={self.place})"

@dataclass
class transaction_transferownership_embargosanction(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, preventer: Optional[List] = None, artifact: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.preventer = preventer if preventer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transferownership_embargosanction(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, preventer={self.preventer}, artifact={self.artifact}, place={self.place})"

@dataclass
class manufacture_artifact_Na(Event):
    def __init__(self, mention: Optional[str] = None, manufacturer: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.manufacturer = manufacturer if manufacturer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"manufacture_artifact_Na(mention='{self.mention}', manufacturer={self.manufacturer}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class inspection_sensoryobserve_Na(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, observer: Optional[List] = None, observedentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.observer = observer if observer is not None else []
        self.observedentity = observedentity if observedentity is not None else []
    def __repr__(self):
        return f"inspection_sensoryobserve_Na(mention='{self.mention}', place={self.place}, observer={self.observer}, observedentity={self.observedentity})"

@dataclass
class transaction_transaction_transfercontrol(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, territoryorfacility: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.territoryorfacility = territoryorfacility if territoryorfacility is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transaction_transfercontrol(mention='{self.mention}', giver={self.giver}, territoryorfacility={self.territoryorfacility}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class movement_transportperson_Na(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, vehicle: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_Na(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, vehicle={self.vehicle}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class artifactexistence_damagedestroy_destroy(Event):
    def __init__(self, mention: Optional[str] = None, destroyer: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.destroyer = destroyer if destroyer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"artifactexistence_damagedestroy_destroy(mention='{self.mention}', destroyer={self.destroyer}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class contact_threatencoerce_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_threatencoerce_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class transaction_transaction_giftgrantprovideaid(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transaction_giftgrantprovideaid(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class contact_funeralvigil_Na(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, deceased: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.deceased = deceased if deceased is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_funeralvigil_Na(mention='{self.mention}', participant={self.participant}, deceased={self.deceased}, place={self.place})"

@dataclass
class contact_publicstatementinperson_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_publicstatementinperson_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class inspection_sensoryobserve_monitorelection(Event):
    def __init__(self, mention: Optional[str] = None, monitor: Optional[List] = None, place: Optional[List] = None, monitoredentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.monitor = monitor if monitor is not None else []
        self.place = place if place is not None else []
        self.monitoredentity = monitoredentity if monitoredentity is not None else []
    def __repr__(self):
        return f"inspection_sensoryobserve_monitorelection(mention='{self.mention}', monitor={self.monitor}, place={self.place}, monitoredentity={self.monitoredentity})"

@dataclass
class movement_transportperson_fall(Event):
    def __init__(self, mention: Optional[str] = None, passenger: Optional[List] = None, destination: Optional[List] = None, origin: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.passenger = passenger if passenger is not None else []
        self.destination = destination if destination is not None else []
        self.origin = origin if origin is not None else []
    def __repr__(self):
        return f"movement_transportperson_fall(mention='{self.mention}', passenger={self.passenger}, destination={self.destination}, origin={self.origin})"

@dataclass
class justice_judicialconsequences_execute(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, executioner: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.executioner = executioner if executioner is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_judicialconsequences_execute(mention='{self.mention}', crime={self.crime}, executioner={self.executioner}, defendant={self.defendant}, place={self.place})"

@dataclass
class transaction_transfermoney_borrowlend(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, money: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.money = money if money is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transfermoney_borrowlend(mention='{self.mention}', giver={self.giver}, money={self.money}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class contact_requestadvise_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_requestadvise_correspondence(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class artifactexistence_damagedestroy_damage(Event):
    def __init__(self, mention: Optional[str] = None, damager: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.damager = damager if damager is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"artifactexistence_damagedestroy_damage(mention='{self.mention}', damager={self.damager}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class conflict_attack_airstrikemissilestrike(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_airstrikemissilestrike(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class transaction_transaction_Na(Event):
    def __init__(self, mention: Optional[str] = None, beneficiary: Optional[List] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transaction_Na(mention='{self.mention}', beneficiary={self.beneficiary}, participant={self.participant}, place={self.place})"

@dataclass
class contact_prevarication_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_prevarication_correspondence(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class contact_commitmentpromiseexpressintent_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commitmentpromiseexpressintent_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class contact_negotiate_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_negotiate_correspondence(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class conflict_attack_hanging(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_hanging(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class contact_commandorder_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commandorder_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class transaction_transferownership_Na(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, artifact: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.artifact = artifact if artifact is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transferownership_Na(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, artifact={self.artifact}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class movement_transportartifact_grantentry(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_grantentry(mention='{self.mention}', origin={self.origin}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class contact_collaborate_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_collaborate_correspondence(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class movement_transportartifact_disperseseparate(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_disperseseparate(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class government_formation_Na(Event):
    def __init__(self, mention: Optional[str] = None, founder: Optional[List] = None, gpe: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.founder = founder if founder is not None else []
        self.gpe = gpe if gpe is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_formation_Na(mention='{self.mention}', founder={self.founder}, gpe={self.gpe}, place={self.place})"

@dataclass
class contact_requestadvise_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_requestadvise_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class transaction_transfermoney_giftgrantprovideaid(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, money: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.money = money if money is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transfermoney_giftgrantprovideaid(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, money={self.money}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class movement_transportartifact_preventexit(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, preventer: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.preventer = preventer if preventer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_preventexit(mention='{self.mention}', origin={self.origin}, preventer={self.preventer}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class government_vote_Na(Event):
    def __init__(self, mention: Optional[str] = None, voter: Optional[List] = None, result: Optional[List] = None, ballot: Optional[List] = None, candidate: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.voter = voter if voter is not None else []
        self.result = result if result is not None else []
        self.ballot = ballot if ballot is not None else []
        self.candidate = candidate if candidate is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_vote_Na(mention='{self.mention}', voter={self.voter}, result={self.result}, ballot={self.ballot}, candidate={self.candidate}, place={self.place})"

@dataclass
class transaction_transfermoney_purchase(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, money: Optional[List] = None, recipient: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.money = money if money is not None else []
        self.recipient = recipient if recipient is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transfermoney_purchase(mention='{self.mention}', giver={self.giver}, money={self.money}, recipient={self.recipient}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class movement_transportperson_grantentryasylum(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, granter: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.granter = granter if granter is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_grantentryasylum(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, granter={self.granter}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class government_vote_violationspreventvote(Event):
    def __init__(self, mention: Optional[str] = None, voter: Optional[List] = None, preventer: Optional[List] = None, ballot: Optional[List] = None, candidate: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.voter = voter if voter is not None else []
        self.preventer = preventer if preventer is not None else []
        self.ballot = ballot if ballot is not None else []
        self.candidate = candidate if candidate is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_vote_violationspreventvote(mention='{self.mention}', voter={self.voter}, preventer={self.preventer}, ballot={self.ballot}, candidate={self.candidate}, place={self.place})"

@dataclass
class transaction_transferownership_borrowlend(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, artifact: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.artifact = artifact if artifact is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transferownership_borrowlend(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, artifact={self.artifact}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class personnel_startposition_Na(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, place: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.place = place if place is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"personnel_startposition_Na(mention='{self.mention}', placeofemployment={self.placeofemployment}, place={self.place}, employee={self.employee})"

@dataclass
class contact_collaborate_meet(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_collaborate_meet(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class contact_discussion_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_discussion_correspondence(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class contact_mediastatement_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_mediastatement_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class justice_judicialconsequences_extradite(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, crime: Optional[List] = None, extraditer: Optional[List] = None, defendant: Optional[List] = None, destination: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.crime = crime if crime is not None else []
        self.extraditer = extraditer if extraditer is not None else []
        self.defendant = defendant if defendant is not None else []
        self.destination = destination if destination is not None else []
    def __repr__(self):
        return f"justice_judicialconsequences_extradite(mention='{self.mention}', origin={self.origin}, crime={self.crime}, extraditer={self.extraditer}, defendant={self.defendant}, destination={self.destination})"

@dataclass
class contact_prevarication_meet(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_prevarication_meet(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class justice_investigate_Na(Event):
    def __init__(self, mention: Optional[str] = None, investigator: Optional[List] = None, place: Optional[List] = None, defendant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.investigator = investigator if investigator is not None else []
        self.place = place if place is not None else []
        self.defendant = defendant if defendant is not None else []
    def __repr__(self):
        return f"justice_investigate_Na(mention='{self.mention}', investigator={self.investigator}, place={self.place}, defendant={self.defendant})"

@dataclass
class contact_negotiate_meet(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_negotiate_meet(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class artifactexistence_damagedestroy_Na(Event):
    def __init__(self, mention: Optional[str] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None, damagerdestroyer: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
        self.damagerdestroyer = damagerdestroyer if damagerdestroyer is not None else []
    def __repr__(self):
        return f"artifactexistence_damagedestroy_Na(mention='{self.mention}', artifact={self.artifact}, instrument={self.instrument}, place={self.place}, damagerdestroyer={self.damagerdestroyer})"

@dataclass
class contact_threatencoerce_correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_threatencoerce_correspondence(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class movement_transportperson_selfmotion(Event):
    def __init__(self, mention: Optional[str] = None, destination: Optional[List] = None, transporter: Optional[List] = None, origin: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
        self.origin = origin if origin is not None else []
    def __repr__(self):
        return f"movement_transportperson_selfmotion(mention='{self.mention}', destination={self.destination}, transporter={self.transporter}, origin={self.origin})"

@dataclass
class life_die_nonviolentdeath(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"life_die_nonviolentdeath(mention='{self.mention}', victim={self.victim}, place={self.place})"

@dataclass
class personnel_endposition_quitretire(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, place: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.place = place if place is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"personnel_endposition_quitretire(mention='{self.mention}', placeofemployment={self.placeofemployment}, place={self.place}, employee={self.employee})"

@dataclass
class movement_transportartifact_receiveimport(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_receiveimport(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class contact_publicstatementinperson_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_publicstatementinperson_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class contact_commitmentpromiseexpressintent_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_commitmentpromiseexpressintent_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class movement_transportartifact_prevententry(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, preventer: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.preventer = preventer if preventer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_prevententry(mention='{self.mention}', origin={self.origin}, preventer={self.preventer}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class contact_mediastatement_broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_mediastatement_broadcast(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class contact_prevarication_Na(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_prevarication_Na(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class contact_collaborate_Na(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_collaborate_Na(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class movement_transportartifact_smuggleextract(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_smuggleextract(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class manufacture_artifact_build(Event):
    def __init__(self, mention: Optional[str] = None, manufacturer: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.manufacturer = manufacturer if manufacturer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"manufacture_artifact_build(mention='{self.mention}', manufacturer={self.manufacturer}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class conflict_attack_invade(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_invade(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class movement_transportperson_disperseseparate(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, vehicle: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_disperseseparate(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, vehicle={self.vehicle}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class inspection_sensoryobserve_inspectpeopleorganization(Event):
    def __init__(self, mention: Optional[str] = None, inspector: Optional[List] = None, place: Optional[List] = None, inspectedentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.inspector = inspector if inspector is not None else []
        self.place = place if place is not None else []
        self.inspectedentity = inspectedentity if inspectedentity is not None else []
    def __repr__(self):
        return f"inspection_sensoryobserve_inspectpeopleorganization(mention='{self.mention}', inspector={self.inspector}, place={self.place}, inspectedentity={self.inspectedentity})"

@dataclass
class justice_initiatejudicialprocess_Na(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, prosecutor: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.prosecutor = prosecutor if prosecutor is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_initiatejudicialprocess_Na(mention='{self.mention}', crime={self.crime}, prosecutor={self.prosecutor}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class government_vote_castvote(Event):
    def __init__(self, mention: Optional[str] = None, voter: Optional[List] = None, result: Optional[List] = None, ballot: Optional[List] = None, candidate: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.voter = voter if voter is not None else []
        self.result = result if result is not None else []
        self.ballot = ballot if ballot is not None else []
        self.candidate = candidate if candidate is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_vote_castvote(mention='{self.mention}', voter={self.voter}, result={self.result}, ballot={self.ballot}, candidate={self.candidate}, place={self.place})"

@dataclass
class movement_transportartifact_sendsupplyexport(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_sendsupplyexport(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class conflict_attack_stabbing(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_stabbing(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class disaster_accidentcrash_accidentcrash(Event):
    def __init__(self, mention: Optional[str] = None, driverpassenger: Optional[List] = None, vehicle: Optional[List] = None, crashobject: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.driverpassenger = driverpassenger if driverpassenger is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.crashobject = crashobject if crashobject is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"disaster_accidentcrash_accidentcrash(mention='{self.mention}', driverpassenger={self.driverpassenger}, vehicle={self.vehicle}, crashobject={self.crashobject}, place={self.place})"

@dataclass
class movement_transportartifact_nonviolentthrowlaunch(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_nonviolentthrowlaunch(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class contact_requestadvise_meet(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"contact_requestadvise_meet(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class government_agreements_Na(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_agreements_Na(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class personnel_elect_winelection(Event):
    def __init__(self, mention: Optional[str] = None, voter: Optional[List] = None, candidate: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.voter = voter if voter is not None else []
        self.candidate = candidate if candidate is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"personnel_elect_winelection(mention='{self.mention}', voter={self.voter}, candidate={self.candidate}, place={self.place})"

@dataclass
class transaction_transferownership_giftgrantprovideaid(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, recipient: Optional[List] = None, artifact: Optional[List] = None, beneficiary: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.artifact = artifact if artifact is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"transaction_transferownership_giftgrantprovideaid(mention='{self.mention}', giver={self.giver}, recipient={self.recipient}, artifact={self.artifact}, beneficiary={self.beneficiary}, place={self.place})"

@dataclass
class movement_transportartifact_hide(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, hidingplace: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.hidingplace = hidingplace if hidingplace is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_hide(mention='{self.mention}', origin={self.origin}, hidingplace={self.hidingplace}, vehicle={self.vehicle}, artifact={self.artifact}, transporter={self.transporter})"

@dataclass
class movement_transportperson_prevententry(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, preventer: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.preventer = preventer if preventer is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_prevententry(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, preventer={self.preventer}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class conflict_yield_Na(Event):
    def __init__(self, mention: Optional[str] = None, yielder: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.yielder = yielder if yielder is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"conflict_yield_Na(mention='{self.mention}', yielder={self.yielder}, place={self.place}, recipient={self.recipient})"

@dataclass
class government_formation_startgpe(Event):
    def __init__(self, mention: Optional[str] = None, founder: Optional[List] = None, gpe: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.founder = founder if founder is not None else []
        self.gpe = gpe if gpe is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_formation_startgpe(mention='{self.mention}', founder={self.founder}, gpe={self.gpe}, place={self.place})"

@dataclass
class contact_negotiate_Na(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"contact_negotiate_Na(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class movement_transportperson_bringcarryunload(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passenger: Optional[List] = None, vehicle: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passenger = passenger if passenger is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportperson_bringcarryunload(mention='{self.mention}', origin={self.origin}, passenger={self.passenger}, vehicle={self.vehicle}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class justice_judicialconsequences_convict(Event):
    def __init__(self, mention: Optional[str] = None, crime: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crime = crime if crime is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"justice_judicialconsequences_convict(mention='{self.mention}', crime={self.crime}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class conflict_attack_setfire(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_setfire(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class conflict_attack_stealrobhijack(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_stealrobhijack(mention='{self.mention}', target={self.target}, attacker={self.attacker}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class conflict_yield_retreat(Event):
    def __init__(self, mention: Optional[str] = None, destination: Optional[List] = None, retreater: Optional[List] = None, origin: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.destination = destination if destination is not None else []
        self.retreater = retreater if retreater is not None else []
        self.origin = origin if origin is not None else []
    def __repr__(self):
        return f"conflict_yield_retreat(mention='{self.mention}', destination={self.destination}, retreater={self.retreater}, origin={self.origin})"

@dataclass
class conflict_attack_biologicalchemicalpoisonattack(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_biologicalchemicalpoisonattack(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class conflict_attack_strangling(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_strangling(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class movement_transportartifact_fall(Event):
    def __init__(self, mention: Optional[str] = None, destination: Optional[List] = None, origin: Optional[List] = None, artifact: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.destination = destination if destination is not None else []
        self.origin = origin if origin is not None else []
        self.artifact = artifact if artifact is not None else []
    def __repr__(self):
        return f"movement_transportartifact_fall(mention='{self.mention}', destination={self.destination}, origin={self.origin}, artifact={self.artifact})"

@dataclass
class manufacture_artifact_createintellectualproperty(Event):
    def __init__(self, mention: Optional[str] = None, manufacturer: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.manufacturer = manufacturer if manufacturer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"manufacture_artifact_createintellectualproperty(mention='{self.mention}', manufacturer={self.manufacturer}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class conflict_demonstrate_marchprotestpoliticalgathering(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, demonstrator: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.demonstrator = demonstrator if demonstrator is not None else []
    def __repr__(self):
        return f"conflict_demonstrate_marchprotestpoliticalgathering(mention='{self.mention}', place={self.place}, demonstrator={self.demonstrator})"

@dataclass
class government_formation_mergegpe(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"government_formation_mergegpe(mention='{self.mention}', participant={self.participant}, place={self.place})"

@dataclass
class conflict_attack_firearmattack(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"conflict_attack_firearmattack(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class movement_transportartifact_bringcarryunload(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, artifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.artifact = artifact if artifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"movement_transportartifact_bringcarryunload(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, artifact={self.artifact}, destination={self.destination}, transporter={self.transporter})"

