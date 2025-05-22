import os
import json
import argparse
from dataclasses import dataclass
from typing import List, Dict, Set
from collections import defaultdict

# Utility function to convert hyphenated event names to CamelCase:
def to_camel_case(s):
    return ''.join(part.capitalize() for part in s.split('-'))

# Utility function to handle 'n/a' and RAMS/WikiEvents formatting
def to_rams_event_name(s):
    return s.replace('n/a', 'Na')

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
                        # Replace hyphens in attribute names with underscores
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
        # print("reversed(parts)")
        # print(part)
        if part.lower() == 'n/a':  # Handle 'n/a' conversion to 'Na'
            part = 'Na'
        if part not in seen:
            result.append(part) #Returning only the parts with no duplicates:
            seen.add(part)
        # print(result)
    return list(reversed(result))

# # Function to generate data class definitions:
def generate_dataclass_definitions(event_types: Dict[str, Set[str]], custom_sep: str = None, dataset_name: str = None) -> Dict[str, Dict[str, List[str]]]:
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

def save_full_hierarchy(event_types: Dict[str, Set[str]], output_python_filepath: str, output_json_filepath: str, dataset_name: str = None, custom_sep: str = None):
    class_hierarchy = []  # Store the hierarchy in the correct order for child classes (ACE) or flat hierarchy (RAMS/WikiEvents)
    parent_classes = set()  # Only for ACE
    unique_events = set()
    declared_classes = set()  # Track classes already declared (ACE)
    
    for event_type in event_types.keys():
        is_flat_hierarchy = False  # Flag to check if it's a flat hierarchy dataset
        
        # Check for RAMS/WikiEvents or flat hierarchy
        if dataset_name in ["rams", "wikievents"]:
            is_flat_hierarchy = True
            transformed_event_type = event_type.replace(':', '_').replace('.', '_')
            class_name = to_rams_event_name(transformed_event_type)

            # Initialize the class definition with the @dataclass decorator and the Event inheritance
            class_definition = f"@dataclass\nclass {class_name}(Event):\n    mention: str"
            
            # Retrieve the attributes using the original (period-separated) event type name
            attributes = sorted(event_types[event_type])
            if attributes:  # Only add if there are attributes
                for attribute in attributes:
                    class_definition += f"\n    {attribute.replace('-', '_')}: List"
            
            # Append the class definition to the hierarchy
            class_hierarchy.append(class_definition)
            unique_events.add(f"{class_name}(Event)")
        
        else:
            # ACE specific logic and flat hierarchy check
            if custom_sep and custom_sep.lower() != "none" and custom_sep in event_type:
                parts = event_type.split(custom_sep)
            elif ':' in event_type:
                parts = event_type.split(':')
            elif '.' in event_type:
                parts = event_type.split('.')
            else:
                parts = [event_type]

            # print("--------------------------------------------------------------------------------------------")
            # print("parts")
            # print(parts)

            # Ensure the parts list is not empty after removing duplicates
            parts = remove_duplicate_hierarchy(parts)
            if not parts:
                raise ValueError(f"Event type {event_type} resulted in an empty parts list after removing duplicates.")

            # print("remove_duplicate")
            # print(parts)

            # If no splitting occurred, treat it as flat hierarchy
            if len(parts) == 1:
                is_flat_hierarchy = True

            # Handle single-part event types (flat hierarchy) outside the loop
            if len(parts) == 1:
                # This is a flat hierarchy event type, treat it as a child class with Event as parent
                top_class = to_camel_case(parts[0])
                class_definition = f"@dataclass\nclass {top_class}(Event):\n    mention: str"
                attributes = sorted(event_types[event_type])
                for attribute in attributes:
                    class_definition += f"\n    {attribute.replace('-', '_')}: List"
                class_hierarchy.append(class_definition)
                unique_events.add(f"{top_class}(Event)")
                # print("class_definition")
                # print(class_definition)
                continue  # Skip the rest of the loop for this case

            # Generate class hierarchy from parent to child
            class_definitions = []
            lowest_class = True  # Flag to track the lowest child class

            for i in range(len(parts) - 1, 0, -1):
                child_class = to_camel_case(parts[i])
                parent_class = to_camel_case(parts[i - 1]) + "Event"

                # Store the parent class in the parent_classes set, ensuring it's printed first later
                if parent_class not in declared_classes:
                    parent_classes.add(parent_class)
                    # print("parent_classes")
                    # print(parent_classes)
                    declared_classes.add(parent_class)
                    # print("declared_classes")
                    # print(declared_classes)
                    unique_events.add(f"{parent_class}(Event)")  # Ensure parent classes are stored as `ParentClass(Event)`

                # Handle the lowest child class with attributes
                if child_class != parent_class:
                    if lowest_class:
                        # Add attributes only to the lowest child class
                        attributes = sorted(event_types[event_type])
                        class_definition = f"@dataclass\nclass {child_class}({parent_class}):\n    mention: str"
                        for attribute in attributes:
                            class_definition += f"\n    {attribute.replace('-', '_')}: List"
                            # print("class_definition")
                            # print(class_definition)
                        lowest_class = False  # Mark that we've processed the lowest class
                    else:
                        # For intermediate or parent classes without attributes, just use 'pass'
                        if child_class not in declared_classes:
                            class_definition = f"@dataclass\nclass {child_class}({parent_class}):\n    pass\n"
                            # print("class_definition")
                            # print(class_definition)
                            declared_classes.add(child_class)

                    class_definitions.append(class_definition)
                    unique_events.add(f"{child_class}({parent_class})")  # Store child class in correct format

            # Add the top-most class with 'Event' as the parent, if it hasn't been declared
            if len(parts) > 1:  # Ensure this part only runs for multi-part hierarchies
                top_class = to_camel_case(parts[0])
                top_class_event = f"{top_class}Event"  # E.g., LifeEvent
                if top_class_event not in declared_classes:
                    parent_classes.add(top_class_event)
                    declared_classes.add(top_class_event)
                    unique_events.add(f"{top_class_event}(Event)")  # Ensure the top class is added as `TopClassEvent(Event)`
                class_hierarchy.extend(reversed(class_definitions))

    # Write the class hierarchy to the output Python file
    os.makedirs(os.path.dirname(output_python_filepath), exist_ok=True)
    with open(output_python_filepath, 'w') as f:
        # Add the @dataclass import at the top
        f.write("from dataclasses import dataclass\n\n")
        
        # Write parent classes for ACE (if any)
        if dataset_name not in ["rams", "wikievents"]:
            for parent_class in sorted(parent_classes):  # Sorted ensures consistent ordering
                f.write(f"@dataclass\nclass {parent_class}(Event):\n    pass\n\n")  # Add a newline after each parent class
        
        # Write each class definition into the Python file
        for class_def in class_hierarchy:
            f.write(class_def + "\n\n")

    # Write the unique events to a JSON file
    with open(output_json_filepath, 'w') as f:
        json.dump(sorted(unique_events), f, indent=4)

