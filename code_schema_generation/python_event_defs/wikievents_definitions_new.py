from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class Movement_Transportation_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, passengerartifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.passengerartifact = passengerartifact if passengerartifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"Movement_Transportation_Unspecified(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, passengerartifact={self.passengerartifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class Life_Die_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, killer: Optional[List] = None, victim: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.killer = killer if killer is not None else []
        self.victim = victim if victim is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Life_Die_Unspecified(mention='{self.mention}', killer={self.killer}, victim={self.victim}, place={self.place})"

@dataclass
class Life_Infect_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Life_Infect_Unspecified(mention='{self.mention}', victim={self.victim})"

@dataclass
class Cognitive_Inspection_SensoryObserve(Event):
    def __init__(self, mention: Optional[str] = None, observer: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None, observedentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.observer = observer if observer is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
        self.observedentity = observedentity if observedentity is not None else []
    def __repr__(self):
        return f"Cognitive_Inspection_SensoryObserve(mention='{self.mention}', observer={self.observer}, instrument={self.instrument}, place={self.place}, observedentity={self.observedentity})"

@dataclass
class Contact_Contact_Broadcast(Event):
    def __init__(self, mention: Optional[str] = None, recipient: Optional[List] = None, communicator: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.recipient = recipient if recipient is not None else []
        self.communicator = communicator if communicator is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Contact_Contact_Broadcast(mention='{self.mention}', recipient={self.recipient}, communicator={self.communicator}, instrument={self.instrument}, place={self.place}, topic={self.topic})"

@dataclass
class Justice_ChargeIndict_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, prosecutor: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.prosecutor = prosecutor if prosecutor is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Justice_ChargeIndict_Unspecified(mention='{self.mention}', prosecutor={self.prosecutor}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class Conflict_Attack_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Conflict_Attack_Unspecified(mention='{self.mention}', target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class Conflict_Attack_DetonateExplode(Event):
    def __init__(self, mention: Optional[str] = None, explosivedevice: Optional[List] = None, target: Optional[List] = None, attacker: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.explosivedevice = explosivedevice if explosivedevice is not None else []
        self.target = target if target is not None else []
        self.attacker = attacker if attacker is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Conflict_Attack_DetonateExplode(mention='{self.mention}', explosivedevice={self.explosivedevice}, target={self.target}, attacker={self.attacker}, instrument={self.instrument}, place={self.place})"

@dataclass
class ArtifactExistence_DamageDestroyDisableDismantle_Destroy(Event):
    def __init__(self, mention: Optional[str] = None, destroyer: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.destroyer = destroyer if destroyer is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"ArtifactExistence_DamageDestroyDisableDismantle_Destroy(mention='{self.mention}', destroyer={self.destroyer}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class Life_Injure_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, bodypart: Optional[List] = None, injurer: Optional[List] = None, instrument: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.bodypart = bodypart if bodypart is not None else []
        self.injurer = injurer if injurer is not None else []
        self.instrument = instrument if instrument is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Life_Injure_Unspecified(mention='{self.mention}', bodypart={self.bodypart}, injurer={self.injurer}, instrument={self.instrument}, victim={self.victim})"

@dataclass
class Justice_TrialHearing_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, prosecutor: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.prosecutor = prosecutor if prosecutor is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Justice_TrialHearing_Unspecified(mention='{self.mention}', prosecutor={self.prosecutor}, judgecourt={self.judgecourt}, defendant={self.defendant}, place={self.place})"

@dataclass
class Justice_ArrestJailDetain_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, jailer: Optional[List] = None, place: Optional[List] = None, detainee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.jailer = jailer if jailer is not None else []
        self.place = place if place is not None else []
        self.detainee = detainee if detainee is not None else []
    def __repr__(self):
        return f"Justice_ArrestJailDetain_Unspecified(mention='{self.mention}', jailer={self.jailer}, place={self.place}, detainee={self.detainee})"

@dataclass
class Justice_ReleaseParole_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
    def __repr__(self):
        return f"Justice_ReleaseParole_Unspecified(mention='{self.mention}', judgecourt={self.judgecourt}, defendant={self.defendant})"

@dataclass
class Contact_Contact_Meet(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Contact_Contact_Meet(mention='{self.mention}', participant={self.participant}, place={self.place}, topic={self.topic})"

@dataclass
class Justice_Sentence_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
    def __repr__(self):
        return f"Justice_Sentence_Unspecified(mention='{self.mention}', place={self.place}, judgecourt={self.judgecourt}, defendant={self.defendant})"

@dataclass
class Justice_Convict_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, judgecourt: Optional[List] = None, defendant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.judgecourt = judgecourt if judgecourt is not None else []
        self.defendant = defendant if defendant is not None else []
    def __repr__(self):
        return f"Justice_Convict_Unspecified(mention='{self.mention}', judgecourt={self.judgecourt}, defendant={self.defendant})"

@dataclass
class Justice_InvestigateCrime_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, investigator: Optional[List] = None, observer: Optional[List] = None, defendant: Optional[List] = None, place: Optional[List] = None, observedentity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.investigator = investigator if investigator is not None else []
        self.observer = observer if observer is not None else []
        self.defendant = defendant if defendant is not None else []
        self.place = place if place is not None else []
        self.observedentity = observedentity if observedentity is not None else []
    def __repr__(self):
        return f"Justice_InvestigateCrime_Unspecified(mention='{self.mention}', investigator={self.investigator}, observer={self.observer}, defendant={self.defendant}, place={self.place}, observedentity={self.observedentity})"

@dataclass
class Cognitive_IdentifyCategorize_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, identifiedrole: Optional[List] = None, place: Optional[List] = None, identifiedobject: Optional[List] = None, identifier: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.identifiedrole = identifiedrole if identifiedrole is not None else []
        self.place = place if place is not None else []
        self.identifiedobject = identifiedobject if identifiedobject is not None else []
        self.identifier = identifier if identifier is not None else []
    def __repr__(self):
        return f"Cognitive_IdentifyCategorize_Unspecified(mention='{self.mention}', identifiedrole={self.identifiedrole}, place={self.place}, identifiedobject={self.identifiedobject}, identifier={self.identifier})"

@dataclass
class Conflict_Demonstrate_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, target: Optional[List] = None, topic: Optional[List] = None, demonstrator: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.target = target if target is not None else []
        self.topic = topic if topic is not None else []
        self.demonstrator = demonstrator if demonstrator is not None else []
    def __repr__(self):
        return f"Conflict_Demonstrate_Unspecified(mention='{self.mention}', target={self.target}, topic={self.topic}, demonstrator={self.demonstrator})"

@dataclass
class ArtifactExistence_ManufactureAssemble_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, components: Optional[List] = None, manufacturerassembler: Optional[List] = None, artifact: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.components = components if components is not None else []
        self.manufacturerassembler = manufacturerassembler if manufacturerassembler is not None else []
        self.artifact = artifact if artifact is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"ArtifactExistence_ManufactureAssemble_Unspecified(mention='{self.mention}', components={self.components}, manufacturerassembler={self.manufacturerassembler}, artifact={self.artifact}, place={self.place})"

@dataclass
class ArtifactExistence_DamageDestroyDisableDismantle_Dismantle(Event):
    def __init__(self, mention: Optional[str] = None, components: Optional[List] = None, dismantler: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.components = components if components is not None else []
        self.dismantler = dismantler if dismantler is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"ArtifactExistence_DamageDestroyDisableDismantle_Dismantle(mention='{self.mention}', components={self.components}, dismantler={self.dismantler}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class Movement_Transportation_Evacuation(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, passengerartifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.passengerartifact = passengerartifact if passengerartifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"Movement_Transportation_Evacuation(mention='{self.mention}', origin={self.origin}, passengerartifact={self.passengerartifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class Contact_ThreatenCoerce_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_ThreatenCoerce_Unspecified(mention='{self.mention}', communicator={self.communicator}, recipient={self.recipient})"

@dataclass
class Conflict_Defeat_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, defeated: Optional[List] = None, victor: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.defeated = defeated if defeated is not None else []
        self.victor = victor if victor is not None else []
    def __repr__(self):
        return f"Conflict_Defeat_Unspecified(mention='{self.mention}', place={self.place}, defeated={self.defeated}, victor={self.victor})"

@dataclass
class ArtifactExistence_DamageDestroyDisableDismantle_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None, damagerdestroyer: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
        self.damagerdestroyer = damagerdestroyer if damagerdestroyer is not None else []
    def __repr__(self):
        return f"ArtifactExistence_DamageDestroyDisableDismantle_Unspecified(mention='{self.mention}', artifact={self.artifact}, instrument={self.instrument}, place={self.place}, damagerdestroyer={self.damagerdestroyer})"

@dataclass
class Movement_Transportation_IllegalTransportation(Event):
    def __init__(self, mention: Optional[str] = None, vehicle: Optional[List] = None, passengerartifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.passengerartifact = passengerartifact if passengerartifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"Movement_Transportation_IllegalTransportation(mention='{self.mention}', vehicle={self.vehicle}, passengerartifact={self.passengerartifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class Transaction_ExchangeBuySell_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, acquiredentity: Optional[List] = None, giver: Optional[List] = None, recipient: Optional[List] = None, paymentbarter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.acquiredentity = acquiredentity if acquiredentity is not None else []
        self.giver = giver if giver is not None else []
        self.recipient = recipient if recipient is not None else []
        self.paymentbarter = paymentbarter if paymentbarter is not None else []
    def __repr__(self):
        return f"Transaction_ExchangeBuySell_Unspecified(mention='{self.mention}', acquiredentity={self.acquiredentity}, giver={self.giver}, recipient={self.recipient}, paymentbarter={self.paymentbarter})"

@dataclass
class ArtifactExistence_DamageDestroyDisableDismantle_Damage(Event):
    def __init__(self, mention: Optional[str] = None, damager: Optional[List] = None, artifact: Optional[List] = None, instrument: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.damager = damager if damager is not None else []
        self.artifact = artifact if artifact is not None else []
        self.instrument = instrument if instrument is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"ArtifactExistence_DamageDestroyDisableDismantle_Damage(mention='{self.mention}', damager={self.damager}, artifact={self.artifact}, instrument={self.instrument}, place={self.place})"

@dataclass
class Contact_Contact_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Contact_Contact_Unspecified(mention='{self.mention}', participant={self.participant}, place={self.place}, topic={self.topic})"

@dataclass
class Movement_Transportation_PreventPassage(Event):
    def __init__(self, mention: Optional[str] = None, origin: Optional[List] = None, vehicle: Optional[List] = None, preventer: Optional[List] = None, passengerartifact: Optional[List] = None, destination: Optional[List] = None, transporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.origin = origin if origin is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.preventer = preventer if preventer is not None else []
        self.passengerartifact = passengerartifact if passengerartifact is not None else []
        self.destination = destination if destination is not None else []
        self.transporter = transporter if transporter is not None else []
    def __repr__(self):
        return f"Movement_Transportation_PreventPassage(mention='{self.mention}', origin={self.origin}, vehicle={self.vehicle}, preventer={self.preventer}, passengerartifact={self.passengerartifact}, destination={self.destination}, transporter={self.transporter})"

@dataclass
class GenericCrime_GenericCrime_GenericCrime(Event):
    def __init__(self, mention: Optional[str] = None, perpetrator: Optional[List] = None, place: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.perpetrator = perpetrator if perpetrator is not None else []
        self.place = place if place is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"GenericCrime_GenericCrime_GenericCrime(mention='{self.mention}', perpetrator={self.perpetrator}, place={self.place}, victim={self.victim})"

@dataclass
class Contact_RequestCommand_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, place: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.place = place if place is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_RequestCommand_Unspecified(mention='{self.mention}', communicator={self.communicator}, place={self.place}, recipient={self.recipient})"

@dataclass
class Contact_ThreatenCoerce_Broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_ThreatenCoerce_Broadcast(mention='{self.mention}', communicator={self.communicator}, recipient={self.recipient})"

@dataclass
class Conflict_Demonstrate_DemonstrateWithViolence(Event):
    def __init__(self, mention: Optional[str] = None, regulator: Optional[List] = None, demonstrator: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.regulator = regulator if regulator is not None else []
        self.demonstrator = demonstrator if demonstrator is not None else []
    def __repr__(self):
        return f"Conflict_Demonstrate_DemonstrateWithViolence(mention='{self.mention}', regulator={self.regulator}, demonstrator={self.demonstrator})"

@dataclass
class Medical_Intervention_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, patient: Optional[List] = None, place: Optional[List] = None, treater: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.patient = patient if patient is not None else []
        self.place = place if place is not None else []
        self.treater = treater if treater is not None else []
    def __repr__(self):
        return f"Medical_Intervention_Unspecified(mention='{self.mention}', patient={self.patient}, place={self.place}, treater={self.treater})"

@dataclass
class Disaster_DiseaseOutbreak_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, victim: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.victim = victim if victim is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Disaster_DiseaseOutbreak_Unspecified(mention='{self.mention}', victim={self.victim}, place={self.place})"

@dataclass
class Disaster_Crash_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, crashobject: Optional[List] = None, place: Optional[List] = None, vehicle: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.crashobject = crashobject if crashobject is not None else []
        self.place = place if place is not None else []
        self.vehicle = vehicle if vehicle is not None else []
    def __repr__(self):
        return f"Disaster_Crash_Unspecified(mention='{self.mention}', crashobject={self.crashobject}, place={self.place}, vehicle={self.vehicle})"

@dataclass
class Cognitive_TeachingTrainingLearning_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, teachertrainer: Optional[List] = None, learner: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.teachertrainer = teachertrainer if teachertrainer is not None else []
        self.learner = learner if learner is not None else []
    def __repr__(self):
        return f"Cognitive_TeachingTrainingLearning_Unspecified(mention='{self.mention}', teachertrainer={self.teachertrainer}, learner={self.learner})"

@dataclass
class Personnel_StartPosition_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, position: Optional[List] = None, place: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.position = position if position is not None else []
        self.place = place if place is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"Personnel_StartPosition_Unspecified(mention='{self.mention}', placeofemployment={self.placeofemployment}, position={self.position}, place={self.place}, employee={self.employee})"

@dataclass
class Control_ImpedeInterfereWith_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, impeder: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.impeder = impeder if impeder is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Control_ImpedeInterfereWith_Unspecified(mention='{self.mention}', impeder={self.impeder}, place={self.place})"

@dataclass
class Cognitive_Research_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, researcher: Optional[List] = None, place: Optional[List] = None, subject: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.researcher = researcher if researcher is not None else []
        self.place = place if place is not None else []
        self.subject = subject if subject is not None else []
    def __repr__(self):
        return f"Cognitive_Research_Unspecified(mention='{self.mention}', researcher={self.researcher}, place={self.place}, subject={self.subject})"

@dataclass
class ArtifactExistence_DamageDestroyDisableDismantle_DisableDefuse(Event):
    def __init__(self, mention: Optional[str] = None, disabler: Optional[List] = None, instrument: Optional[List] = None, artifact: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.disabler = disabler if disabler is not None else []
        self.instrument = instrument if instrument is not None else []
        self.artifact = artifact if artifact is not None else []
    def __repr__(self):
        return f"ArtifactExistence_DamageDestroyDisableDismantle_DisableDefuse(mention='{self.mention}', disabler={self.disabler}, instrument={self.instrument}, artifact={self.artifact})"

@dataclass
class Contact_Contact_Correspondence(Event):
    def __init__(self, mention: Optional[str] = None, participant: Optional[List] = None, place: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant = participant if participant is not None else []
        self.place = place if place is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Contact_Contact_Correspondence(mention='{self.mention}', participant={self.participant}, place={self.place}, topic={self.topic})"

@dataclass
class Personnel_EndPosition_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, placeofemployment: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.placeofemployment = placeofemployment if placeofemployment is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"Personnel_EndPosition_Unspecified(mention='{self.mention}', placeofemployment={self.placeofemployment}, employee={self.employee})"

@dataclass
class Justice_Acquit_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, defendant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.defendant = defendant if defendant is not None else []
    def __repr__(self):
        return f"Justice_Acquit_Unspecified(mention='{self.mention}', defendant={self.defendant})"

@dataclass
class Contact_RequestCommand_Meet(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_RequestCommand_Meet(mention='{self.mention}', communicator={self.communicator}, recipient={self.recipient})"

@dataclass
class Contact_ThreatenCoerce_Correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_ThreatenCoerce_Correspondence(mention='{self.mention}', communicator={self.communicator}, recipient={self.recipient})"

@dataclass
class Contact_RequestCommand_Correspondence(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, topic: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.topic = topic if topic is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_RequestCommand_Correspondence(mention='{self.mention}', communicator={self.communicator}, topic={self.topic}, recipient={self.recipient})"

@dataclass
class Contact_RequestCommand_Broadcast(Event):
    def __init__(self, mention: Optional[str] = None, communicator: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.communicator = communicator if communicator is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Contact_RequestCommand_Broadcast(mention='{self.mention}', communicator={self.communicator}, recipient={self.recipient})"

@dataclass
class Transaction_Donation_Unspecified(Event):
    def __init__(self, mention: Optional[str] = None, giver: Optional[List] = None, artifactmoney: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.giver = giver if giver is not None else []
        self.artifactmoney = artifactmoney if artifactmoney is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Transaction_Donation_Unspecified(mention='{self.mention}', giver={self.giver}, artifactmoney={self.artifactmoney}, recipient={self.recipient})"

