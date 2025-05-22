import os
import re
import argparse

def extract_classes_and_attributes(file_content):
    """
    Extracts classes and their attributes from the provided Python file content.
    Returns a dictionary with class signature (name + parent) as keys and attributes as values.
    """
    class_pattern = re.compile(r'@dataclass\nclass (\w+)\((\w+)\):\n((?:\s+\w+:\s+\w+\n)*)', re.MULTILINE)
    classes = {}
    
    for match in class_pattern.finditer(file_content):
        class_name = match.group(1)
        parent_class = match.group(2)
        attributes = match.group(3).strip().splitlines()
        # Remove empty lines
        attributes = [attr.strip() for attr in attributes if attr.strip()]
        
        # Create a class signature: class_name(parent_class)
        class_signature = f"{class_name}({parent_class})"
        
        # Store attributes for this class signature
        classes[class_signature] = {
            "parent_class": parent_class,
            "attributes": attributes
        }
    
    return classes

def merge_class_attributes(master_classes, new_classes):
    """
    Merge the new classes and attributes into the master class dictionary.
    The comparison is done by checking the entire class signature.
    """
    for class_signature, class_data in new_classes.items():
        if class_signature not in master_classes:
            # Add the entire new class if it doesn't exist in master
            master_classes[class_signature] = class_data
        else:
            # Merge attributes if the class already exists in the master
            master_attributes = master_classes[class_signature]["attributes"]
            new_attributes = class_data["attributes"]
            
            # Add missing attributes
            for attr in new_attributes:
                if attr not in master_attributes:
                    master_attributes.append(attr)
                    
    return master_classes

def write_master_dataclass(master_classes, output_file):
    """
    Writes the consolidated classes into the master dataclass file.
    Step 1: Classes with only `pass` are identified and separated.
    Step 1.1: Classes with Event as parent come first.
    Step 1.2: Classes with other parents but having only pass come next.
    Step 2: Remaining classes with attributes are placed at the bottom.
    """
    with open(output_file, 'w') as f:
        f.write("from dataclasses import dataclass\nfrom typing import List\n\n")

        # Separate classes into different categories
        event_pass_classes = []
        non_event_pass_classes = []
        attribute_classes = []

        for class_signature, class_data in master_classes.items():
            class_name, parent_class = class_signature.split('(')
            parent_class = parent_class.strip(')')

            if not class_data["attributes"]:
                # Classes with pass only
                if parent_class == "Event":
                    event_pass_classes.append((class_name, parent_class))
                else:
                    non_event_pass_classes.append((class_name, parent_class))
            else:
                # Classes with attributes
                attribute_classes.append((class_signature, class_data))

        # Write base classes with pass and Event as parent (Step 1.1)
        for class_name, parent_class in event_pass_classes:
            f.write(f"@dataclass\nclass {class_name}({parent_class}):\n")
            f.write("    pass\n\n")

        # Write base classes with pass and non-Event parents (Step 1.2)
        for class_name, parent_class in non_event_pass_classes:
            f.write(f"@dataclass\nclass {class_name}({parent_class}):\n")
            f.write("    pass\n\n")

        # Now write the classes with attributes (Step 2)
        for class_signature, class_data in attribute_classes:
            class_name, parent_class = class_signature.split('(')
            parent_class = parent_class.strip(')')
            f.write(f"@dataclass\nclass {class_name}({parent_class}):\n")
            for attr in class_data["attributes"]:
                f.write(f"    {attr}\n")
            f.write("\n")

def consolidate_dataclass_files(datasets, input_dir, output_file):
    master_classes = {}

    for dataset in datasets:
        filename = f"Dataclass_{dataset}.py"
        filepath = os.path.join(input_dir, dataset, filename)

        if os.path.exists(filepath):
            # print(f"Processing {filepath}")
            with open(filepath, 'r') as f:
                file_content = f.read()
                new_classes = extract_classes_and_attributes(file_content)
                master_classes = merge_class_attributes(master_classes, new_classes)
        else:
            print(f"File {filepath} not found!")

    # Write the consolidated classes to the master dataclass file
    write_master_dataclass(master_classes, output_file)
    # print(f"Master dataclass file saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consolidate dataclass Python files from multiple datasets.")
    
    # Define the arguments
    parser.add_argument('--datasets', nargs='+', required=True, help="List of dataset names to process in order.")
    parser.add_argument('--input_dir', required=True, help="Directory where the input Python files are located.")
    parser.add_argument('--output_file', required=True, help="File to save the consolidated master dataclass.")
    
    args = parser.parse_args()

    # Call the function to consolidate the dataclass files
    consolidate_dataclass_files(args.datasets, args.input_dir, args.output_file)
