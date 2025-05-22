import json
import argparse
from dataclasses import dataclass
from typing import List
import re

# Load the guidelines master
def load_guidelines(guidelines_filepath):
    with open(guidelines_filepath, "r") as f:
        return json.load(f)

# Function to get the instruction based on the task type
def get_instruction(task_type):
    if task_type == "ED":
        return "# This is an event detection task where the goal is to identify event triggers and their types in the text. For each event, please output the extracted information into python-style dictionaries where the key is 'mention' with the value of the event trigger. The event type definitions are defined next."
    elif task_type == "EAE":
        return "# This is an event argument extraction task where the goal is to extract the arguments of a given event trigger in the text. The event trigger and its type are provided. Please output the extracted arguments and their roles into python-style dictionaries. The event type definitions and their argument roles are defined next."
    else:  # E2E
        return "# This is an event extraction task where the goal is to extract structured events from the text. A structured event contains an event trigger word, an event type, the arguments participating in the event, and their roles in the event. For each different event type, please output the extracted information from the text into python-style dictionaries where the first key will be 'mention' with the value of the event trigger. Next, please output the arguments and their roles following the same format. The event type definitions and their argument roles are defined next."

###################Includes the functionality of handling multiple arguments in EAE###################################
def process_instance(instance, guidelines_master, task_type, dataset_name):
    # Get existing event definitions from the instance
    existing_event_definitions = {}
    is_auth_value = 0
    
    if instance['event_mentions']:
        for event_type, event_data in instance['event_mentions'].items():
            is_auth_value = event_data.get('is_auth', 0)
            # print("--"*50)
            # print(instance['event_mentions'])
            # print("event_type:", event_type)
            # print("event_data:", event_data)
            event_definition = "\n".join(event_data['definition'])
            existing_event_definitions[event_type] = event_definition
    else:
        existing_event_definitions = {}
    
    # Prepare the event definitions section
    if existing_event_definitions:
        event_definitions = "\n\n".join(existing_event_definitions.values()) + "\n\n"
    else:
        event_definitions = ""
    
    # Get the instruction
    instruction_text = get_instruction(task_type)
    
    # Prepare the input section
    input_section = f"# The following lines describe the task definition\n\n{event_definitions}"
    input_section += f"# This is the text to analyze\ntext = \"{instance['text']}\"\n\n"
    
    # if task_type == "EAE":
    #     if instance['event_mentions']:
    #         # Collect all event triggers and their classes
    #         triggers_info = []
    #         for event_type, event_info in instance['event_mentions'].items():
    #             class_name = event_type  # event_type is already the class name
    #             for result in event_info['results']:
    #                 print("result:", result)
    #                 # Extract the mention (trigger)
    #                 # mention_match = re.search(r'mention="([^"]+)"', result)
    #                 mention_match = re.search(r'mention="(.*?)(?<!\\)"', result)
    #                 if mention_match:
    #                     mention = mention_match.group(1)
    #                     # Also, extract the index or position if available to distinguish events
    #                     # For now, we can include the result index
    #                     triggers_info.append((class_name, mention))
    #         # Note: Do not remove duplicates
    #         # Add the dynamic lines for EAE
    #         input_section += "# The list called result contains the instances for the following events according to the guidelines above\n"
    #         for idx, (class_name, mention) in enumerate(triggers_info, 1):
    #             input_section += f"# {idx}. \"{mention}\" triggers a {class_name} event.\n"
    #         input_section += "\n"
    #     else:
    #         # Handle cases where there is no event mention in EAE
    #         input_section += "# No event mentions are present in this text.\n"
    #         input_section += "# The list called result should be empty.\n\n"

    if task_type == "EAE":
        if instance['event_mentions']:
            all_empty = True  # Track if all results arrays are empty
            triggers_info = []
            for event_type, event_info in instance['event_mentions'].items():
                class_name = event_type  # event_type is already the class name
                if event_info['results']:  # Using 'results' key to access actual results
                    all_empty = False  # Found at least one non-empty result
                    for result in event_info['results']:
                        mention_match = re.search(r'mention="(.*?)(?<!\\)"', result)
                        if mention_match:
                            mention = mention_match.group(1)
                            triggers_info.append((class_name, mention))
                else:
                    # Add a message even if there are no results
                    triggers_info.append((class_name, "No specific trigger found"))

            if not all_empty:
                input_section += "# The list called result contains the instances for the following events according to the guidelines above\n"
                for idx, (class_name, mention) in enumerate(triggers_info, 1):
                    input_section += f"# {idx}. \"{mention}\" triggers a {class_name} event.\n"
                input_section += "\n"
            else:
                input_section += "# No event mentions are present in this text with extractable arguments.\n"
                input_section += "# The list called result should be empty.\n\n"
        else:
            input_section += "# No event mentions are present in this text.\n"
            input_section += "# The list called result should be empty.\n\n"    
    else:
        input_section += "# The list called result should contain the instances for the following events according to the guidelines above:\n"
    
    input_section += "result = \n"
    # print("**"*10)
    # print("input_section:", input_section)
    
    # Prepare the output section based on event results
    output_section = []
    if instance['event_mentions']:
        for event_type, event_info in instance['event_mentions'].items():
            for result in event_info['results']:
                if task_type == "ED":
                    # Only include the mention attribute
                    class_name = event_type.split('(')[0]
                    # mention_match = re.search(r'mention="([^"]+)"', result)
                    mention_match = re.search(r'mention="(.*?)(?<!\\)"', result)
                    if mention_match:
                        mention = mention_match.group(1)
                        event_instance_str = f'{class_name}(\n    mention="{mention}"\n)'
                        output_section.append(event_instance_str.strip())
                else:
                    # Include arguments as is
                    output_section.append(result.strip())
    else:
        output_section = []
    
    # Combine everything into the final dictionary
    return {
        "doc_id": instance['doc_id'],
        "wnd_id": instance.get('wnd_id', ''),
        "instance_id": instance['instance_id'],
        "dataset_name": dataset_name,  # Add dataset name
        "task_type": task_type,        # Add task type
        "is_auth": str(is_auth_value),
        "instruction": instruction_text,
        "input": input_section,
        "output": "[" + ",\n".join(output_section) + "]" if output_section else "[]"
    }

