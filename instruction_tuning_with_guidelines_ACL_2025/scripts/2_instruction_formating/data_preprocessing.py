import os
import re
import copy
import json
import argparse
import random
from dataclasses import dataclass
from typing import List, Dict, Set, Any
from collections import defaultdict

# Utility function to convert hyphenated event names to CamelCase:
def to_camel_case(s):
    return ''.join(part.capitalize() for part in s.split('-'))

# Utility function to handle 'n/a' and RAMS/WikiEvents formatting
def to_rams_event_name(s):
    return s.replace('n/a', 'Na')

def append_random_event_definition(json_data, dataclass_definitions):
    # Choose a random event class from the available definitions
    random_event_type = random.choice(list(dataclass_definitions.keys()))
    random_event_def = dataclass_definitions[random_event_type]

    # Construct the event mention structure with no results
    event_mention = {
        random_event_def['class_name']: {
            "definition": random_event_def['definition'],
            "output_found": 0,
            "results": []
        }
    }
    # Ensure that 'event_mentions' is a dictionary
    if 'event_mentions' not in json_data or not isinstance(json_data['event_mentions'], dict):
        json_data['event_mentions'] = {}

    # Add the random event mention to the 'event_mentions'
    json_data['event_mentions'].update(event_mention)

    return json_data

def complete_event_attributes(event_type: str, result_str: str, guidelines: Dict[str, Dict[str, Any]], transformed_event_types: Dict[str, str]) -> str:
    # Use the transformed event type instead of the original event type
    transformed_event_type = transformed_event_types.get(event_type, event_type)

    if transformed_event_type not in guidelines:
        # print(f"Warning: Event type '{transformed_event_type}' not found in guidelines.")
        return result_str

    # print("result_str")
    # print(result_str)
    
    expected_attributes = set(guidelines[transformed_event_type]["attributes"].keys()) - {"mention"}

    # print("-*"*100)
    # print(f"Expected attributes for {transformed_event_type}: {expected_attributes}")
    
    # Extract existing attributes from the result_str
    existing_attributes = set()
    for attr in expected_attributes:
        # if f"{attr}=[" in result_str:
        if re.search(rf"\b{attr}=\[", result_str):
            existing_attributes.add(attr)

    # print(f"Existing attributes in result: {existing_attributes}")
    
    missing_attributes = expected_attributes - existing_attributes

    # Debugging print statement to check missing attributes
    # print(f"Missing attributes: {missing_attributes}")
    
    if not missing_attributes:
        # No missing attributes; return as is
        return result_str
    
    # Prepare the string to append missing attributes
    missing_attrs_str = ""
    for attr in sorted(missing_attributes):
        # Uniformly insert newlines for all attributes, including the missing ones
        missing_attrs_str += f",\n    {attr}=[]"
    
    # Insert the missing attributes before the closing parenthesis
    if result_str.endswith(")"):
        # Ensure that existing attributes are followed by a newline, if needed
        result_str = result_str.rstrip(")\n")  # Strip any extra closing parenthesis and newlines

        # Check if there is a trailing comma after the mention, and remove it if present
        if result_str.endswith(","):
            result_str = result_str.rstrip(",")

        modified_result = result_str + missing_attrs_str + "\n)"
    else:
        # Handle unexpected formatting
        modified_result = result_str + missing_attrs_str
    
    return modified_result

# Function to collect attributes for each event type:
def collect_event_attributes(json_data) -> Dict[str, Set[str]]:
    event_types = defaultdict(set)
    for entry in json_data:
        if 'event_mentions' in entry:
            for event in entry['event_mentions']:
                event_type = event['event_type']
                
                # Always capture the event_type, even if no arguments are present
                if 'arguments' in event and event['arguments']:
                    for argument in event.get('arguments', []):
                        # event_types[event_type].add(argument['role'].lower())
                        # Replace hyphen with underscore in argument role
                        event_types[event_type].add(argument['role'].lower().replace('-', '_'))
                else:
                    # If no arguments are present, just add the event_type with an empty set
                    event_types[event_type]  # This will ensure the event type is recorded

    return event_types

