# ===========================
# File: test_enumeration.py
# Description:
#     Modify test/dev data by adding missing event types with or without guideline-aware descriptions.
# ===========================

import json
import re
import random
import argparse

def get_max_instance_id(test_data):
    return max(int(instance["instance_id"]) for instance in test_data)

def create_class_definition(event_type, event_details, task_type, is_random=False, no_guideline=False):
    if no_guideline:
        new_class_definition = f"@dataclass\nclass {event_type}:\n"
        if task_type == "ED":
            new_class_definition += '    mention: str\n'
        else:
            for attr in event_details["attributes"].keys():
                attr_type = "List" if attr != "mention" else "str"
                new_class_definition += f'    {attr}: {attr_type}\n'
        return new_class_definition

    if isinstance(event_details["description"], list):
        class_description = random.choice(event_details["description"]) if is_random else event_details["description"][0]
    else:
        class_description = event_details["description"]

    new_class_definition = f"@dataclass\nclass {event_type}:\n    \"\"\"{class_description}\"\"\"\n"

    if task_type == "ED":
        new_class_definition += '    mention: str  # The text span that triggers the event.\n'
    else:
        for attr, description in event_details["attributes"].items():
            attr_type = "str" if attr == "mention" else "List"
            if isinstance(description, list):
                attr_description = random.choice(description) if is_random else description[0]
            else:
                attr_description = description
            new_class_definition += f'    {attr}: {attr_type}  # {attr_description}\n'

    return new_class_definition

def add_missing_event_types(test_data, master_event_types, ace_master_definitions, is_random=False, no_guideline=False):
    visited_wnd_ids = set()
    max_instance_id = get_max_instance_id(test_data)
    updated_test_data = test_data.copy()

    for instance in test_data:
        wnd_id = instance["wnd_id"]
        if wnd_id in visited_wnd_ids:
            continue
        visited_wnd_ids.add(wnd_id)
        task_type = instance["task_type"]

        unique_event_types = set()
        for inst in test_data:
            if inst["wnd_id"] == wnd_id:
                match = re.search(r'@dataclass\nclass (\w+)\(', inst["input"])
                if match:
                    unique_event_types.add(match.group(1))

        remaining_event_types = [event for event in master_event_types if event.split("(")[0] not in unique_event_types and event in ace_master_definitions]

        for event_type in remaining_event_types:
            if event_type not in ace_master_definitions:
                continue
            class_definition = create_class_definition(event_type, ace_master_definitions[event_type], task_type, is_random, no_guideline)
            new_instance = instance.copy()
            max_instance_id += 1
            new_instance["instance_id"] = str(max_instance_id)

            new_input = re.sub(r'@dataclass.*?(\n\n|$)', class_definition + '\n\n', instance["input"], flags=re.DOTALL)
            new_instance["input"] = new_input

            replacement_text = (
                "# No event mentions are present in this text with extractable arguments.\n"
                "# The list called result should be empty.\n\n"
            )
            new_instance["input"] = re.sub(
                r'# The list called result contains the instances for the following events.*?result =',
                replacement_text + "result =",
                new_instance["input"],
                flags=re.DOTALL
            )

            new_instance["output"] = "[]"
            updated_test_data.append(new_instance)

    return updated_test_data

def main():
    parser = argparse.ArgumentParser(description="Process test/dev data and add missing event types.")
    parser.add_argument("--test_file", required=True)
    parser.add_argument("--master_event_file", required=True)
    parser.add_argument("--ace_master_file", required=True)
    parser.add_argument("--output_file", required=True)
    parser.add_argument("--is_random", type=bool, default=False)
    parser.add_argument("--no_guideline", action="store_true", help="Use structural-only class definitions")
    args = parser.parse_args()

    print("\n==============================")
    print(f"📂 Processing: {args.test_file}")
    print(f"📥 Master event types: {args.master_event_file}")
    print(f"📥 Master definitions: {args.ace_master_file}")
    print(f"💾 Output path: {args.output_file}")
    print(f"📘 No Guideline Mode: {'YES' if args.no_guideline else 'NO'}")
    print("==============================\n")

    with open(args.test_file, "r") as test_file:
        test_data = json.load(test_file)
    with open(args.master_event_file, "r") as master_file:
        master_event_types = json.load(master_file)
    with open(args.ace_master_file, "r") as ace_file:
        ace_master_definitions = json.load(ace_file)

    updated_test_data = add_missing_event_types(test_data, master_event_types, ace_master_definitions, args.is_random, args.no_guideline)
    sorted_updated_test_data = sorted(updated_test_data, key=lambda x: x["wnd_id"])

    with open(args.output_file, "w") as updated_file:
        json.dump(sorted_updated_test_data, updated_file, indent=4)

if __name__ == "__main__":
    main()
