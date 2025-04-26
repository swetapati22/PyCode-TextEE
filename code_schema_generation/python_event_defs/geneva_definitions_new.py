from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class Manufacturing(Event):
    def __init__(self, mention: Optional[str] = None, resource: Optional[List] = None, producer: Optional[List] = None, product: Optional[List] = None, instrument: Optional[List] = None, factory: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.resource = resource if resource is not None else []
        self.producer = producer if producer is not None else []
        self.product = product if product is not None else []
        self.instrument = instrument if instrument is not None else []
        self.factory = factory if factory is not None else []
    def __repr__(self):
        return f"Manufacturing(mention='{self.mention}', resource={self.resource}, producer={self.producer}, product={self.product}, instrument={self.instrument}, factory={self.factory})"

@dataclass
class Arranging(Event):
    def __init__(self, mention: Optional[str] = None, configuration: Optional[List] = None, location: Optional[List] = None, theme: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.configuration = configuration if configuration is not None else []
        self.location = location if location is not None else []
        self.theme = theme if theme is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Arranging(mention='{self.mention}', configuration={self.configuration}, location={self.location}, theme={self.theme}, agent={self.agent})"

@dataclass
class Confronting_problem(Event):
    def __init__(self, mention: Optional[str] = None, activity: Optional[List] = None, experiencer: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.activity = activity if activity is not None else []
        self.experiencer = experiencer if experiencer is not None else []
    def __repr__(self):
        return f"Confronting_problem(mention='{self.mention}', activity={self.activity}, experiencer={self.experiencer})"

@dataclass
class Causation(Event):
    def __init__(self, mention: Optional[str] = None, effect: Optional[List] = None, means: Optional[List] = None, actor: Optional[List] = None, affected: Optional[List] = None, cause: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.effect = effect if effect is not None else []
        self.means = means if means is not None else []
        self.actor = actor if actor is not None else []
        self.affected = affected if affected is not None else []
        self.cause = cause if cause is not None else []
    def __repr__(self):
        return f"Causation(mention='{self.mention}', effect={self.effect}, means={self.means}, actor={self.actor}, affected={self.affected}, cause={self.cause})"

@dataclass
class Action(Event):
    def __init__(self, mention: Optional[str] = None, domain: Optional[List] = None, act: Optional[List] = None, manner: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.domain = domain if domain is not None else []
        self.act = act if act is not None else []
        self.manner = manner if manner is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Action(mention='{self.mention}', domain={self.domain}, act={self.act}, manner={self.manner}, agent={self.agent})"

@dataclass
class Cause_change_of_position_on_a_scale(Event):
    def __init__(self, mention: Optional[str] = None, attribute: Optional[List] = None, value_2: Optional[List] = None, item: Optional[List] = None, cause: Optional[List] = None, value_1: Optional[List] = None, difference: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.attribute = attribute if attribute is not None else []
        self.value_2 = value_2 if value_2 is not None else []
        self.item = item if item is not None else []
        self.cause = cause if cause is not None else []
        self.value_1 = value_1 if value_1 is not None else []
        self.difference = difference if difference is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Cause_change_of_position_on_a_scale(mention='{self.mention}', attribute={self.attribute}, value_2={self.value_2}, item={self.item}, cause={self.cause}, value_1={self.value_1}, difference={self.difference}, agent={self.agent})"

@dataclass
class Sending(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, goal: Optional[List] = None, transferors: Optional[List] = None, source: Optional[List] = None, recipient: Optional[List] = None, vehicle: Optional[List] = None, theme: Optional[List] = None, sender: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.goal = goal if goal is not None else []
        self.transferors = transferors if transferors is not None else []
        self.source = source if source is not None else []
        self.recipient = recipient if recipient is not None else []
        self.vehicle = vehicle if vehicle is not None else []
        self.theme = theme if theme is not None else []
        self.sender = sender if sender is not None else []
    def __repr__(self):
        return f"Sending(mention='{self.mention}', means={self.means}, goal={self.goal}, transferors={self.transferors}, source={self.source}, recipient={self.recipient}, vehicle={self.vehicle}, theme={self.theme}, sender={self.sender})"

@dataclass
class Getting(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, source: Optional[List] = None, recipient: Optional[List] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.source = source if source is not None else []
        self.recipient = recipient if recipient is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Getting(mention='{self.mention}', means={self.means}, source={self.source}, recipient={self.recipient}, theme={self.theme})"

@dataclass
class Research(Event):
    def __init__(self, mention: Optional[str] = None, field: Optional[List] = None, researcher: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.field = field if field is not None else []
        self.researcher = researcher if researcher is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Research(mention='{self.mention}', field={self.field}, researcher={self.researcher}, topic={self.topic})"

@dataclass
class Legality(Event):
    def __init__(self, mention: Optional[str] = None, action: Optional[List] = None, object: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.action = action if action is not None else []
        self.object = object if object is not None else []
    def __repr__(self):
        return f"Legality(mention='{self.mention}', action={self.action}, object={self.object})"

@dataclass
class Statement(Event):
    def __init__(self, mention: Optional[str] = None, speaker: Optional[List] = None, message: Optional[List] = None, medium: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.speaker = speaker if speaker is not None else []
        self.message = message if message is not None else []
        self.medium = medium if medium is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Statement(mention='{self.mention}', speaker={self.speaker}, message={self.message}, medium={self.medium}, addressee={self.addressee})"

@dataclass
class Using(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, purpose: Optional[List] = None, instrument: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.purpose = purpose if purpose is not None else []
        self.instrument = instrument if instrument is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Using(mention='{self.mention}', means={self.means}, purpose={self.purpose}, instrument={self.instrument}, agent={self.agent})"

@dataclass
class Cost(Event):
    def __init__(self, mention: Optional[str] = None, goods: Optional[List] = None, intended_event: Optional[List] = None, payer: Optional[List] = None, rate: Optional[List] = None, asset: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goods = goods if goods is not None else []
        self.intended_event = intended_event if intended_event is not None else []
        self.payer = payer if payer is not None else []
        self.rate = rate if rate is not None else []
        self.asset = asset if asset is not None else []
    def __repr__(self):
        return f"Cost(mention='{self.mention}', goods={self.goods}, intended_event={self.intended_event}, payer={self.payer}, rate={self.rate}, asset={self.asset})"

@dataclass
class Traveling(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, traveler: Optional[List] = None, goal: Optional[List] = None, purpose: Optional[List] = None, entity: Optional[List] = None, distance: Optional[List] = None, area: Optional[List] = None, path: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.traveler = traveler if traveler is not None else []
        self.goal = goal if goal is not None else []
        self.purpose = purpose if purpose is not None else []
        self.entity = entity if entity is not None else []
        self.distance = distance if distance is not None else []
        self.area = area if area is not None else []
        self.path = path if path is not None else []
    def __repr__(self):
        return f"Traveling(mention='{self.mention}', means={self.means}, traveler={self.traveler}, goal={self.goal}, purpose={self.purpose}, entity={self.entity}, distance={self.distance}, area={self.area}, path={self.path})"

@dataclass
class Know(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, evidence: Optional[List] = None, instrument: Optional[List] = None, phenomenon: Optional[List] = None, cognizer: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.evidence = evidence if evidence is not None else []
        self.instrument = instrument if instrument is not None else []
        self.phenomenon = phenomenon if phenomenon is not None else []
        self.cognizer = cognizer if cognizer is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Know(mention='{self.mention}', means={self.means}, evidence={self.evidence}, instrument={self.instrument}, phenomenon={self.phenomenon}, cognizer={self.cognizer}, topic={self.topic})"

@dataclass
class Self_motion(Event):
    def __init__(self, mention: Optional[str] = None, goal: Optional[List] = None, self_mover: Optional[List] = None, source: Optional[List] = None, distance: Optional[List] = None, direction: Optional[List] = None, path: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goal = goal if goal is not None else []
        self.self_mover = self_mover if self_mover is not None else []
        self.source = source if source is not None else []
        self.distance = distance if distance is not None else []
        self.direction = direction if direction is not None else []
        self.path = path if path is not None else []
    def __repr__(self):
        return f"Self_motion(mention='{self.mention}', goal={self.goal}, self_mover={self.self_mover}, source={self.source}, distance={self.distance}, direction={self.direction}, path={self.path})"

@dataclass
class Destroying(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, patient: Optional[List] = None, destroyer: Optional[List] = None, cause: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.patient = patient if patient is not None else []
        self.destroyer = destroyer if destroyer is not None else []
        self.cause = cause if cause is not None else []
    def __repr__(self):
        return f"Destroying(mention='{self.mention}', means={self.means}, patient={self.patient}, destroyer={self.destroyer}, cause={self.cause})"

@dataclass
class Testing(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, result: Optional[List] = None, tested_property: Optional[List] = None, circumstances: Optional[List] = None, tester: Optional[List] = None, product: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.result = result if result is not None else []
        self.tested_property = tested_property if tested_property is not None else []
        self.circumstances = circumstances if circumstances is not None else []
        self.tester = tester if tester is not None else []
        self.product = product if product is not None else []
    def __repr__(self):
        return f"Testing(mention='{self.mention}', means={self.means}, result={self.result}, tested_property={self.tested_property}, circumstances={self.circumstances}, tester={self.tester}, product={self.product})"

@dataclass
class Creating(Event):
    def __init__(self, mention: Optional[str] = None, cause: Optional[List] = None, creator: Optional[List] = None, created_entity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.cause = cause if cause is not None else []
        self.creator = creator if creator is not None else []
        self.created_entity = created_entity if created_entity is not None else []
    def __repr__(self):
        return f"Creating(mention='{self.mention}', cause={self.cause}, creator={self.creator}, created_entity={self.created_entity})"

@dataclass
class Dispersal(Event):
    def __init__(self, mention: Optional[str] = None, individuals: Optional[List] = None, goal_area: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.individuals = individuals if individuals is not None else []
        self.goal_area = goal_area if goal_area is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Dispersal(mention='{self.mention}', individuals={self.individuals}, goal_area={self.goal_area}, cause={self.cause}, agent={self.agent})"

@dataclass
class Supply(Event):
    def __init__(self, mention: Optional[str] = None, recipient: Optional[List] = None, imposed_purpose: Optional[List] = None, supplier: Optional[List] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.recipient = recipient if recipient is not None else []
        self.imposed_purpose = imposed_purpose if imposed_purpose is not None else []
        self.supplier = supplier if supplier is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Supply(mention='{self.mention}', recipient={self.recipient}, imposed_purpose={self.imposed_purpose}, supplier={self.supplier}, theme={self.theme})"

@dataclass
class Process_end(Event):
    def __init__(self, mention: Optional[str] = None, state: Optional[List] = None, final_subevent: Optional[List] = None, time: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None, process: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.state = state if state is not None else []
        self.final_subevent = final_subevent if final_subevent is not None else []
        self.time = time if time is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
        self.process = process if process is not None else []
    def __repr__(self):
        return f"Process_end(mention='{self.mention}', state={self.state}, final_subevent={self.final_subevent}, time={self.time}, cause={self.cause}, agent={self.agent}, process={self.process})"

@dataclass
class Resolve_problem(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, problem: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.problem = problem if problem is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Resolve_problem(mention='{self.mention}', means={self.means}, problem={self.problem}, cause={self.cause}, agent={self.agent})"

@dataclass
class Cause_to_make_progress(Event):
    def __init__(self, mention: Optional[str] = None, project: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.project = project if project is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Cause_to_make_progress(mention='{self.mention}', project={self.project}, agent={self.agent})"

@dataclass
class Assistance(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, goal: Optional[List] = None, benefited_party: Optional[List] = None, focal_entity: Optional[List] = None, helper: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.goal = goal if goal is not None else []
        self.benefited_party = benefited_party if benefited_party is not None else []
        self.focal_entity = focal_entity if focal_entity is not None else []
        self.helper = helper if helper is not None else []
    def __repr__(self):
        return f"Assistance(mention='{self.mention}', means={self.means}, goal={self.goal}, benefited_party={self.benefited_party}, focal_entity={self.focal_entity}, helper={self.helper})"

@dataclass
class Arriving(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, goal: Optional[List] = None, source: Optional[List] = None, purpose: Optional[List] = None, theme: Optional[List] = None, place: Optional[List] = None, path: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.goal = goal if goal is not None else []
        self.source = source if source is not None else []
        self.purpose = purpose if purpose is not None else []
        self.theme = theme if theme is not None else []
        self.place = place if place is not None else []
        self.path = path if path is not None else []
    def __repr__(self):
        return f"Arriving(mention='{self.mention}', means={self.means}, goal={self.goal}, source={self.source}, purpose={self.purpose}, theme={self.theme}, place={self.place}, path={self.path})"

@dataclass
class Departing(Event):
    def __init__(self, mention: Optional[str] = None, traveller: Optional[List] = None, goal: Optional[List] = None, source: Optional[List] = None, path: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.traveller = traveller if traveller is not None else []
        self.goal = goal if goal is not None else []
        self.source = source if source is not None else []
        self.path = path if path is not None else []
    def __repr__(self):
        return f"Departing(mention='{self.mention}', traveller={self.traveller}, goal={self.goal}, source={self.source}, path={self.path})"

@dataclass
class Building(Event):
    def __init__(self, mention: Optional[str] = None, components: Optional[List] = None, created_entity: Optional[List] = None, place: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.components = components if components is not None else []
        self.created_entity = created_entity if created_entity is not None else []
        self.place = place if place is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Building(mention='{self.mention}', components={self.components}, created_entity={self.created_entity}, place={self.place}, agent={self.agent})"

@dataclass
class Presence(Event):
    def __init__(self, mention: Optional[str] = None, inherent_purpose: Optional[List] = None, time: Optional[List] = None, entity: Optional[List] = None, circumstances: Optional[List] = None, duration: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.inherent_purpose = inherent_purpose if inherent_purpose is not None else []
        self.time = time if time is not None else []
        self.entity = entity if entity is not None else []
        self.circumstances = circumstances if circumstances is not None else []
        self.duration = duration if duration is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Presence(mention='{self.mention}', inherent_purpose={self.inherent_purpose}, time={self.time}, entity={self.entity}, circumstances={self.circumstances}, duration={self.duration}, place={self.place})"

@dataclass
class Defending(Event):
    def __init__(self, mention: Optional[str] = None, defender: Optional[List] = None, assailant: Optional[List] = None, instrument: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.defender = defender if defender is not None else []
        self.assailant = assailant if assailant is not None else []
        self.instrument = instrument if instrument is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Defending(mention='{self.mention}', defender={self.defender}, assailant={self.assailant}, instrument={self.instrument}, victim={self.victim})"

@dataclass
class Attack(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, weapon: Optional[List] = None, assailant: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.weapon = weapon if weapon is not None else []
        self.assailant = assailant if assailant is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Attack(mention='{self.mention}', means={self.means}, weapon={self.weapon}, assailant={self.assailant}, victim={self.victim})"

@dataclass
class Request(Event):
    def __init__(self, mention: Optional[str] = None, speaker: Optional[List] = None, message: Optional[List] = None, medium: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.speaker = speaker if speaker is not None else []
        self.message = message if message is not None else []
        self.medium = medium if medium is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Request(mention='{self.mention}', speaker={self.speaker}, message={self.message}, medium={self.medium}, addressee={self.addressee})"

@dataclass
class Death(Event):
    def __init__(self, mention: Optional[str] = None, deceased: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.deceased = deceased if deceased is not None else []
    def __repr__(self):
        return f"Death(mention='{self.mention}', deceased={self.deceased})"

@dataclass
class Becoming(Event):
    def __init__(self, mention: Optional[str] = None, final_category: Optional[List] = None, final_quality: Optional[List] = None, entity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.final_category = final_category if final_category is not None else []
        self.final_quality = final_quality if final_quality is not None else []
        self.entity = entity if entity is not None else []
    def __repr__(self):
        return f"Becoming(mention='{self.mention}', final_category={self.final_category}, final_quality={self.final_quality}, entity={self.entity})"

@dataclass
class Change_of_leadership(Event):
    def __init__(self, mention: Optional[str] = None, role: Optional[List] = None, selector: Optional[List] = None, new_leader: Optional[List] = None, body: Optional[List] = None, old_leader: Optional[List] = None, old_order: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.role = role if role is not None else []
        self.selector = selector if selector is not None else []
        self.new_leader = new_leader if new_leader is not None else []
        self.body = body if body is not None else []
        self.old_leader = old_leader if old_leader is not None else []
        self.old_order = old_order if old_order is not None else []
    def __repr__(self):
        return f"Change_of_leadership(mention='{self.mention}', role={self.role}, selector={self.selector}, new_leader={self.new_leader}, body={self.body}, old_leader={self.old_leader}, old_order={self.old_order})"

@dataclass
class Process_start(Event):
    def __init__(self, mention: Optional[str] = None, event: Optional[List] = None, initial_subevent: Optional[List] = None, time: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.event = event if event is not None else []
        self.initial_subevent = initial_subevent if initial_subevent is not None else []
        self.time = time if time is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Process_start(mention='{self.mention}', event={self.event}, initial_subevent={self.initial_subevent}, time={self.time}, agent={self.agent})"

@dataclass
class Influence(Event):
    def __init__(self, mention: Optional[str] = None, situation: Optional[List] = None, action: Optional[List] = None, behavior: Optional[List] = None, cognizer: Optional[List] = None, agent: Optional[List] = None, product: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.situation = situation if situation is not None else []
        self.action = action if action is not None else []
        self.behavior = behavior if behavior is not None else []
        self.cognizer = cognizer if cognizer is not None else []
        self.agent = agent if agent is not None else []
        self.product = product if product is not None else []
    def __repr__(self):
        return f"Influence(mention='{self.mention}', situation={self.situation}, action={self.action}, behavior={self.behavior}, cognizer={self.cognizer}, agent={self.agent}, product={self.product})"

@dataclass
class Bringing(Event):
    def __init__(self, mention: Optional[str] = None, goal: Optional[List] = None, source: Optional[List] = None, carrier: Optional[List] = None, area: Optional[List] = None, theme: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goal = goal if goal is not None else []
        self.source = source if source is not None else []
        self.carrier = carrier if carrier is not None else []
        self.area = area if area is not None else []
        self.theme = theme if theme is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Bringing(mention='{self.mention}', goal={self.goal}, source={self.source}, carrier={self.carrier}, area={self.area}, theme={self.theme}, agent={self.agent})"

@dataclass
class Practice(Event):
    def __init__(self, mention: Optional[str] = None, agent: Optional[List] = None, action: Optional[List] = None, occasion: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.agent = agent if agent is not None else []
        self.action = action if action is not None else []
        self.occasion = occasion if occasion is not None else []
    def __repr__(self):
        return f"Practice(mention='{self.mention}', agent={self.agent}, action={self.action}, occasion={self.occasion})"

@dataclass
class Education_teaching(Event):
    def __init__(self, mention: Optional[str] = None, skill: Optional[List] = None, fact: Optional[List] = None, student: Optional[List] = None, teacher: Optional[List] = None, role: Optional[List] = None, subject: Optional[List] = None, course: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.skill = skill if skill is not None else []
        self.fact = fact if fact is not None else []
        self.student = student if student is not None else []
        self.teacher = teacher if teacher is not None else []
        self.role = role if role is not None else []
        self.subject = subject if subject is not None else []
        self.course = course if course is not None else []
    def __repr__(self):
        return f"Education_teaching(mention='{self.mention}', skill={self.skill}, fact={self.fact}, student={self.student}, teacher={self.teacher}, role={self.role}, subject={self.subject}, course={self.course})"

@dataclass
class Convincing(Event):
    def __init__(self, mention: Optional[str] = None, content: Optional[List] = None, speaker: Optional[List] = None, addressee: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.content = content if content is not None else []
        self.speaker = speaker if speaker is not None else []
        self.addressee = addressee if addressee is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Convincing(mention='{self.mention}', content={self.content}, speaker={self.speaker}, addressee={self.addressee}, topic={self.topic})"

@dataclass
class Scrutiny(Event):
    def __init__(self, mention: Optional[str] = None, phenomenon: Optional[List] = None, ground: Optional[List] = None, instrument: Optional[List] = None, unwanted_entity: Optional[List] = None, cognizer: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.phenomenon = phenomenon if phenomenon is not None else []
        self.ground = ground if ground is not None else []
        self.instrument = instrument if instrument is not None else []
        self.unwanted_entity = unwanted_entity if unwanted_entity is not None else []
        self.cognizer = cognizer if cognizer is not None else []
    def __repr__(self):
        return f"Scrutiny(mention='{self.mention}', phenomenon={self.phenomenon}, ground={self.ground}, instrument={self.instrument}, unwanted_entity={self.unwanted_entity}, cognizer={self.cognizer})"

@dataclass
class Expansion(Event):
    def __init__(self, mention: Optional[str] = None, dimension: Optional[List] = None, item: Optional[List] = None, initial_size: Optional[List] = None, result_size: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.dimension = dimension if dimension is not None else []
        self.item = item if item is not None else []
        self.initial_size = initial_size if initial_size is not None else []
        self.result_size = result_size if result_size is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Expansion(mention='{self.mention}', dimension={self.dimension}, item={self.item}, initial_size={self.initial_size}, result_size={self.result_size}, agent={self.agent})"

@dataclass
class Employment(Event):
    def __init__(self, mention: Optional[str] = None, place_of_employment: Optional[List] = None, type: Optional[List] = None, task: Optional[List] = None, employer: Optional[List] = None, position: Optional[List] = None, field: Optional[List] = None, employee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place_of_employment = place_of_employment if place_of_employment is not None else []
        self.type = type if type is not None else []
        self.task = task if task is not None else []
        self.employer = employer if employer is not None else []
        self.position = position if position is not None else []
        self.field = field if field is not None else []
        self.employee = employee if employee is not None else []
    def __repr__(self):
        return f"Employment(mention='{self.mention}', place_of_employment={self.place_of_employment}, type={self.type}, task={self.task}, employer={self.employer}, position={self.position}, field={self.field}, employee={self.employee})"

@dataclass
class Change(Event):
    def __init__(self, mention: Optional[str] = None, final_category: Optional[List] = None, attribute: Optional[List] = None, initial_category: Optional[List] = None, entity: Optional[List] = None, final_value: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.final_category = final_category if final_category is not None else []
        self.attribute = attribute if attribute is not None else []
        self.initial_category = initial_category if initial_category is not None else []
        self.entity = entity if entity is not None else []
        self.final_value = final_value if final_value is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Change(mention='{self.mention}', final_category={self.final_category}, attribute={self.attribute}, initial_category={self.initial_category}, entity={self.entity}, final_value={self.final_value}, cause={self.cause}, agent={self.agent})"

@dataclass
class Hostile_encounter(Event):
    def __init__(self, mention: Optional[str] = None, purpose: Optional[List] = None, sides: Optional[List] = None, side_1: Optional[List] = None, side_2: Optional[List] = None, instrument: Optional[List] = None, issue: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.purpose = purpose if purpose is not None else []
        self.sides = sides if sides is not None else []
        self.side_1 = side_1 if side_1 is not None else []
        self.side_2 = side_2 if side_2 is not None else []
        self.instrument = instrument if instrument is not None else []
        self.issue = issue if issue is not None else []
    def __repr__(self):
        return f"Hostile_encounter(mention='{self.mention}', purpose={self.purpose}, sides={self.sides}, side_1={self.side_1}, side_2={self.side_2}, instrument={self.instrument}, issue={self.issue})"

@dataclass
class Commerce_pay(Event):
    def __init__(self, mention: Optional[str] = None, goods: Optional[List] = None, money: Optional[List] = None, buyer: Optional[List] = None, seller: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goods = goods if goods is not None else []
        self.money = money if money is not None else []
        self.buyer = buyer if buyer is not None else []
        self.seller = seller if seller is not None else []
    def __repr__(self):
        return f"Commerce_pay(mention='{self.mention}', goods={self.goods}, money={self.money}, buyer={self.buyer}, seller={self.seller})"

@dataclass
class Collaboration(Event):
    def __init__(self, mention: Optional[str] = None, partners: Optional[List] = None, undertaking: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.partners = partners if partners is not None else []
        self.undertaking = undertaking if undertaking is not None else []
    def __repr__(self):
        return f"Collaboration(mention='{self.mention}', partners={self.partners}, undertaking={self.undertaking})"

@dataclass
class Arrest(Event):
    def __init__(self, mention: Optional[str] = None, authorities: Optional[List] = None, charges: Optional[List] = None, suspect: Optional[List] = None, offense: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.authorities = authorities if authorities is not None else []
        self.charges = charges if charges is not None else []
        self.suspect = suspect if suspect is not None else []
        self.offense = offense if offense is not None else []
    def __repr__(self):
        return f"Arrest(mention='{self.mention}', authorities={self.authorities}, charges={self.charges}, suspect={self.suspect}, offense={self.offense})"

@dataclass
class Bodily_harm(Event):
    def __init__(self, mention: Optional[str] = None, body_part: Optional[List] = None, instrument: Optional[List] = None, cause: Optional[List] = None, victim: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.body_part = body_part if body_part is not None else []
        self.instrument = instrument if instrument is not None else []
        self.cause = cause if cause is not None else []
        self.victim = victim if victim is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Bodily_harm(mention='{self.mention}', body_part={self.body_part}, instrument={self.instrument}, cause={self.cause}, victim={self.victim}, agent={self.agent})"

@dataclass
class Motion(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, goal: Optional[List] = None, source: Optional[List] = None, speed: Optional[List] = None, distance: Optional[List] = None, area: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None, path: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.goal = goal if goal is not None else []
        self.source = source if source is not None else []
        self.speed = speed if speed is not None else []
        self.distance = distance if distance is not None else []
        self.area = area if area is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
        self.path = path if path is not None else []
    def __repr__(self):
        return f"Motion(mention='{self.mention}', means={self.means}, goal={self.goal}, source={self.source}, speed={self.speed}, distance={self.distance}, area={self.area}, theme={self.theme}, cause={self.cause}, agent={self.agent}, path={self.path})"

@dataclass
class Catastrophe(Event):
    def __init__(self, mention: Optional[str] = None, patient: Optional[List] = None, cause: Optional[List] = None, place: Optional[List] = None, undesirable_event: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.patient = patient if patient is not None else []
        self.cause = cause if cause is not None else []
        self.place = place if place is not None else []
        self.undesirable_event = undesirable_event if undesirable_event is not None else []
    def __repr__(self):
        return f"Catastrophe(mention='{self.mention}', patient={self.patient}, cause={self.cause}, place={self.place}, undesirable_event={self.undesirable_event})"

@dataclass
class Bearing_arms(Event):
    def __init__(self, mention: Optional[str] = None, protagonist: Optional[List] = None, weapon: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.protagonist = protagonist if protagonist is not None else []
        self.weapon = weapon if weapon is not None else []
    def __repr__(self):
        return f"Bearing_arms(mention='{self.mention}', protagonist={self.protagonist}, weapon={self.weapon})"

@dataclass
class Participation(Event):
    def __init__(self, mention: Optional[str] = None, event: Optional[List] = None, participants: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.event = event if event is not None else []
        self.participants = participants if participants is not None else []
    def __repr__(self):
        return f"Participation(mention='{self.mention}', event={self.event}, participants={self.participants})"

@dataclass
class Communication(Event):
    def __init__(self, mention: Optional[str] = None, trigger: Optional[List] = None, speaker: Optional[List] = None, interlocutors: Optional[List] = None, message: Optional[List] = None, addressee: Optional[List] = None, topic: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.trigger = trigger if trigger is not None else []
        self.speaker = speaker if speaker is not None else []
        self.interlocutors = interlocutors if interlocutors is not None else []
        self.message = message if message is not None else []
        self.addressee = addressee if addressee is not None else []
        self.topic = topic if topic is not None else []
    def __repr__(self):
        return f"Communication(mention='{self.mention}', trigger={self.trigger}, speaker={self.speaker}, interlocutors={self.interlocutors}, message={self.message}, addressee={self.addressee}, topic={self.topic})"

@dataclass
class Telling(Event):
    def __init__(self, mention: Optional[str] = None, speaker: Optional[List] = None, message: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.speaker = speaker if speaker is not None else []
        self.message = message if message is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Telling(mention='{self.mention}', speaker={self.speaker}, message={self.message}, addressee={self.addressee})"

@dataclass
class Wearing(Event):
    def __init__(self, mention: Optional[str] = None, wearer: Optional[List] = None, clothing: Optional[List] = None, body_location: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.wearer = wearer if wearer is not None else []
        self.clothing = clothing if clothing is not None else []
        self.body_location = body_location if body_location is not None else []
    def __repr__(self):
        return f"Wearing(mention='{self.mention}', wearer={self.wearer}, clothing={self.clothing}, body_location={self.body_location})"

@dataclass
class Damaging(Event):
    def __init__(self, mention: Optional[str] = None, patient: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.patient = patient if patient is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Damaging(mention='{self.mention}', patient={self.patient}, cause={self.cause}, agent={self.agent})"

@dataclass
class Motion_directional(Event):
    def __init__(self, mention: Optional[str] = None, goal: Optional[List] = None, source: Optional[List] = None, direction: Optional[List] = None, area: Optional[List] = None, theme: Optional[List] = None, path: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goal = goal if goal is not None else []
        self.source = source if source is not None else []
        self.direction = direction if direction is not None else []
        self.area = area if area is not None else []
        self.theme = theme if theme is not None else []
        self.path = path if path is not None else []
    def __repr__(self):
        return f"Motion_directional(mention='{self.mention}', goal={self.goal}, source={self.source}, direction={self.direction}, area={self.area}, theme={self.theme}, path={self.path})"

@dataclass
class Placing(Event):
    def __init__(self, mention: Optional[str] = None, location: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.location = location if location is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Placing(mention='{self.mention}', location={self.location}, theme={self.theme}, cause={self.cause}, agent={self.agent})"

@dataclass
class Reveal_secret(Event):
    def __init__(self, mention: Optional[str] = None, speaker: Optional[List] = None, topic: Optional[List] = None, addressee: Optional[List] = None, information: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.speaker = speaker if speaker is not None else []
        self.topic = topic if topic is not None else []
        self.addressee = addressee if addressee is not None else []
        self.information = information if information is not None else []
    def __repr__(self):
        return f"Reveal_secret(mention='{self.mention}', speaker={self.speaker}, topic={self.topic}, addressee={self.addressee}, information={self.information})"

@dataclass
class Commerce_buy(Event):
    def __init__(self, mention: Optional[str] = None, buyer: Optional[List] = None, goods: Optional[List] = None, seller: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.buyer = buyer if buyer is not None else []
        self.goods = goods if goods is not None else []
        self.seller = seller if seller is not None else []
    def __repr__(self):
        return f"Commerce_buy(mention='{self.mention}', buyer={self.buyer}, goods={self.goods}, seller={self.seller})"

@dataclass
class Deciding(Event):
    def __init__(self, mention: Optional[str] = None, decision: Optional[List] = None, cognizer: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.decision = decision if decision is not None else []
        self.cognizer = cognizer if cognizer is not None else []
    def __repr__(self):
        return f"Deciding(mention='{self.mention}', decision={self.decision}, cognizer={self.cognizer})"

@dataclass
class Come_together(Event):
    def __init__(self, mention: Optional[str] = None, individuals: Optional[List] = None, configuration: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.individuals = individuals if individuals is not None else []
        self.configuration = configuration if configuration is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Come_together(mention='{self.mention}', individuals={self.individuals}, configuration={self.configuration}, place={self.place})"

@dataclass
class Earnings_and_losses(Event):
    def __init__(self, mention: Optional[str] = None, earner: Optional[List] = None, goods: Optional[List] = None, earnings: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.earner = earner if earner is not None else []
        self.goods = goods if goods is not None else []
        self.earnings = earnings if earnings is not None else []
    def __repr__(self):
        return f"Earnings_and_losses(mention='{self.mention}', earner={self.earner}, goods={self.goods}, earnings={self.earnings})"

@dataclass
class Create_artwork(Event):
    def __init__(self, mention: Optional[str] = None, activity: Optional[List] = None, culture: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.activity = activity if activity is not None else []
        self.culture = culture if culture is not None else []
    def __repr__(self):
        return f"Create_artwork(mention='{self.mention}', activity={self.activity}, culture={self.culture})"

@dataclass
class Judgment_communication(Event):
    def __init__(self, mention: Optional[str] = None, reason: Optional[List] = None, evaluee: Optional[List] = None, communicator: Optional[List] = None, topic: Optional[List] = None, medium: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.reason = reason if reason is not None else []
        self.evaluee = evaluee if evaluee is not None else []
        self.communicator = communicator if communicator is not None else []
        self.topic = topic if topic is not None else []
        self.medium = medium if medium is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Judgment_communication(mention='{self.mention}', reason={self.reason}, evaluee={self.evaluee}, communicator={self.communicator}, topic={self.topic}, medium={self.medium}, addressee={self.addressee})"

@dataclass
class Exchange(Event):
    def __init__(self, mention: Optional[str] = None, themes: Optional[List] = None, theme_2: Optional[List] = None, exchanger_1: Optional[List] = None, exchanger_2: Optional[List] = None, theme_1: Optional[List] = None, exchangers: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.themes = themes if themes is not None else []
        self.theme_2 = theme_2 if theme_2 is not None else []
        self.exchanger_1 = exchanger_1 if exchanger_1 is not None else []
        self.exchanger_2 = exchanger_2 if exchanger_2 is not None else []
        self.theme_1 = theme_1 if theme_1 is not None else []
        self.exchangers = exchangers if exchangers is not None else []
    def __repr__(self):
        return f"Exchange(mention='{self.mention}', themes={self.themes}, theme_2={self.theme_2}, exchanger_1={self.exchanger_1}, exchanger_2={self.exchanger_2}, theme_1={self.theme_1}, exchangers={self.exchangers})"

@dataclass
class Revenge(Event):
    def __init__(self, mention: Optional[str] = None, injury: Optional[List] = None, punishment: Optional[List] = None, avenger: Optional[List] = None, injured_party: Optional[List] = None, offender: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.injury = injury if injury is not None else []
        self.punishment = punishment if punishment is not None else []
        self.avenger = avenger if avenger is not None else []
        self.injured_party = injured_party if injured_party is not None else []
        self.offender = offender if offender is not None else []
    def __repr__(self):
        return f"Revenge(mention='{self.mention}', injury={self.injury}, punishment={self.punishment}, avenger={self.avenger}, injured_party={self.injured_party}, offender={self.offender})"

@dataclass
class Labeling(Event):
    def __init__(self, mention: Optional[str] = None, label: Optional[List] = None, speaker: Optional[List] = None, entity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.label = label if label is not None else []
        self.speaker = speaker if speaker is not None else []
        self.entity = entity if entity is not None else []
    def __repr__(self):
        return f"Labeling(mention='{self.mention}', label={self.label}, speaker={self.speaker}, entity={self.entity})"

@dataclass
class Cure(Event):
    def __init__(self, mention: Optional[str] = None, patient: Optional[List] = None, affliction: Optional[List] = None, treatment: Optional[List] = None, medication: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.patient = patient if patient is not None else []
        self.affliction = affliction if affliction is not None else []
        self.treatment = treatment if treatment is not None else []
        self.medication = medication if medication is not None else []
    def __repr__(self):
        return f"Cure(mention='{self.mention}', patient={self.patient}, affliction={self.affliction}, treatment={self.treatment}, medication={self.medication})"

@dataclass
class Social_event(Event):
    def __init__(self, mention: Optional[str] = None, attendees: Optional[List] = None, host: Optional[List] = None, social_event: Optional[List] = None, occasion: Optional[List] = None, beneficiary: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.attendees = attendees if attendees is not None else []
        self.host = host if host is not None else []
        self.social_event = social_event if social_event is not None else []
        self.occasion = occasion if occasion is not None else []
        self.beneficiary = beneficiary if beneficiary is not None else []
    def __repr__(self):
        return f"Social_event(mention='{self.mention}', attendees={self.attendees}, host={self.host}, social_event={self.social_event}, occasion={self.occasion}, beneficiary={self.beneficiary})"

@dataclass
class Commitment(Event):
    def __init__(self, mention: Optional[str] = None, speaker: Optional[List] = None, message: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.speaker = speaker if speaker is not None else []
        self.message = message if message is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Commitment(mention='{self.mention}', speaker={self.speaker}, message={self.message}, addressee={self.addressee})"

@dataclass
class Commerce_sell(Event):
    def __init__(self, mention: Optional[str] = None, goods: Optional[List] = None, money: Optional[List] = None, buyer: Optional[List] = None, seller: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goods = goods if goods is not None else []
        self.money = money if money is not None else []
        self.buyer = buyer if buyer is not None else []
        self.seller = seller if seller is not None else []
    def __repr__(self):
        return f"Commerce_sell(mention='{self.mention}', goods={self.goods}, money={self.money}, buyer={self.buyer}, seller={self.seller})"

@dataclass
class Coming_to_believe(Event):
    def __init__(self, mention: Optional[str] = None, cognizer: Optional[List] = None, content: Optional[List] = None, means: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.cognizer = cognizer if cognizer is not None else []
        self.content = content if content is not None else []
        self.means = means if means is not None else []
    def __repr__(self):
        return f"Coming_to_believe(mention='{self.mention}', cognizer={self.cognizer}, content={self.content}, means={self.means})"

@dataclass
class Protest(Event):
    def __init__(self, mention: Optional[str] = None, arguer: Optional[List] = None, content: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.arguer = arguer if arguer is not None else []
        self.content = content if content is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Protest(mention='{self.mention}', arguer={self.arguer}, content={self.content}, addressee={self.addressee})"

@dataclass
class Terrorism(Event):
    def __init__(self, mention: Optional[str] = None, terrorist: Optional[List] = None, act: Optional[List] = None, instrument: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.terrorist = terrorist if terrorist is not None else []
        self.act = act if act is not None else []
        self.instrument = instrument if instrument is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Terrorism(mention='{self.mention}', terrorist={self.terrorist}, act={self.act}, instrument={self.instrument}, victim={self.victim})"

@dataclass
class Giving(Event):
    def __init__(self, mention: Optional[str] = None, offerer: Optional[List] = None, theme: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.offerer = offerer if offerer is not None else []
        self.theme = theme if theme is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Giving(mention='{self.mention}', offerer={self.offerer}, theme={self.theme}, recipient={self.recipient})"

@dataclass
class Recovering(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, entity: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.entity = entity if entity is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Recovering(mention='{self.mention}', means={self.means}, entity={self.entity}, agent={self.agent})"

@dataclass
class Receiving(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, donor: Optional[List] = None, recipient: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.donor = donor if donor is not None else []
        self.recipient = recipient if recipient is not None else []
    def __repr__(self):
        return f"Receiving(mention='{self.mention}', theme={self.theme}, donor={self.donor}, recipient={self.recipient})"

@dataclass
class Control(Event):
    def __init__(self, mention: Optional[str] = None, dependent_variable: Optional[List] = None, controlling_variable: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.dependent_variable = dependent_variable if dependent_variable is not None else []
        self.controlling_variable = controlling_variable if controlling_variable is not None else []
    def __repr__(self):
        return f"Control(mention='{self.mention}', dependent_variable={self.dependent_variable}, controlling_variable={self.controlling_variable})"

@dataclass
class Killing(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, killer: Optional[List] = None, instrument: Optional[List] = None, cause: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.killer = killer if killer is not None else []
        self.instrument = instrument if instrument is not None else []
        self.cause = cause if cause is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Killing(mention='{self.mention}', means={self.means}, killer={self.killer}, instrument={self.instrument}, cause={self.cause}, victim={self.victim})"

@dataclass
class Theft(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, goods: Optional[List] = None, perpetrator: Optional[List] = None, source: Optional[List] = None, instrument: Optional[List] = None, victim: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.goods = goods if goods is not None else []
        self.perpetrator = perpetrator if perpetrator is not None else []
        self.source = source if source is not None else []
        self.instrument = instrument if instrument is not None else []
        self.victim = victim if victim is not None else []
    def __repr__(self):
        return f"Theft(mention='{self.mention}', means={self.means}, goods={self.goods}, perpetrator={self.perpetrator}, source={self.source}, instrument={self.instrument}, victim={self.victim})"

@dataclass
class Rite(Event):
    def __init__(self, mention: Optional[str] = None, type: Optional[List] = None, member: Optional[List] = None, object: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.type = type if type is not None else []
        self.member = member if member is not None else []
        self.object = object if object is not None else []
    def __repr__(self):
        return f"Rite(mention='{self.mention}', type={self.type}, member={self.member}, object={self.object})"

@dataclass
class Quarreling(Event):
    def __init__(self, mention: Optional[str] = None, arguer2: Optional[List] = None, issue: Optional[List] = None, arguers: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.arguer2 = arguer2 if arguer2 is not None else []
        self.issue = issue if issue is not None else []
        self.arguers = arguers if arguers is not None else []
    def __repr__(self):
        return f"Quarreling(mention='{self.mention}', arguer2={self.arguer2}, issue={self.issue}, arguers={self.arguers})"

@dataclass
class Preventing_or_letting(Event):
    def __init__(self, mention: Optional[str] = None, event: Optional[List] = None, means: Optional[List] = None, potential_hindrance: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.event = event if event is not None else []
        self.means = means if means is not None else []
        self.potential_hindrance = potential_hindrance if potential_hindrance is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Preventing_or_letting(mention='{self.mention}', event={self.event}, means={self.means}, potential_hindrance={self.potential_hindrance}, agent={self.agent})"

@dataclass
class Openness(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, barrier: Optional[List] = None, useful_location: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.barrier = barrier if barrier is not None else []
        self.useful_location = useful_location if useful_location is not None else []
    def __repr__(self):
        return f"Openness(mention='{self.mention}', theme={self.theme}, barrier={self.barrier}, useful_location={self.useful_location})"

@dataclass
class Connect(Event):
    def __init__(self, mention: Optional[str] = None, figures: Optional[List] = None, ground: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.figures = figures if figures is not None else []
        self.ground = ground if ground is not None else []
    def __repr__(self):
        return f"Connect(mention='{self.mention}', figures={self.figures}, ground={self.ground})"

@dataclass
class Conquering(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, conqueror: Optional[List] = None, means: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.conqueror = conqueror if conqueror is not None else []
        self.means = means if means is not None else []
    def __repr__(self):
        return f"Conquering(mention='{self.mention}', theme={self.theme}, conqueror={self.conqueror}, means={self.means})"

@dataclass
class Becoming_a_member(Event):
    def __init__(self, mention: Optional[str] = None, group: Optional[List] = None, new_member: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.group = group if group is not None else []
        self.new_member = new_member if new_member is not None else []
    def __repr__(self):
        return f"Becoming_a_member(mention='{self.mention}', group={self.group}, new_member={self.new_member})"

@dataclass
class Ratification(Event):
    def __init__(self, mention: Optional[str] = None, ratifier: Optional[List] = None, proposal: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.ratifier = ratifier if ratifier is not None else []
        self.proposal = proposal if proposal is not None else []
    def __repr__(self):
        return f"Ratification(mention='{self.mention}', ratifier={self.ratifier}, proposal={self.proposal})"

@dataclass
class Adducing(Event):
    def __init__(self, mention: Optional[str] = None, speaker: Optional[List] = None, role: Optional[List] = None, medium: Optional[List] = None, specified_entity: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.speaker = speaker if speaker is not None else []
        self.role = role if role is not None else []
        self.medium = medium if medium is not None else []
        self.specified_entity = specified_entity if specified_entity is not None else []
    def __repr__(self):
        return f"Adducing(mention='{self.mention}', speaker={self.speaker}, role={self.role}, medium={self.medium}, specified_entity={self.specified_entity})"

@dataclass
class Sign_agreement(Event):
    def __init__(self, mention: Optional[str] = None, signatory: Optional[List] = None, agreement: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.signatory = signatory if signatory is not None else []
        self.agreement = agreement if agreement is not None else []
    def __repr__(self):
        return f"Sign_agreement(mention='{self.mention}', signatory={self.signatory}, agreement={self.agreement})"

@dataclass
class Coming_to_be(Event):
    def __init__(self, mention: Optional[str] = None, components: Optional[List] = None, time: Optional[List] = None, entity: Optional[List] = None, place: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.components = components if components is not None else []
        self.time = time if time is not None else []
        self.entity = entity if entity is not None else []
        self.place = place if place is not None else []
    def __repr__(self):
        return f"Coming_to_be(mention='{self.mention}', components={self.components}, time={self.time}, entity={self.entity}, place={self.place})"

@dataclass
class Perception_active(Event):
    def __init__(self, mention: Optional[str] = None, perceiver_agentive: Optional[List] = None, phenomenon: Optional[List] = None, direction: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.perceiver_agentive = perceiver_agentive if perceiver_agentive is not None else []
        self.phenomenon = phenomenon if phenomenon is not None else []
        self.direction = direction if direction is not None else []
    def __repr__(self):
        return f"Perception_active(mention='{self.mention}', perceiver_agentive={self.perceiver_agentive}, phenomenon={self.phenomenon}, direction={self.direction})"

@dataclass
class Committing_crime(Event):
    def __init__(self, mention: Optional[str] = None, instrument: Optional[List] = None, perpetrator: Optional[List] = None, crime: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.instrument = instrument if instrument is not None else []
        self.perpetrator = perpetrator if perpetrator is not None else []
        self.crime = crime if crime is not None else []
    def __repr__(self):
        return f"Committing_crime(mention='{self.mention}', instrument={self.instrument}, perpetrator={self.perpetrator}, crime={self.crime})"

@dataclass
class Supporting(Event):
    def __init__(self, mention: Optional[str] = None, supported: Optional[List] = None, supporter: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.supported = supported if supported is not None else []
        self.supporter = supporter if supporter is not None else []
    def __repr__(self):
        return f"Supporting(mention='{self.mention}', supported={self.supported}, supporter={self.supporter})"

@dataclass
class Containing(Event):
    def __init__(self, mention: Optional[str] = None, container: Optional[List] = None, contents: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.container = container if container is not None else []
        self.contents = contents if contents is not None else []
    def __repr__(self):
        return f"Containing(mention='{self.mention}', container={self.container}, contents={self.contents})"

@dataclass
class Hold(Event):
    def __init__(self, mention: Optional[str] = None, entity: Optional[List] = None, manipulator: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.entity = entity if entity is not None else []
        self.manipulator = manipulator if manipulator is not None else []
    def __repr__(self):
        return f"Hold(mention='{self.mention}', entity={self.entity}, manipulator={self.manipulator})"

@dataclass
class Emergency(Event):
    def __init__(self, mention: Optional[str] = None, place: Optional[List] = None, undesirable_event: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.place = place if place is not None else []
        self.undesirable_event = undesirable_event if undesirable_event is not None else []
    def __repr__(self):
        return f"Emergency(mention='{self.mention}', place={self.place}, undesirable_event={self.undesirable_event})"

@dataclass
class Choosing(Event):
    def __init__(self, mention: Optional[str] = None, possibilities: Optional[List] = None, cognizer: Optional[List] = None, chosen: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.possibilities = possibilities if possibilities is not None else []
        self.cognizer = cognizer if cognizer is not None else []
        self.chosen = chosen if chosen is not None else []
    def __repr__(self):
        return f"Choosing(mention='{self.mention}', possibilities={self.possibilities}, cognizer={self.cognizer}, chosen={self.chosen})"

@dataclass
class Hindering(Event):
    def __init__(self, mention: Optional[str] = None, protagonist: Optional[List] = None, hindrance: Optional[List] = None, action: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.protagonist = protagonist if protagonist is not None else []
        self.hindrance = hindrance if hindrance is not None else []
        self.action = action if action is not None else []
    def __repr__(self):
        return f"Hindering(mention='{self.mention}', protagonist={self.protagonist}, hindrance={self.hindrance}, action={self.action})"

@dataclass
class Removing(Event):
    def __init__(self, mention: Optional[str] = None, goal: Optional[List] = None, source: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goal = goal if goal is not None else []
        self.source = source if source is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Removing(mention='{self.mention}', goal={self.goal}, source={self.source}, theme={self.theme}, cause={self.cause}, agent={self.agent})"

@dataclass
class Cause_to_amalgamate(Event):
    def __init__(self, mention: Optional[str] = None, parts: Optional[List] = None, part_2: Optional[List] = None, whole: Optional[List] = None, part_1: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.parts = parts if parts is not None else []
        self.part_2 = part_2 if part_2 is not None else []
        self.whole = whole if whole is not None else []
        self.part_1 = part_1 if part_1 is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Cause_to_amalgamate(mention='{self.mention}', parts={self.parts}, part_2={self.part_2}, whole={self.whole}, part_1={self.part_1}, agent={self.agent})"

@dataclass
class Agree_or_refuse_to_act(Event):
    def __init__(self, mention: Optional[str] = None, proposed_action: Optional[List] = None, speaker: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.proposed_action = proposed_action if proposed_action is not None else []
        self.speaker = speaker if speaker is not None else []
    def __repr__(self):
        return f"Agree_or_refuse_to_act(mention='{self.mention}', proposed_action={self.proposed_action}, speaker={self.speaker})"

@dataclass
class Achieve(Event):
    def __init__(self, mention: Optional[str] = None, agent: Optional[List] = None, goal: Optional[List] = None, means: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.agent = agent if agent is not None else []
        self.goal = goal if goal is not None else []
        self.means = means if means is not None else []
    def __repr__(self):
        return f"Achieve(mention='{self.mention}', agent={self.agent}, goal={self.goal}, means={self.means})"

@dataclass
class Check(Event):
    def __init__(self, mention: Optional[str] = None, means: Optional[List] = None, inspector: Optional[List] = None, unconfirmed_content: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.means = means if means is not None else []
        self.inspector = inspector if inspector is not None else []
        self.unconfirmed_content = unconfirmed_content if unconfirmed_content is not None else []
    def __repr__(self):
        return f"Check(mention='{self.mention}', means={self.means}, inspector={self.inspector}, unconfirmed_content={self.unconfirmed_content})"

@dataclass
class Writing(Event):
    def __init__(self, mention: Optional[str] = None, author: Optional[List] = None, instrument: Optional[List] = None, text: Optional[List] = None, addressee: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.author = author if author is not None else []
        self.instrument = instrument if instrument is not None else []
        self.text = text if text is not None else []
        self.addressee = addressee if addressee is not None else []
    def __repr__(self):
        return f"Writing(mention='{self.mention}', author={self.author}, instrument={self.instrument}, text={self.text}, addressee={self.addressee})"

@dataclass
class Emptying(Event):
    def __init__(self, mention: Optional[str] = None, source: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.source = source if source is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Emptying(mention='{self.mention}', source={self.source}, theme={self.theme}, cause={self.cause}, agent={self.agent})"

@dataclass
class GetReady(Event):
    def __init__(self, mention: Optional[str] = None, activity: Optional[List] = None, protagonist: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.activity = activity if activity is not None else []
        self.protagonist = protagonist if protagonist is not None else []
    def __repr__(self):
        return f"GetReady(mention='{self.mention}', activity={self.activity}, protagonist={self.protagonist})"

@dataclass
class Filling(Event):
    def __init__(self, mention: Optional[str] = None, goal: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.goal = goal if goal is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Filling(mention='{self.mention}', goal={self.goal}, theme={self.theme}, cause={self.cause}, agent={self.agent})"

@dataclass
class Ingestion(Event):
    def __init__(self, mention: Optional[str] = None, ingestor: Optional[List] = None, ingestibles: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.ingestor = ingestor if ingestor is not None else []
        self.ingestibles = ingestibles if ingestibles is not None else []
    def __repr__(self):
        return f"Ingestion(mention='{self.mention}', ingestor={self.ingestor}, ingestibles={self.ingestibles})"

@dataclass
class Response(Event):
    def __init__(self, mention: Optional[str] = None, response: Optional[List] = None, trigger: Optional[List] = None, responding_entity: Optional[List] = None, agent: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.response = response if response is not None else []
        self.trigger = trigger if trigger is not None else []
        self.responding_entity = responding_entity if responding_entity is not None else []
        self.agent = agent if agent is not None else []
    def __repr__(self):
        return f"Response(mention='{self.mention}', response={self.response}, trigger={self.trigger}, responding_entity={self.responding_entity}, agent={self.agent})"

@dataclass
class Criminal_investigation(Event):
    def __init__(self, mention: Optional[str] = None, suspect: Optional[List] = None, investigator: Optional[List] = None, incident: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.suspect = suspect if suspect is not None else []
        self.investigator = investigator if investigator is not None else []
        self.incident = incident if incident is not None else []
    def __repr__(self):
        return f"Criminal_investigation(mention='{self.mention}', suspect={self.suspect}, investigator={self.investigator}, incident={self.incident})"

@dataclass
class Competition(Event):
    def __init__(self, mention: Optional[str] = None, venue: Optional[List] = None, participants: Optional[List] = None, competition: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.venue = venue if venue is not None else []
        self.participants = participants if participants is not None else []
        self.competition = competition if competition is not None else []
    def __repr__(self):
        return f"Competition(mention='{self.mention}', venue={self.venue}, participants={self.participants}, competition={self.competition})"

