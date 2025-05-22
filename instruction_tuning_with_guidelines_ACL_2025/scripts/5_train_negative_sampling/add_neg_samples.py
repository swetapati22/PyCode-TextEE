# # ===========================
# # File: add_neg_samples.py
# # Description:
# #     Add negative event-type examples to training data with guideline-aware descriptions,
# #     or structure-only for No_guideline setting.
# # ===========================

# import os
# import json
# import re
# import random
# import argparse

# def get_max_instance_id(instances):
#     return max(int(instance["instance_id"]) for instance in instances)

# def create_class_definition(event_type, event_details, task_type, is_random=False, no_guideline=False):
#     if no_guideline:
#         # Structure-only class definition (no guideline description)
#         new_class_definition = f"@dataclass\nclass {event_type}:\n"
#         if task_type == "ED":
#             new_class_definition += '    mention: str\n'
#         else:
#             for attr in event_details["attributes"].keys():
#                 attr_type = "str" if attr == "mention" else "List"
#                 new_class_definition += f'    {attr}: {attr_type}\n'
#         return new_class_definition

#     # Standard guideline-based class definition
#     if isinstance(event_details["description"], list):
#         class_description = random.choice(event_details["description"]) if is_random else event_details["description"][0]
#     else:
#         class_description = event_details["description"]

#     new_class_definition = f"@dataclass\nclass {event_type}:\n    \"\"\"{class_description}\"\"\"\n"

#     if task_type == "ED":
#         new_class_definition += '    mention: str  # The text span that triggers the event.\n'
#     else:
#         for attr, description in event_details["attributes"].items():
#             attr_type = "str" if attr == "mention" else "List"
#             if isinstance(description, list):
#                 attr_description = random.choice(description) if is_random else description[0]
#             else:
#                 attr_description = description
#             new_class_definition += f'    {attr}: {attr_type}  # {attr_description}\n'

#     return new_class_definition

# def add_missing_event_types(data, master_event_types, ace_master_definitions, num_instances=None, is_random=False, no_guideline=False):
#     visited_wnd_ids = set()
#     max_instance_id = get_max_instance_id(data)
#     updated_data = data.copy()

#     for instance in data:
#         wnd_id = instance["wnd_id"]
#         if wnd_id in visited_wnd_ids:
#             continue
#         visited_wnd_ids.add(wnd_id)
#         task_type = instance["task_type"]

#         unique_event_types = set(
#             re.search(r'@dataclass\nclass (\w+)', inst["input"]).group(1)
#             for inst in data if inst["wnd_id"] == wnd_id and re.search(r'@dataclass\nclass (\w+)', inst["input"])
#         )

#         remaining_event_types = [e for e in master_event_types if e not in unique_event_types and e in ace_master_definitions]
#         selected_event_types = random.sample(remaining_event_types, min(num_instances, len(remaining_event_types))) if num_instances else remaining_event_types

#         for event_type in selected_event_types:
#             class_def = create_class_definition(event_type, ace_master_definitions[event_type], task_type, is_random, no_guideline)
#             new_instance = instance.copy()
#             max_instance_id += 1
#             new_instance["instance_id"] = str(max_instance_id)
#             new_instance["input"] = re.sub(r'@dataclass.*?(\n\n|$)', class_def + '\n', instance["input"], flags=re.DOTALL)
#             replacement_text = "# No event mentions are present in this text with extractable arguments.\n# The list called result should be empty.\n\n"
#             new_instance["input"] = re.sub(
#                 r'# The list called result contains the instances for the following events.*?result =',
#                 replacement_text + "result =",
#                 new_instance["input"],
#                 flags=re.DOTALL
#             )
#             new_instance["output"] = "[]"
#             updated_data.append(new_instance)

#     return sorted(updated_data, key=lambda x: x["wnd_id"])

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--test_file", required=True)
#     parser.add_argument("--master_event_file", required=True)
#     parser.add_argument("--ace_master_file", required=True)
#     parser.add_argument("--output_file", required=True)
#     parser.add_argument("--is_random", type=bool, default=False)
#     parser.add_argument("--num_instances", type=int, default=None)
#     args = parser.parse_args()

#     # Automatically detect "No_guideline" setting
#     no_guideline = "No_guideline" in args.test_file or "No_guideline" in args.output_file

