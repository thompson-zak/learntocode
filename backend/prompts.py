RESPONSE_SECTIONS = " Your response should contain a prompt, an outline of steps to be completed, a code sample, and an explanation. The prompt should be first, the outline of steps should be second, the code sample should be third, and the explanation should come last."
SECTION_STRUCTURE = " Each section should be titled in <b> html tags and followed by an <hr> html tag. Each step in the outline of steps should be numbered and end with a period."
NO_INPUT_ONLY_PRINT = " This code should not contain any input statements and should rely only a print statements for displaying output."

def getPrompts(track: str):
    TRACK_CUSTOMIZATION = ""
    if track != "" or track != "None":
        TRACK_CUSTOMIZATION = " Your response should be {track} themed.".format(track=track)

    PROMPT_INSTRUCTIONS = TRACK_CUSTOMIZATION + RESPONSE_SECTIONS + SECTION_STRUCTURE + NO_INPUT_ONLY_PRINT
    prompts = {
        "Variables": {
            1: "Please provide a very basic problem to help a student who has never coded before learn python syntax and variables." + PROMPT_INSTRUCTIONS,
            2: "Please provide a prompt and code outline for a problem to help a student who has never coded before learn python syntax and variables." + PROMPT_INSTRUCTIONS
        },
        # This could be extended to include Queues/Stacks, Linked Lists, etc.
        "Data": {
            1: "Please provide a very basic problem to help a student who has only coded once before learn how to use python arrays." + PROMPT_INSTRUCTIONS,
            2: "Please provide a problem to help a student who has only coded once before learn how to use python dictionaries." + PROMPT_INSTRUCTIONS
        },
        # This could be extended to include Ternary statements.
        "Conditionals": {
            1: "Please provide a basic problem to help a student who has only coded once before learn how to use a python if statement." + PROMPT_INSTRUCTIONS,
            2: "Please provide a basic problem to help a student who has only coded once before learn how to use a python if, else, and elif statement." + PROMPT_INSTRUCTIONS
        },
        # This could be extended to include Nested Loops and Loops with 'else' statement.
        "Loops": {
            1: "Please provide a basic problem to help a student who has only coded once before learn how to use python for loops." + PROMPT_INSTRUCTIONS,
            2: "Please provide a basic problem to help a student who has only coded once before learn how to use python while loops." + PROMPT_INSTRUCTIONS
        }
}
    return prompts