# Function to remove duplicate hierarchy parts, keeping the rightmost one
def remove_duplicate_hierarchy(parts: List[str]) -> List[str]:
    seen = set()
    result = []
    for part in reversed(parts):
        if part.lower() == 'n/a':  # Handle 'n/a' conversion to 'Na'
            part = 'Na'
        if part not in seen:
            result.append(part)
            seen.add(part)
    return list(reversed(result))

def generate_dataclass_definitions(event_types: Dict[str, Set[str]], custom_sep: str = None,dataset_name: str = None, task_type: str = None) -> Dict[str, Dict[str, List[str]]]:

    dataclass_definitions = {}
    transformed_event_types = {}
    event_type_mapper = {}

    for event_type, arguments in event_types.items():
        original_event_type = event_type  # Store the original event type for mapping

        # Handle splitting by colon (:), period (.), or custom separator
        if custom_sep and custom_sep.lower() != "none" and custom_sep in event_type:
            parts = event_type.split(custom_sep)
        elif ':' in event_type:
            parts = event_type.split(':')
        elif '.' in event_type:
            parts = event_type.split('.')
        else:
            parts = [event_type]

        # Special case for "rams" or "wikievents" datasets
        if dataset_name in ["rams", "wikievents"]:
            transformed_event_type = event_type.replace(':', '_').replace('.', '_')
            if custom_sep:
                transformed_event_type = transformed_event_type.replace(custom_sep, '_')

            # Replace 'n/a' with 'Na' and apply RAMS/WikiEvents formatting
            class_name = to_rams_event_name(transformed_event_type)
            transformed_event_types[original_event_type] = f"{class_name}(Event)"
            event_type_mapper[original_event_type] = f"{class_name}(Event)"

            # Initialize the dataclass definition for RAMS/WikiEvents with attributes
            # dataclass_definition = [f"class {class_name}(Event):", "    mention: str"]
            dataclass_definition = ["@dataclass", f"class {class_name}(Event):", "    mention: str"]

            # Only add attributes if the task is not ED
            if task_type != "ED":
                # Add attributes using the original event_type key (which has periods/colons)
                for argument in sorted(arguments):
                    #dataclass_definition.append(f"    {argument}: List")
                    # Replace hyphen with underscore in attribute name
                    dataclass_definition.append(f"    {argument.replace('-', '_')}: List")

            # Store the generated dataclass definition
            dataclass_definitions[original_event_type] = {
                "class_name": class_name,
                "definition": dataclass_definition
            }
            continue  # Skip further processing for RAMS/WikiEvents

        # For non-RAMS/WikiEvents, remove duplicates, keeping the rightmost part
        parts = remove_duplicate_hierarchy(parts)

        # Determine the parent and child class hierarchy (for non-RAMS/WikiEvents)
        if len(parts) >= 2:
            parent_part = to_camel_case(parts[-2]) + "Event"
            child_part = to_camel_case(parts[-1])
            class_name = f"{child_part}({parent_part})"
        else:
            main_type = to_camel_case(parts[0])
            class_name = f"{main_type}(Event)"

        # Store the transformed event type and generate dataclass definition
        transformed_event_types[original_event_type] = class_name
        event_type_mapper[original_event_type] = class_name

        # Initialize the dataclass definition for the lowest child class with attributes
        dataclass_definition = ["@dataclass", f"class {class_name}:", "    mention: str"]

        # Only add attributes if the task is not ED
        if task_type != "ED":
            for argument in sorted(arguments):
                # dataclass_definition.append(f"    {argument}: List")
                # Replace hyphen with underscore in attribute name
                dataclass_definition.append(f"    {argument.replace('-', '_')}: List")

        # Store the generated dataclass definition
        dataclass_definitions[original_event_type] = {
            "class_name": class_name,
            "definition": dataclass_definition
        }

    return dataclass_definitions, transformed_event_types, event_type_mapper


# Function to create unique event types file:
def create_unique_event_types_file(transformed_event_types: Dict[str, str], output_filepath: str):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    sorted_event_types = sorted(transformed_event_types.values())
    with open(output_filepath, 'w') as f:
        json.dump(sorted_event_types, f, indent=4)