#     print("\n==============================")
#     print(f"📂 Processing: {args.test_file}")
#     print(f"📥 Train file: {args.test_file}")
#     print(f"📥 Master event types file: {args.master_event_file}")
#     print(f"📥 ACE master definition file: {args.ace_master_file}")
#     print(f"💾 Output file will be saved to: {args.output_file}")
#     print(f"📘 No Guideline Mode: {'YES' if no_guideline else 'NO'}")
#     print("==============================\n")

#     with open(args.test_file, "r") as f:
#         test_data = json.load(f)
#     with open(args.master_event_file, "r") as f:
#         master_event_types = json.load(f)
#     with open(args.ace_master_file, "r") as f:
#         ace_master_definitions = json.load(f)

#     updated_data = add_missing_event_types(
#         test_data,
#         master_event_types,
#         ace_master_definitions,
#         args.num_instances,
#         args.is_random,
#         no_guideline
#     )

#     with open(args.output_file, "w") as f:
#         json.dump(updated_data, f, indent=4)

# if __name__ == "__main__":
#     main()

# ===========================
# File: add_negative_examples.py
# Description:
#     Add negative event-type examples to training data with or without guideline-aware descriptions.
# ===========================

import os
import json
import re
import random
import argparse

def get_max_instance_id(instances):
    return max(int(instance["instance_id"]) for instance in instances)

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

def add_missing_event_types(data, master_event_types, ace_master_definitions, num_instances=None, is_random=False, no_guideline=False):
    visited_wnd_ids = set()
    max_instance_id = get_max_instance_id(data)
    updated_data = data.copy()

    for instance in data:
        wnd_id = instance["wnd_id"]
        if wnd_id in visited_wnd_ids:
            continue
        visited_wnd_ids.add(wnd_id)
        task_type = instance["task_type"]

        unique_event_types = set(
            re.search(r'@dataclass\\nclass (\\w+)', inst["input"]).group(1)
            for inst in data if inst["wnd_id"] == wnd_id and re.search(r'@dataclass\\nclass (\\w+)', inst["input"])
        )

        remaining_event_types = [e for e in master_event_types if e not in unique_event_types and e in ace_master_definitions]
        selected_event_types = random.sample(remaining_event_types, min(num_instances, len(remaining_event_types))) if num_instances else remaining_event_types

        for event_type in selected_event_types:
            class_def = create_class_definition(event_type, ace_master_definitions[event_type], task_type, is_random, no_guideline)
            new_instance = instance.copy()
            max_instance_id += 1
            new_instance["instance_id"] = str(max_instance_id)
            new_instance["input"] = re.sub(r'@dataclass.*?(\n\n|$)', class_def + '\n', instance["input"], flags=re.DOTALL)
            replacement_text = "# No event mentions are present in this text with extractable arguments.\n# The list called result should be empty.\n\n"
            new_instance["input"] = re.sub(
                r'# The list called result contains the instances for the following events.*?result =',
                replacement_text + "result =",
                new_instance["input"],
                flags=re.DOTALL
            )
            new_instance["output"] = "[]"
            updated_data.append(new_instance)

    return sorted(updated_data, key=lambda x: x["wnd_id"])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_file", required=True)
    parser.add_argument("--master_event_file", required=True)
    parser.add_argument("--ace_master_file", required=True)
    parser.add_argument("--output_file", required=True)
    parser.add_argument("--is_random", type=bool, default=False)
    parser.add_argument("--num_instances", type=int, default=None)
    parser.add_argument("--no_guideline", action="store_true", help="Use structural-only class definitions (no guideline text)")
    args = parser.parse_args()

    print("\n==============================")
    print(f"📂 Processing: {args.test_file}")
    print(f"📥 Train file: {args.test_file}")
    print(f"📥 Master event types file: {args.master_event_file}")
    print(f"📥 Master definition file: {args.ace_master_file}")
    print(f"💾 Output file will be saved to: {args.output_file}")
    print(f"📘 No Guideline Mode: {'YES' if args.no_guideline else 'NO'}")
    print("==============================\n")

    with open(args.test_file, "r") as f:
        test_data = json.load(f)
    with open(args.master_event_file, "r") as f:
        master_event_types = json.load(f)
    with open(args.ace_master_file, "r") as f:
        ace_master_definitions = json.load(f)

    updated_data = add_missing_event_types(
        test_data,
        master_event_types,
        ace_master_definitions,
        args.num_instances,
        args.is_random,
        args.no_guideline
    )

    with open(args.output_file, "w") as f:
        json.dump(updated_data, f, indent=4)

if __name__ == "__main__":
    main()
