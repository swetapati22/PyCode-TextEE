from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class Adverse_event(Event):
    def __init__(self, mention: Optional[str] = None, treatment_route: Optional[List] = None, effect: Optional[List] = None, treatment_drug: Optional[List] = None, treatment_time_elapsed: Optional[List] = None, subject_gender: Optional[List] = None, treatment_duration: Optional[List] = None, treatment_freq: Optional[List] = None, subject_population: Optional[List] = None, treatment_dosage: Optional[List] = None, combination_drug: Optional[List] = None, treatment: Optional[List] = None, subject: Optional[List] = None, subject_age: Optional[List] = None, subject_race: Optional[List] = None, treatment_disorder: Optional[List] = None, subject_disorder: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.treatment_route = treatment_route if treatment_route is not None else []
        self.effect = effect if effect is not None else []
        self.treatment_drug = treatment_drug if treatment_drug is not None else []
        self.treatment_time_elapsed = treatment_time_elapsed if treatment_time_elapsed is not None else []
        self.subject_gender = subject_gender if subject_gender is not None else []
        self.treatment_duration = treatment_duration if treatment_duration is not None else []
        self.treatment_freq = treatment_freq if treatment_freq is not None else []
        self.subject_population = subject_population if subject_population is not None else []
        self.treatment_dosage = treatment_dosage if treatment_dosage is not None else []
        self.combination_drug = combination_drug if combination_drug is not None else []
        self.treatment = treatment if treatment is not None else []
        self.subject = subject if subject is not None else []
        self.subject_age = subject_age if subject_age is not None else []
        self.subject_race = subject_race if subject_race is not None else []
        self.treatment_disorder = treatment_disorder if treatment_disorder is not None else []
        self.subject_disorder = subject_disorder if subject_disorder is not None else []
    def __repr__(self):
        return f"Adverse_event(mention='{self.mention}', treatment_route={self.treatment_route}, effect={self.effect}, treatment_drug={self.treatment_drug}, treatment_time_elapsed={self.treatment_time_elapsed}, subject_gender={self.subject_gender}, treatment_duration={self.treatment_duration}, treatment_freq={self.treatment_freq}, subject_population={self.subject_population}, treatment_dosage={self.treatment_dosage}, combination_drug={self.combination_drug}, treatment={self.treatment}, subject={self.subject}, subject_age={self.subject_age}, subject_race={self.subject_race}, treatment_disorder={self.treatment_disorder}, subject_disorder={self.subject_disorder})"

@dataclass
class Potential_therapeutic_event(Event):
    def __init__(self, mention: Optional[str] = None, treatment_route: Optional[List] = None, treatment_drug: Optional[List] = None, effect: Optional[List] = None, treatment_time_elapsed: Optional[List] = None, subject_gender: Optional[List] = None, treatment_duration: Optional[List] = None, treatment_freq: Optional[List] = None, subject_population: Optional[List] = None, treatment_dosage: Optional[List] = None, combination_drug: Optional[List] = None, treatment: Optional[List] = None, subject_age: Optional[List] = None, subject: Optional[List] = None, subject_race: Optional[List] = None, treatment_disorder: Optional[List] = None, subject_disorder: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.treatment_route = treatment_route if treatment_route is not None else []
        self.treatment_drug = treatment_drug if treatment_drug is not None else []
        self.effect = effect if effect is not None else []
        self.treatment_time_elapsed = treatment_time_elapsed if treatment_time_elapsed is not None else []
        self.subject_gender = subject_gender if subject_gender is not None else []
        self.treatment_duration = treatment_duration if treatment_duration is not None else []
        self.treatment_freq = treatment_freq if treatment_freq is not None else []
        self.subject_population = subject_population if subject_population is not None else []
        self.treatment_dosage = treatment_dosage if treatment_dosage is not None else []
        self.combination_drug = combination_drug if combination_drug is not None else []
        self.treatment = treatment if treatment is not None else []
        self.subject_age = subject_age if subject_age is not None else []
        self.subject = subject if subject is not None else []
        self.subject_race = subject_race if subject_race is not None else []
        self.treatment_disorder = treatment_disorder if treatment_disorder is not None else []
        self.subject_disorder = subject_disorder if subject_disorder is not None else []
    def __repr__(self):
        return f"Potential_therapeutic_event(mention='{self.mention}', treatment_route={self.treatment_route}, treatment_drug={self.treatment_drug}, effect={self.effect}, treatment_time_elapsed={self.treatment_time_elapsed}, subject_gender={self.subject_gender}, treatment_duration={self.treatment_duration}, treatment_freq={self.treatment_freq}, subject_population={self.subject_population}, treatment_dosage={self.treatment_dosage}, combination_drug={self.combination_drug}, treatment={self.treatment}, subject_age={self.subject_age}, subject={self.subject}, subject_race={self.subject_race}, treatment_disorder={self.treatment_disorder}, subject_disorder={self.subject_disorder})"