# Function to create event attributes file:
def create_event_attributes_file(event_types: Dict[str, Set[str]], transformed_event_types: Dict[str, str], output_filepath: str):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    event_attribute_mapping = {}
    for event_type, attributes in event_types.items():
        class_name = transformed_event_types[event_type]
        event_attribute_mapping[class_name] = {"description": "Placeholder for event description.",
                                               "attributes": {"mention": "The text span that triggers the event."}}
        for attribute in sorted(attributes):
            event_attribute_mapping[class_name]["attributes"][attribute] = "Placeholder for attribute description."
    with open(output_filepath, 'w') as f:
        json.dump(event_attribute_mapping, f, indent=4)

# Function to save the event type mapper:
def save_event_type_mapper(event_type_mapper: Dict[str, str], output_filepath: str):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, 'w') as f:
        json.dump(event_type_mapper, f, indent=4)

# # Function to convert the JSON data to the desired format:
def convert_json_to_format_E2E_ED(input_filepath, master_file, mapper_file, instance_id, event_types,transformed_event_types, guidelines, custom_sep=None, dataset_name=None, task_type=None):

    with open(input_filepath, 'r') as file:
        for line in file:
            # first_line = file.readline()
            # print("First line of the file:", first_line)
            # file.seek(0) 
            json_data = json.loads(line.strip())
            # dataclass_definitions, _, _ = generate_dataclass_definitions(event_types, custom_sep, dataset_name)
            dataclass_definitions, _, _ = generate_dataclass_definitions(event_types, custom_sep, dataset_name, task_type=task_type)

            event_instances = {}  # To track unique event types and group mentions of the same event type
            has_events = False     # To track if there are any events in the current document

            # Iterate over each event mention in the document
            for event in json_data.get('event_mentions', []):
                event_type = event['event_type']
                class_name = dataclass_definitions[event_type]["class_name"]
                class_instance_name = class_name.split('(')[0]  # Extracting simple class name

                has_events = True  # Mark that this document has event mentions

                # If this event type has not been added yet, create a new entry
                if class_name not in event_instances:
                    event_instances[class_name] = {
                        "doc_id": json_data["doc_id"],
                        "wnd_id": json_data.get("wnd_id", ""),  # Use get() to avoid KeyError if wnd_id is missing
                        "instance_id": str(instance_id),
                        "text": json_data["text"],
                        "event_mentions": {
                            class_name: {
                                "definition": dataclass_definitions[event_type]["definition"],
                                "output_found": 0,
                                "results": []
                            }
                        }
                    }
                    instance_id += 1  # Increment instance_id for each unique event type

                # Initialize the result with the mention attribute
                mention_text = event['trigger']['text'].replace('"', '\\"')  # Escaping quotes for mention
                event_instance_str = f'{class_instance_name}(\n    mention="{mention_text}"'

                # Only collect and include arguments if the task is not ED
                if task_type != "ED":
                    # Collect arguments and append them to the same event type
                    event_args = defaultdict(list)
                    for argument in event.get('arguments', []):
                        role = argument['role'].lower().replace('-', '_')
                        text = argument['text'].replace('"', '\\"')  # Escaping double quotes
                        event_args[role].append(f'"{text}"')

                    # Adding event arguments present in the data
                    if event_args:
                        event_instance_str += ",\n" + ", \n".join(
                            f'    {role}=[{", ".join(texts)}]' for role, texts in event_args.items()
                        )

                event_instance_str += "\n)"

                # Skip missing attributes for ED datasets
                if task_type != "ED":
                    # Use the helper function to complete attributes
                    # modified_event_instance_str = complete_event_attributes(event_type, event_instance_str, guidelines)
                    modified_event_instance_str = complete_event_attributes(event_type, event_instance_str, guidelines, transformed_event_types)
                else:
                    modified_event_instance_str = event_instance_str

                # Append this result to the corresponding event mention in the event_instances dictionary
                event_instances[class_name]["event_mentions"][class_name]["results"].append(modified_event_instance_str)
                event_instances[class_name]["event_mentions"][class_name]["output_found"] += 1

            # If no event mentions, still add an instance with an empty event_mentions
            if not has_events:
                # print("Json Data:", json_data)
                json_data = append_random_event_definition(json_data, dataclass_definitions)
                # print("Modified json_data to write:", json_data)

                # Prepare data structure to write to file
                instance_data = {
                    "doc_id": json_data["doc_id"],
                    "wnd_id": json_data.get("wnd_id", ""),
                    "instance_id": str(instance_id),
                    "text": json_data["text"],
                    "event_mentions": json_data['event_mentions']  # This now includes the random event definition if there were no events
                }
                # print("Instance_Data:", instance_data)
                master_file.write(json.dumps(instance_data) + "\n")

                # empty_instance = {
                #     "doc_id": json_data["doc_id"],
                #     "wnd_id": json_data.get("wnd_id", ""),
                #     "instance_id": str(instance_id),
                #     "text": json_data["text"],
                #     "event_mentions": {}  # No event mentions
                # }
                # master_file.write(json.dumps(empty_instance) + "\n")

                # Create a mapper entry for tracking
                mapper_entry = {
                    "doc_id": json_data["doc_id"],
                    "wnd_id": json_data.get("wnd_id", ""),
                    "inst_id": str(instance_id),
                    "text": json_data["text"],
                    "output": {}  # No events mapped
                }
                mapper_file.write(json.dumps(mapper_entry) + "\n")

                # Increment instance_id for the empty instance
                instance_id += 1

            # Write all the unique event type instances into the master_file and mapper_file
            for class_name, event_instance in event_instances.items():
                master_file.write(json.dumps(event_instance) + "\n")

                # Create a mapper entry for tracking
                mapper_entry = {
                    "doc_id": event_instance["doc_id"],
                    "wnd_id": event_instance["wnd_id"],
                    "inst_id": event_instance["instance_id"],
                    "text": event_instance["text"],
                    "output": {class_name: event_instance["event_mentions"][class_name]["output_found"]}
                }
                mapper_file.write(json.dumps(mapper_entry) + "\n")

    return instance_id