# Function to save the event type mapper:
def save_event_type_mapper(event_type_mapper: Dict[str, str], output_filepath: str):
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    with open(output_filepath, 'w') as f:
        json.dump(event_type_mapper, f, indent=4)


# Helper function to create directories if they do not exist
def ensure_directories_exist(filepath):
    """
    Ensure all directories in the given filepath exist.
    """
    if filepath and filepath != "None":  # Check if the filepath is not None or "None"
        dir_path = os.path.dirname(filepath)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

# Ontology preprocessing logic:
def ontology_preprocessing(root_dir, master_event_types, master_event_attributes, python_class_hierarchy, json_class_hierarchy, mapper_output_filepath, custom_sep=None, dataset=None):

    # Loading all JSON data from the dataset files:
    all_json_data = []
    for filename in ['train.json', 'dev.json', 'test.json']:
        input_filepath = os.path.join(root_dir, filename)
        if os.path.exists(input_filepath):
            with open(input_filepath, 'r') as file:
                for line in file:
                    json_data = json.loads(line.strip())
                    all_json_data.append(json_data)

    # Collect event types and attributes from all data
    event_types = collect_event_attributes(all_json_data)

    # Generate dataclass definitions
    _, transformed_event_types, event_type_mapper = generate_dataclass_definitions(event_types, custom_sep, dataset)

    # Create the required files
    create_unique_event_types_file(transformed_event_types, master_event_types)
    create_event_attributes_file(event_types, transformed_event_types, master_event_attributes)

    save_full_hierarchy(event_types, python_class_hierarchy, json_class_hierarchy, dataset, custom_sep)

    # Save the event type mapper
    save_event_type_mapper(event_type_mapper, mapper_output_filepath)

# Main script entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ontology Preprocessing.")
    parser.add_argument('--root_dir', type=str, required=True)
    parser.add_argument('--master_event_types', type=str, required=True)
    parser.add_argument('--master_event_attributes', type=str, required=True)
    parser.add_argument('--python_class_hierarchy', type=str, required=True)
    parser.add_argument('--json_class_hierarchy', type=str, required=True)
    parser.add_argument('--custom_sep', type=str, help="Custom separator for event types")
    parser.add_argument('--dataset', type=str, help="Dataset name (e.g., rams, wikievents)")
    parser.add_argument('--mapper_output_filepath', type=str, required=True, help="Path to save the original-to-transformed event type mapper")
    args = parser.parse_args()

    # Ensure directories only if valid paths are provided and not "None"
    ensure_directories_exist(args.master_event_types)
    ensure_directories_exist(args.master_event_attributes)
    ensure_directories_exist(args.python_class_hierarchy)
    ensure_directories_exist(args.json_class_hierarchy)
    ensure_directories_exist(args.mapper_output_filepath)

    ontology_preprocessing(
        args.root_dir,
        args.master_event_types,
        args.master_event_attributes,
        args.python_class_hierarchy,
        args.json_class_hierarchy,
        custom_sep=args.custom_sep,
        dataset=args.dataset,
        mapper_output_filepath=args.mapper_output_filepath
    )
