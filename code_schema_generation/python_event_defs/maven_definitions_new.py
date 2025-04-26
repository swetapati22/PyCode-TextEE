from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class Military_operation(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Military_operation(mention='{self.mention}')"

@dataclass
class Bearing_arms(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Bearing_arms(mention='{self.mention}')"

@dataclass
class Hostile_encounter(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Hostile_encounter(mention='{self.mention}')"

@dataclass
class Becoming_a_member(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Becoming_a_member(mention='{self.mention}')"

@dataclass
class Bodily_harm(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Bodily_harm(mention='{self.mention}')"

@dataclass
class Using(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Using(mention='{self.mention}')"

@dataclass
class Conquering(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Conquering(mention='{self.mention}')"

@dataclass
class Self_motion(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Self_motion(mention='{self.mention}')"

@dataclass
class Participation(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Participation(mention='{self.mention}')"

@dataclass
class Surrendering(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Surrendering(mention='{self.mention}')"

@dataclass
class Bringing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Bringing(mention='{self.mention}')"

@dataclass
class Confronting_problem(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Confronting_problem(mention='{self.mention}')"

@dataclass
class Causation(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Causation(mention='{self.mention}')"

@dataclass
class Process_start(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Process_start(mention='{self.mention}')"

@dataclass
class Being_in_operation(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Being_in_operation(mention='{self.mention}')"

@dataclass
class Recovering(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Recovering(mention='{self.mention}')"

@dataclass
class Cause_to_make_progress(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cause_to_make_progress(mention='{self.mention}')"

@dataclass
class Process_end(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Process_end(mention='{self.mention}')"

@dataclass
class Sign_agreement(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Sign_agreement(mention='{self.mention}')"

@dataclass
class Writing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Writing(mention='{self.mention}')"

@dataclass
class Legal_rulings(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Legal_rulings(mention='{self.mention}')"

@dataclass
class Change_of_leadership(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Change_of_leadership(mention='{self.mention}')"

@dataclass
class Defending(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Defending(mention='{self.mention}')"

@dataclass
class Escaping(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Escaping(mention='{self.mention}')"

@dataclass
class Creating(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Creating(mention='{self.mention}')"

@dataclass
class Response(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Response(mention='{self.mention}')"

@dataclass
class Collaboration(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Collaboration(mention='{self.mention}')"

@dataclass
class Change(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Change(mention='{self.mention}')"

@dataclass
class Getting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Getting(mention='{self.mention}')"

@dataclass
class Quarreling(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Quarreling(mention='{self.mention}')"

@dataclass
class Perception_active(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Perception_active(mention='{self.mention}')"

@dataclass
class Convincing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Convincing(mention='{self.mention}')"

@dataclass
class Communication(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Communication(mention='{self.mention}')"

@dataclass
class Damaging(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Damaging(mention='{self.mention}')"

@dataclass
class Cause_to_amalgamate(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cause_to_amalgamate(mention='{self.mention}')"

@dataclass
class Cause_change_of_position_on_a_scale(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cause_change_of_position_on_a_scale(mention='{self.mention}')"

@dataclass
class Cause_change_of_strength(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cause_change_of_strength(mention='{self.mention}')"

@dataclass
class Motion(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Motion(mention='{self.mention}')"

@dataclass
class Coming_to_be(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Coming_to_be(mention='{self.mention}')"

@dataclass
class Achieve(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Achieve(mention='{self.mention}')"

@dataclass
class Catastrophe(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Catastrophe(mention='{self.mention}')"

@dataclass
class Destroying(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Destroying(mention='{self.mention}')"

@dataclass
class Reporting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Reporting(mention='{self.mention}')"

@dataclass
class Influence(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Influence(mention='{self.mention}')"

@dataclass
class Having_or_lacking_access(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Having_or_lacking_access(mention='{self.mention}')"

@dataclass
class Expansion(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Expansion(mention='{self.mention}')"

@dataclass
class Removing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Removing(mention='{self.mention}')"

@dataclass
class Competition(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Competition(mention='{self.mention}')"

@dataclass
class Sending(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Sending(mention='{self.mention}')"

@dataclass
class Preventing_or_letting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Preventing_or_letting(mention='{self.mention}')"

@dataclass
class Becoming(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Becoming(mention='{self.mention}')"

@dataclass
class Agree_or_refuse_to_act(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Agree_or_refuse_to_act(mention='{self.mention}')"

@dataclass
class Traveling(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Traveling(mention='{self.mention}')"

@dataclass
class Commerce_pay(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Commerce_pay(mention='{self.mention}')"

@dataclass
class Social_event(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Social_event(mention='{self.mention}')"

@dataclass
class Hold(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Hold(mention='{self.mention}')"

@dataclass
class Recording(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Recording(mention='{self.mention}')"

@dataclass
class Name_conferral(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Name_conferral(mention='{self.mention}')"

@dataclass
class Arriving(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Arriving(mention='{self.mention}')"

@dataclass
class Motion_directional(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Motion_directional(mention='{self.mention}')"

@dataclass
class Lighting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Lighting(mention='{self.mention}')"

@dataclass
class Presence(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Presence(mention='{self.mention}')"

@dataclass
class Attack(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Attack(mention='{self.mention}')"

@dataclass
class Departing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Departing(mention='{self.mention}')"

@dataclass
class Killing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Killing(mention='{self.mention}')"

@dataclass
class Supply(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Supply(mention='{self.mention}')"

@dataclass
class Arranging(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Arranging(mention='{self.mention}')"

@dataclass
class Rewards_and_punishments(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Rewards_and_punishments(mention='{self.mention}')"

@dataclass
class Receiving(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Receiving(mention='{self.mention}')"

@dataclass
class Expressing_publicly(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Expressing_publicly(mention='{self.mention}')"

@dataclass
class Hindering(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Hindering(mention='{self.mention}')"

@dataclass
class Earnings_and_losses(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Earnings_and_losses(mention='{self.mention}')"

@dataclass
class Award(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Award(mention='{self.mention}')"

@dataclass
class Action(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Action(mention='{self.mention}')"

@dataclass
class Adducing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Adducing(mention='{self.mention}')"

@dataclass
class Practice(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Practice(mention='{self.mention}')"

@dataclass
class Create_artwork(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Create_artwork(mention='{self.mention}')"

@dataclass
class Come_together(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Come_together(mention='{self.mention}')"

@dataclass
class Statement(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Statement(mention='{self.mention}')"

@dataclass
class Vocalizations(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Vocalizations(mention='{self.mention}')"

@dataclass
class Judgment_communication(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Judgment_communication(mention='{self.mention}')"

@dataclass
class Arrest(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Arrest(mention='{self.mention}')"

@dataclass
class Request(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Request(mention='{self.mention}')"

@dataclass
class Preserving(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Preserving(mention='{self.mention}')"

@dataclass
class Check(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Check(mention='{self.mention}')"

@dataclass
class Theft(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Theft(mention='{self.mention}')"

@dataclass
class Change_sentiment(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Change_sentiment(mention='{self.mention}')"

@dataclass
class Assistance(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Assistance(mention='{self.mention}')"

@dataclass
class Aiming(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Aiming(mention='{self.mention}')"

@dataclass
class Cause_to_be_included(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cause_to_be_included(mention='{self.mention}')"

@dataclass
class Control(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Control(mention='{self.mention}')"

@dataclass
class Emptying(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Emptying(mention='{self.mention}')"

@dataclass
class Choosing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Choosing(mention='{self.mention}')"

@dataclass
class Placing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Placing(mention='{self.mention}')"

@dataclass
class Testing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Testing(mention='{self.mention}')"

@dataclass
class Extradition(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Extradition(mention='{self.mention}')"

@dataclass
class Building(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Building(mention='{self.mention}')"

@dataclass
class Education_teaching(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Education_teaching(mention='{self.mention}')"

@dataclass
class Supporting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Supporting(mention='{self.mention}')"

@dataclass
class Filling(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Filling(mention='{self.mention}')"

@dataclass
class Death(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Death(mention='{self.mention}')"

@dataclass
class Change_event_time(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Change_event_time(mention='{self.mention}')"

@dataclass
class Employment(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Employment(mention='{self.mention}')"

@dataclass
class Dispersal(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Dispersal(mention='{self.mention}')"

@dataclass
class Research(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Research(mention='{self.mention}')"

@dataclass
class Know(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Know(mention='{self.mention}')"

@dataclass
class GiveUp(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"GiveUp(mention='{self.mention}')"

@dataclass
class Surrounding(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Surrounding(mention='{self.mention}')"

@dataclass
class Connect(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Connect(mention='{self.mention}')"

@dataclass
class Reforming_a_system(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Reforming_a_system(mention='{self.mention}')"

@dataclass
class Manufacturing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Manufacturing(mention='{self.mention}')"

@dataclass
class Legality(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Legality(mention='{self.mention}')"

@dataclass
class Deciding(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Deciding(mention='{self.mention}')"

@dataclass
class Forming_relationships(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Forming_relationships(mention='{self.mention}')"

@dataclass
class Body_movement(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Body_movement(mention='{self.mention}')"

@dataclass
class Warning(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Warning(mention='{self.mention}')"

@dataclass
class Cost(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cost(mention='{self.mention}')"

@dataclass
class Use_firearm(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Use_firearm(mention='{self.mention}')"

@dataclass
class Commerce_sell(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Commerce_sell(mention='{self.mention}')"

@dataclass
class Giving(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Giving(mention='{self.mention}')"

@dataclass
class Openness(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Openness(mention='{self.mention}')"

@dataclass
class Rescuing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Rescuing(mention='{self.mention}')"

@dataclass
class Coming_to_believe(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Coming_to_believe(mention='{self.mention}')"

@dataclass
class Wearing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Wearing(mention='{self.mention}')"

@dataclass
class Carry_goods(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Carry_goods(mention='{self.mention}')"

@dataclass
class Commitment(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Commitment(mention='{self.mention}')"

@dataclass
class Violence(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Violence(mention='{self.mention}')"

@dataclass
class Criminal_investigation(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Criminal_investigation(mention='{self.mention}')"

@dataclass
class Institutionalization(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Institutionalization(mention='{self.mention}')"

@dataclass
class Commerce_buy(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Commerce_buy(mention='{self.mention}')"

@dataclass
class Besieging(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Besieging(mention='{self.mention}')"

@dataclass
class Expend_resource(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Expend_resource(mention='{self.mention}')"

@dataclass
class Cure(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Cure(mention='{self.mention}')"

@dataclass
class Rite(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Rite(mention='{self.mention}')"

@dataclass
class Imposing_obligation(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Imposing_obligation(mention='{self.mention}')"

@dataclass
class Submitting_documents(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Submitting_documents(mention='{self.mention}')"

@dataclass
class GetReady(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"GetReady(mention='{self.mention}')"

@dataclass
class Kidnapping(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Kidnapping(mention='{self.mention}')"

@dataclass
class Releasing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Releasing(mention='{self.mention}')"

@dataclass
class Committing_crime(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Committing_crime(mention='{self.mention}')"

@dataclass
class Resolve_problem(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Resolve_problem(mention='{self.mention}')"

@dataclass
class Publishing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Publishing(mention='{self.mention}')"

@dataclass
class Temporary_stay(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Temporary_stay(mention='{self.mention}')"

@dataclass
class Containing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Containing(mention='{self.mention}')"

@dataclass
class Exchange(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Exchange(mention='{self.mention}')"

@dataclass
class Limiting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Limiting(mention='{self.mention}')"

@dataclass
class Scouring(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Scouring(mention='{self.mention}')"

@dataclass
class Ingestion(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Ingestion(mention='{self.mention}')"

@dataclass
class Telling(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Telling(mention='{self.mention}')"

@dataclass
class Terrorism(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Terrorism(mention='{self.mention}')"

@dataclass
class Protest(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Protest(mention='{self.mention}')"

@dataclass
class Robbery(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Robbery(mention='{self.mention}')"

@dataclass
class Scrutiny(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Scrutiny(mention='{self.mention}')"

@dataclass
class Justifying(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Justifying(mention='{self.mention}')"

@dataclass
class Suspicion(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Suspicion(mention='{self.mention}')"

@dataclass
class Reveal_secret(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Reveal_secret(mention='{self.mention}')"

@dataclass
class Revenge(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Revenge(mention='{self.mention}')"

@dataclass
class Renting(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Renting(mention='{self.mention}')"

@dataclass
class Patrolling(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Patrolling(mention='{self.mention}')"

@dataclass
class Prison(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Prison(mention='{self.mention}')"

@dataclass
class Hiding_objects(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Hiding_objects(mention='{self.mention}')"

@dataclass
class Emergency(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Emergency(mention='{self.mention}')"

@dataclass
class Risk(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Risk(mention='{self.mention}')"

@dataclass
class Incident(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Incident(mention='{self.mention}')"

@dataclass
class Labeling(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Labeling(mention='{self.mention}')"

@dataclass
class Ratification(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Ratification(mention='{self.mention}')"

@dataclass
class Breathing(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Breathing(mention='{self.mention}')"

@dataclass
class Change_tool(Event):
    def __init__(self, mention: Optional[str] = None):
        self.mention = mention if mention is not None else []
    def __repr__(self):
        return f"Change_tool(mention='{self.mention}')"