def convert_json_to_format_EAE(input_filepath, master_file, mapper_file, instance_id, event_types, transformed_event_types, guidelines, custom_sep=None, dataset_name=None, task_type=None):
    with open(input_filepath, 'r') as file:
        for line in file:
            json_data = json.loads(line.strip())
            dataclass_definitions, _, _ = generate_dataclass_definitions(event_types, custom_sep, dataset_name, task_type=task_type)
            # print("dataclass_definitions:")
            # print(dataclass_definitions)
            # Handle instances with no event mentions

            # Create a deep copy of dataclass_definitions and update class_name in the copy to append '(Event)'
            dataclass_definitions_withevent = copy.deepcopy(dataclass_definitions)
            for key, value in dataclass_definitions_withevent.items():
                value['class_name'] += '(Event)'

            # print("dataclass_definitions_withevent")
            # print(dataclass_definitions_withevent)

            if not json_data.get('event_mentions', []):

                # Append a random event definition using the new function
                # print("Json Data:", json_data)
                # json_data = append_random_event_definition(json_data, dataclass_definitions)

                # Check if the dataset is either 'rams' or 'wikievents'
                if dataset_name in ['rams', 'wikievents']:
                    json_data = append_random_event_definition(json_data, dataclass_definitions_withevent)
                else:
                    json_data = append_random_event_definition(json_data, dataclass_definitions)

                # print("Modified json_data to write:", json_data)

                # Prepare data structure to write to file
                output = {
                    "doc_id": json_data["doc_id"],
                    "wnd_id": json_data.get("wnd_id", ""),
                    "instance_id": str(instance_id),
                    "text": json_data["text"],
                    "event_mentions": json_data['event_mentions']  # This now includes the random event definition if there were no events
                }
                # print("output:", output)
                master_file.write(json.dumps(output) + "\n")
                
                # output = {
                #     "doc_id": json_data["doc_id"],
                #     "wnd_id": json_data["wnd_id"],
                #     "instance_id": str(instance_id),
                #     "text": json_data["text"],
                #     "event_mentions": {}  # No event mentions
                # }
                # master_file.write(json.dumps(output) + "\n")

                mapper_entry = {
                    "doc_id": json_data["doc_id"],
                    "wnd_id": json_data["wnd_id"],
                    "inst_id": str(instance_id),
                    "text": json_data["text"],
                    "output": {}  # No event mentions to map
                }
                mapper_file.write(json.dumps(mapper_entry) + "\n")

                instance_id += 1
                continue  # Skip further processing for this instance if there are no event mentions

            # Group events by trigger text and event type
            event_group = defaultdict(lambda: defaultdict(list))

            # Process each event mention
            for event in json_data.get('event_mentions', []):
                event_type = event['event_type']
                # print("event_type: ")
                # print(event_type)
                # print("transformed_event_types: ")
                # print(transformed_event_types)
                class_name_with_event = transformed_event_types[event_type]  # Includes '(Event)' suffix
                # class_instance_name = class_name_with_event.split('(')[0]
                # print(class_name_with_event)
                # print(class_name_with_event)
                # No need to derive class_name separately here
                definition = dataclass_definitions[event_type]["definition"]
                # print(definition)
                trigger_text = event['trigger']['text']
                # print(trigger_text)

                # Create a unique key for grouping
                event_key = f"{trigger_text}_{class_name_with_event}"
                # print("event_key")
                # print(event_key)

                # Collect event arguments
                event_args = defaultdict(list)
                for argument in event.get('arguments', []):
                    role = argument['role'].lower().replace('-', '_')  # Normalize role names
                    text = argument['text'].replace('"', '\\"')  # Escaping double quotes
                    event_args[role].append(f'"{text}"')

                # Append event details to the group
                event_group[event_key][class_name_with_event].append({
                    "definition": definition,
                    "mention": trigger_text,
                    "event_args": event_args
                })

                # print(event_group)
                # print("**************")

            # Write grouped event mentions to the master and mapper files
            for event_key, class_dict in event_group.items():

                # print("event_key")
                # print(event_key)

                # print("class_dict")
                # print(class_dict)

                for class_name_with_event, event_list in class_dict.items():
                    class_instance_name = class_name_with_event.split('(')[0]
                    # No need to derive class_name separately
                    results = []
                    for event_instance in event_list:
                        # Use class_name_with_event directly
                        # event_instance_str = f'{class_name_with_event}(\n    mention="{event_instance["mention"]}"'
                        event_instance_str = f'{class_instance_name}(\n    mention="{event_instance["mention"]}"'
                        # print(event_instance_str)

                        # print("++++++++")
                        # print(event_instance_str)
                        # print("++++++++")

                        # Merge attributes into the event instance string
                        if task_type != "ED":
                            event_instance_str += ",\n" + ", \n".join(
                                f'    {role}=[{", ".join(texts)}]' for role, texts in event_instance["event_args"].items()
                            )
                        event_instance_str += "\n)"
                        # print("$$$$$$$$$$$$$$$$$$$$$$$$$")
                        # print(event_instance_str)
                        # print("$$$$$$$$$$$$$$$$$$$$$$$$$")

                        # Use the helper function to complete attributes
                        # modified_event_instance_str = complete_event_attributes(event_type, event_instance_str, guidelines)
                        
                        modified_event_instance_str = complete_event_attributes(class_name_with_event, event_instance_str, guidelines, transformed_event_types)
                        # print("modified_event_instance_str")
                        # print(modified_event_instance_str)

                        results.append(modified_event_instance_str)

                    # Create a single output entry for each trigger and event type
                    output = {
                        "doc_id": json_data["doc_id"],
                        "wnd_id": json_data["wnd_id"],
                        "instance_id": str(instance_id),
                        "text": json_data["text"],
                        "event_mentions": {
                            class_name_with_event: {
                                "definition": event_list[0]["definition"],  # Same definition for all instances of the same event type
                                "output_found": len(results),
                                "results": results  # Add all separate instances for the same trigger and event type
                            }
                        }
                    }

                    master_file.write(json.dumps(output) + "\n")

                    # Create a mapper entry for tracking
                    mapper_entry = {
                        "doc_id": json_data["doc_id"],
                        "wnd_id": json_data["wnd_id"],
                        "inst_id": str(instance_id),
                        "text": json_data["text"],
                        "output": {class_name_with_event: len(results)}  # Track the number of instances
                    }
                    mapper_file.write(json.dumps(mapper_entry) + "\n")

                    # Increment the instance_id for each unique event trigger
                    instance_id += 1

    return instance_id

