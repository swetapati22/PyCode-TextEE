PROMPT_P = """You are an expert in annotating NLP datasets for event extraction.Your task is to generate precise and detailed annotation guidelines for the event type [###Event_Type###]

### Input Format ###
```
Event Schema:
Event Name and its parent class
Arguments:
Arguments separated by new lines. If there are no arguments None will be given.

Examples:
Examples provided to illustrate the event type and arguments.
```

### Instructions ###
1. Identify and List All Unique Arguments: 
   - Carefully review the schema to identify all arguments relevant to the event type.
   - Please remember that the examples may not cover all the arguments in the list. In some cases, you may not have arguments at all, in such cases, you can have an empty list for arguments. 
2. Define the Event Type: Write 5 clear and specific definitions, starting with "The event is triggered by ...":
   - Include example triggers.
   - Highlight key characteristics and scope of the event.
   - Compare and contrast with closely related events using provided negative examples.
   - Explain how triggers and outcomes differ for similar event types.
3. Define Each Argument:** For each argument, provide 5 definitions with detailed examples, starting with "Examples are ...":
   - Explain the role and importance of each argument.
   - Include domain knowledge and address edge cases to clarify ambiguities.
4. Focus on Distinctions: Use positive examples to describe the event, and negative examples to clarify what the event is not. Explicitly state differences using phrases like:
   - "Unlike [Related Event Type], this event does not ..."
   - "Triggers such as [Trigger] are indicative of [Related Event Type], not this event type."
5. Structured Output: Present the output in the following JSON format:
   ```json
   {
     "Event Definition": [
       "Definition 1",
       "Definition 2",
       "Definition 3",
       "Definition 4",
       "Definition 5"
     ],
     "Arguments Definitions": {
       "Argument1": [
         "Definition 1",
         "Definition 2",
         "Definition 3",
         "Definition 4",
         "Definition 5"
       ],
       "Argument2": [
         "Definition 1",
         "Definition 2",
         "Definition 3",
         "Definition 4",
         "Definition 5"
       ]
       // Add more arguments if applicable
     }
   }
   ```

### Output Requirements ###
- Use detailed yet concise language for event and argument definitions.
- Incorporate diverse and domain-relevant examples for each definition.
- Avoid copying examples directly from provided data, create unique variations.

"""

PROMPT_INT = """You are an expert in summarizing NLP event extraction guidelines. Your goal is to consolidate multiple detailed descriptions into a single concise, comprehensive "Advanced" guideline.

### Input Format ###
Event Type: Event Type Name
```json
{
  "Event Definition": [
    "Definition 1",
    "Definition 2",
    "Definition 3",
    "Definition 4",
    "Definition 5"
  ],
  "Arguments Definitions": {
    "mention": [
      "Definition 1",
      "Definition 2",
      "Definition 3",
      "Definition 4",
      "Definition 5"
    ],
    "Argument1": [
      "Definition 1",
      "Definition 2",
      "Definition 3",
      "Definition 4",
      "Definition 5"
    ],
    // Add additional arguments as necessary
  }
}
```

### Task ###
1. Consolidate the 5 definitions under "Event Definition" into a single definition:
   - Highlight all critical points and examples from the five definitions.
   - Ensure the description is concise, comprehensive, and clear, using formal language that non-experts can understand.

2. Do the same for each argument under "Arguments Definitions," producing a single advanced definition for each. 

### Output Format ###
```json
{
  "Event Definition": "Consolidated advanced guideline for the event type.",
  "Arguments Definitions": {
    "mention": "Consolidated advanced guideline for the mention argument.",
    "Argument1": "Consolidated advanced guideline for Argument1.",
    "Argument2": "Consolidated advanced guideline for Argument2."
    // Add additional arguments as applicable
  }
}
```

### Guidelines to Summarize ###
Event Type: [###Event_Type###]
```json
[###Detailed_Guidelines###]
```
"""

negative_footer = "### The following examples are negative examples, as they illustrate different event types provided for contrast and differentiation: ###\n\n"
positive_footer = "### The below examples are positive examples, as they match the Event Type being annotated: ###\n\n"