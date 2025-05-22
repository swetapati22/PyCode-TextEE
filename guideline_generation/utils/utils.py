import importlib
import random
import json
import sys
import re
import os

schema_splitters = {
    "ace05-en": ":",
    "speed": "None",
    "genia2013": "None",
    "maven": "None",
    "rams": ".",
    "fewevent": ".",
    "casie": ":",
    "geneva": "None",
    "mlee": "None",
    "genia2011": "None",
    "m2e2": ":",
    "phee": "None",
    "richere-en": ":",
    "muc4": "None",
    "mee": "_",
    "wikievents": "None"
}


def clean_event_name(event_type, dataset_name):
    splitter = schema_splitters[dataset_name]
    event_type = event_type.replace("n/a", "Na")
    event_type_parts = event_type.split(splitter)
    if len(event_type_parts) > 1:
        parent_event_name = event_type_parts[0].replace("-", "").replace(".", "_")
        if(dataset_name=="casie"):
            parent_event_name = parent_event_name.title()
        event_type = "_".join(event_type_parts[1:]).replace("-", "").replace(".", "_")
        if(dataset_name=="rams"):
            event_type = f"{parent_event_name}_{event_type}(Event)"
        else:
            parent_event_name = parent_event_name + "Event"
            event_type = f"{event_type}({parent_event_name})"
    else:
        original_event_type = event_type + ""
        event_type = event_type.replace("-", "").replace(".", "_") + "(Event)"
        if(dataset_name=="speed"):
            event_type = event_type.title()
    return event_type