# Function to add guidelines to the event class definitions:
# def add_guidelines_to_event_definitions(input_filepath, guidelines_filepath, output_filepath, is_random):
def add_guidelines_to_event_definitions(input_filepath, guidelines_filepath, output_filepath, is_random, task_type=None):

    # Loading the guidelines from the JSON file:
    with open(guidelines_filepath, 'r') as guidelines_file:
        guidelines = json.load(guidelines_file)

    # Processing the master preprocessed file and adding guidelines:
    with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
        for line in input_file:
            instance = json.loads(line.strip())

            # Processing each event mention:
            for event_class_name, event_details in instance.get("event_mentions", {}).items():
                if event_class_name in guidelines:
                    event_guideline = guidelines[event_class_name]

                    # Check if the event description is a list or a string
                    if isinstance(event_guideline["description"], list):
                        # Determining the number of descriptions available:
                        num_descriptions = len(event_guideline["description"])

                        # Picking the index based on the flag `is_random`:
                        if is_random:
                            selected_index = random.randint(0, num_descriptions - 1)
                        else:
                            selected_index = 0  # Picking the 0th index if not random:

                        # Determining if the selected description is authentic:
                        if num_descriptions == 6 and selected_index == 0:
                            is_auth = 1  # Marking as authentic description:
                        else:
                            is_auth = 0  # Marking as synthetic description:

                        # Adding the docstring (event description) after the class declaration:
                        event_description = event_guideline["description"][selected_index]
                    else:
                        # Directly use the string description if it's not a list
                        event_description = event_guideline["description"]
                        is_auth = 1  # Default to authentic if there's only one description

                    # Modifying the definition to ensure event description is after the class declaration:
                    definition_lines = event_details["definition"]

                    # First line: @dataclass decorator:
                    updated_definition = [definition_lines[0]]  # Adding @dataclass decorator:

                    # Second line: class <EventName>(<SuperClass>) without event description:
                    updated_definition.append(definition_lines[1])  # Adding class line:

                    # Adding the docstring (event description) after the class declaration:
                    updated_definition.append(f'    """{event_description}"""')

                    # Ensuring the 'mention' attribute always gets its description:
                    mention_description = event_guideline["attributes"].get("mention", "The text span that triggers the event.")
                    updated_definition.append(f"    mention: str  # {mention_description}")

                    # Only add other attributes if the task is not ED
                    if task_type != "ED":
                        # Adding all other attributes based on the selected index:
                        for attr_name, attr_descriptions in event_guideline["attributes"].items():
                            if attr_name != "mention":
                                if isinstance(attr_descriptions, list):
                                    attr_description = attr_descriptions[selected_index]
                                else:
                                    attr_description = attr_descriptions
                                updated_definition.append(f"    {attr_name.replace('-', '_')}: List  # {attr_description}")

                    # Updating the definition in the event details and adding `is_auth` flag:
                    instance["event_mentions"][event_class_name]["definition"] = updated_definition
                    instance["event_mentions"][event_class_name]["is_auth"] = is_auth

            # Writing the updated instance back to the output file:
            output_file.write(json.dumps(instance) + "\n")


