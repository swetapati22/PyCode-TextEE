from dataclasses import dataclass
from typing import List, Optional
from utils_typing import Entity, Event, Relation, dataclass


@dataclass
class Event:
    pass

@dataclass
class Blood_vessel_development(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, atloc: Optional[List] = None, fromloc: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.atloc = atloc if atloc is not None else []
        self.fromloc = fromloc if fromloc is not None else []
    def __repr__(self):
        return f"Blood_vessel_development(mention='{self.mention}', theme={self.theme}, atloc={self.atloc}, fromloc={self.fromloc})"

@dataclass
class Breakdown(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Breakdown(mention='{self.mention}', theme={self.theme})"

@dataclass
class Regulation(Event):
    def __init__(self, mention: Optional[str] = None, site: Optional[List] = None, csite: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.site = site if site is not None else []
        self.csite = csite if csite is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
    def __repr__(self):
        return f"Regulation(mention='{self.mention}', site={self.site}, csite={self.csite}, theme={self.theme}, cause={self.cause})"

@dataclass
class Planned_process(Event):
    def __init__(self, mention: Optional[str] = None, theme2: Optional[List] = None, instrument2: Optional[List] = None, theme: Optional[List] = None, instrument: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme2 = theme2 if theme2 is not None else []
        self.instrument2 = instrument2 if instrument2 is not None else []
        self.theme = theme if theme is not None else []
        self.instrument = instrument if instrument is not None else []
    def __repr__(self):
        return f"Planned_process(mention='{self.mention}', theme2={self.theme2}, instrument2={self.instrument2}, theme={self.theme}, instrument={self.instrument})"

@dataclass
class Negative_regulation(Event):
    def __init__(self, mention: Optional[str] = None, site: Optional[List] = None, csite: Optional[List] = None, theme: Optional[List] = None, cause: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.site = site if site is not None else []
        self.csite = csite if csite is not None else []
        self.theme = theme if theme is not None else []
        self.cause = cause if cause is not None else []
    def __repr__(self):
        return f"Negative_regulation(mention='{self.mention}', site={self.site}, csite={self.csite}, theme={self.theme}, cause={self.cause})"

@dataclass
class Growth(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Growth(mention='{self.mention}', theme={self.theme})"

@dataclass
class Localization(Event):
    def __init__(self, mention: Optional[str] = None, toloc: Optional[List] = None, fromloc: Optional[List] = None, theme: Optional[List] = None, atloc: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.toloc = toloc if toloc is not None else []
        self.fromloc = fromloc if fromloc is not None else []
        self.theme = theme if theme is not None else []
        self.atloc = atloc if atloc is not None else []
    def __repr__(self):
        return f"Localization(mention='{self.mention}', toloc={self.toloc}, fromloc={self.fromloc}, theme={self.theme}, atloc={self.atloc})"

@dataclass
class Gene_expression(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Gene_expression(mention='{self.mention}', theme={self.theme})"

@dataclass
class Positive_regulation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, theme2: Optional[List] = None, csite: Optional[List] = None, site: Optional[List] = None, cause: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.theme2 = theme2 if theme2 is not None else []
        self.csite = csite if csite is not None else []
        self.site = site if site is not None else []
        self.cause = cause if cause is not None else []
    def __repr__(self):
        return f"Positive_regulation(mention='{self.mention}', theme={self.theme}, theme2={self.theme2}, csite={self.csite}, site={self.site}, cause={self.cause})"

@dataclass
class Cell_proliferation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Cell_proliferation(mention='{self.mention}', theme={self.theme})"

@dataclass
class Binding(Event):
    def __init__(self, mention: Optional[str] = None, theme2: Optional[List] = None, theme: Optional[List] = None, site: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme2 = theme2 if theme2 is not None else []
        self.theme = theme if theme is not None else []
        self.site = site if site is not None else []
    def __repr__(self):
        return f"Binding(mention='{self.mention}', theme2={self.theme2}, theme={self.theme}, site={self.site})"

@dataclass
class Transcription(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Transcription(mention='{self.mention}', theme={self.theme})"

@dataclass
class Development(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Development(mention='{self.mention}', theme={self.theme})"

@dataclass
class Remodeling(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Remodeling(mention='{self.mention}', theme={self.theme})"

@dataclass
class Metabolism(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Metabolism(mention='{self.mention}', theme={self.theme})"

@dataclass
class Synthesis(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Synthesis(mention='{self.mention}', theme={self.theme})"

@dataclass
class Catabolism(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Catabolism(mention='{self.mention}', theme={self.theme})"

@dataclass
class Pathway(Event):
    def __init__(self, mention: Optional[str] = None, participant3: Optional[List] = None, participant4: Optional[List] = None, participant2: Optional[List] = None, participant: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.participant3 = participant3 if participant3 is not None else []
        self.participant4 = participant4 if participant4 is not None else []
        self.participant2 = participant2 if participant2 is not None else []
        self.participant = participant if participant is not None else []
    def __repr__(self):
        return f"Pathway(mention='{self.mention}', participant3={self.participant3}, participant4={self.participant4}, participant2={self.participant2}, participant={self.participant})"

@dataclass
class Death(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Death(mention='{self.mention}', theme={self.theme})"

@dataclass
class Phosphorylation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, site: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.site = site if site is not None else []
    def __repr__(self):
        return f"Phosphorylation(mention='{self.mention}', theme={self.theme}, site={self.site})"

@dataclass
class Dephosphorylation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, site: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.site = site if site is not None else []
    def __repr__(self):
        return f"Dephosphorylation(mention='{self.mention}', theme={self.theme}, site={self.site})"

@dataclass
class Reproduction(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Reproduction(mention='{self.mention}', theme={self.theme})"

@dataclass
class Protein_processing(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Protein_processing(mention='{self.mention}', theme={self.theme})"

@dataclass
class Translation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Translation(mention='{self.mention}', theme={self.theme})"

@dataclass
class Cell_division(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Cell_division(mention='{self.mention}', theme={self.theme})"

@dataclass
class Dissociation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Dissociation(mention='{self.mention}', theme={self.theme})"

@dataclass
class DNA_methylation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None, site: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
        self.site = site if site is not None else []
    def __repr__(self):
        return f"DNA_methylation(mention='{self.mention}', theme={self.theme}, site={self.site})"

@dataclass
class Acetylation(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Acetylation(mention='{self.mention}', theme={self.theme})"

@dataclass
class Ubiquitination(Event):
    def __init__(self, mention: Optional[str] = None, theme: Optional[List] = None):
        self.mention = mention if mention is not None else []
        self.theme = theme if theme is not None else []
    def __repr__(self):
        return f"Ubiquitination(mention='{self.mention}', theme={self.theme})"