# Function to process the entire final_master.json file
def convert_final_master_to_format(input_filepath, output_filepath, guidelines_master, task_type, dataset_name):
    with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
        final_output = []
        for line in infile:
            instance = json.loads(line.strip())  # Load each instance
            # formatted_instance = process_instance(instance, guidelines_master, task_type)  # Process the instance
            formatted_instance = process_instance(instance, guidelines_master, task_type, dataset_name)
            # print(formatted_instance)
            final_output.append(formatted_instance)  # Append the formatted instance to output

        # Save the transformed dataset
        json.dump(final_output, outfile, indent=4)

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Process input and output file paths for conversion.")
    parser.add_argument('--input_filepath', type=str, required=True, help='Path to the input JSON file.')
    parser.add_argument('--output_filepath', type=str, required=True, help='Path to save the output JSON file.')
    parser.add_argument('--guidelines_file', type=str, required=True, help='Path to the guidelines file.')
    parser.add_argument('--task', type=str, required=True, choices=["E2E", "ED", "EAE"], help='Task type: E2E, ED, or EAE')
    parser.add_argument('--dataset', type=str, required=True, help='Dataset name')

    args = parser.parse_args()

    # Load the guidelines
    guidelines_master = load_guidelines(args.guidelines_file)

    # Run the conversion
    # convert_final_master_to_format(args.input_filepath, args.output_filepath, guidelines_master, args.task)
    convert_final_master_to_format(args.input_filepath, args.output_filepath, guidelines_master, args.task, args.dataset)


    print(f"Conversion completed! Output saved to {args.output_filepath}")

if __name__ == "__main__":
    main()