# Helper function to create directories if they do not exist
def ensure_directories_exist(filepath):
    """
    Ensure all directories in the given filepath exist.
    """
    if filepath and filepath != "None":  # Check if the filepath is not None or "None"
        dir_path = os.path.dirname(filepath)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

# Main function to parse arguments and execute the processing workflow:
def main():
    parser = argparse.ArgumentParser(description="Process event types and attributes.")
    
    # Defining command-line arguments for file paths:
    parser.add_argument('--task', type=str, required=True, choices=["E2E", "ED", "EAE"], help='Task type: E2E, ED, or EAE')
    parser.add_argument('--root_dir', type=str, required=True, help='Path to the root dataset directory.')
    parser.add_argument('--master_data', type=str, help='Path to the master output file (optional, controlled by flag).')
    parser.add_argument('--mapper_data', type=str, help='Path to the document-instance mapper file (optional, controlled by flag).')
    parser.add_argument('--master_event_types', type=str, help='Path to save unique event types JSON file (optional).')
    parser.add_argument('--master_event_attributes', type=str, help='Path to save event attributes JSON file (optional).')
    parser.add_argument('--mapper_event_filepath', type=str, required=True, help="Path to save the original-to-transformed event type mapper")
    parser.add_argument('--guidelines_filepath', type=str, help='Path to the event guidelines file (optional).')
    parser.add_argument('--final_output_filepath', type=str, help='Path to the final output file with guidelines (optional).')
    
    # New flags to control task execution:
    parser.add_argument('--custom_sep', type=str, help="Custom separator for event types")
    parser.add_argument('--dataset', type=str, help="Dataset name (e.g., rams, wikievents)")
    parser.add_argument('--generate_unique_event_types', type=int, default=0, help='1 to generate unique event types JSON file, 0 to skip.')
    parser.add_argument('--generate_event_attributes', type=int, default=0, help='1 to generate event attributes JSON file, 0 to skip.')
    parser.add_argument('--generate_final_output', type=int, default=0, help='1 to generate master/mapper and final output, 0 to skip.')
    parser.add_argument('--is_random', type=int, default=1, help='1 to pick random guideline, 0 to pick 0th index.')

    args = parser.parse_args()

    # Ensure directories for each provided path
    ensure_directories_exist(args.master_data)
    ensure_directories_exist(args.mapper_data)
    ensure_directories_exist(args.master_event_types)
    ensure_directories_exist(args.master_event_attributes)
    ensure_directories_exist(args.mapper_event_filepath)
    ensure_directories_exist(args.guidelines_filepath)
    ensure_directories_exist(args.final_output_filepath)

    instance_id = 1

    # Loading all JSON data from the dataset files:
    all_json_data = []
    for filename in ['train.json', 'dev.json', 'test.json']:
        input_filepath = os.path.join(args.root_dir, filename)
        if os.path.exists(input_filepath):
            with open(input_filepath, 'r') as file:
                for line in file:
                    json_data = json.loads(line.strip())
                    all_json_data.append(json_data)
    
    # Collecting event types and attributes from all data:
    event_types = collect_event_attributes(all_json_data)

    # Load the guidelines file if provided
    if args.guidelines_filepath and os.path.exists(args.guidelines_filepath):
        with open(args.guidelines_filepath, 'r') as guidelines_file:
            guidelines = json.load(guidelines_file)
    else:
        guidelines = {}

    # Generate dataclass definitions
    # _, transformed_event_types, event_type_mapper = generate_dataclass_definitions(event_types, args.custom_sep, args.dataset)
    # _, transformed_event_types, event_type_mapper = generate_dataclass_definitions(event_types, args.custom_sep, args.dataset, task_type=args.task)
    #Just for checking:
    _, transformed_event_types, event_type_mapper = generate_dataclass_definitions(event_types, args.custom_sep, args.dataset, task_type=args.task)

    # dataclass_definitions, transformed_event_types, event_type_mapper = generate_dataclass_definitions(event_types, args.custom_sep, args.dataset, task_type=args.task)
    # print("Available Dataclass Definitions:", dataclass_definitions)

    # Optionally creating unique event types file:
    if args.generate_unique_event_types:
        create_unique_event_types_file(transformed_event_types, args.master_event_types)

    # Optionally creating event-to-attributes mapping file:
    if args.generate_event_attributes:
        create_event_attributes_file(event_types, transformed_event_types, args.master_event_attributes)
         
    # Save the event type mapper
    save_event_type_mapper(event_type_mapper, args.mapper_event_filepath)

    # Choose the appropriate conversion function based on task type
    if args.task == "EAE":
        conversion_function = convert_json_to_format_EAE
    else:
        conversion_function = convert_json_to_format_E2E_ED

    # Always generate the master and mapper files, irrespective of generate_final_output flag
    with open(args.master_data, 'w') as master_file, open(args.mapper_data, 'w') as mapper_file:
        for filename in ['train.json', 'dev.json', 'test.json']:
            input_filepath = os.path.join(args.root_dir, filename)
            if os.path.exists(input_filepath):
                # instance_id = conversion_function(input_filepath, master_file, mapper_file, instance_id,event_types, transformed_event_types, None, custom_sep=args.custom_sep, dataset_name=args.dataset,task_type=args.task)
                instance_id = conversion_function(input_filepath, master_file, mapper_file, instance_id,event_types, transformed_event_types, guidelines,custom_sep=args.custom_sep, dataset_name=args.dataset, task_type=args.task)
                
    # Only add guidelines if generate_final_output is set to 1
    if args.generate_final_output and args.guidelines_filepath:
        # add_guidelines_to_event_definitions(args.master_data, args.guidelines_filepath, args.final_output_filepath, args.is_random)
        add_guidelines_to_event_definitions(args.master_data, args.guidelines_filepath, args.final_output_filepath,args.is_random, task_type=args.task)

if __name__ == "__main__":
    main()
