import json
from enum import Enum

# json_file = ""


# with open('./BatchJobsPrompts.json') as json_data:
#     json_file = json.load(json_data)
#
# print(json_file["prompts"]["small_prompt"])

class PromptType(Enum):
    SMALL_PROMPT = "small_prompt"
    MEDIUM_PROMPT = "medium_prompt"
    LARGE_PROMPT = "large_prompt"
    SYSTEM_SMALL_PROMPT = "system_small_prompt"
    SYSTEM_MEDIUM_PROMPT = "system_medium_prompt"
    SYSTEM_LARGE_PROMPT = "system_large_prompt"


class TestType(Enum):
    ATL_PROMPT = "ATLPROMPTS"
    BATCH_JOBS_PROMPT = "BATCHJOBSPROMPTs"
    DISPLAY_FUNCTION_PROMPT = "DISPLAYFUNCTIONPROMPTS"
    UNIT_TEST_PROMPT = "UNITTESTPROMPTS"


def return_json_information(promptType: PromptType, testType: TestType):
    json_file: str
    with open(f"./{testType.value}.json") as json_data:
        json_file = json.load(json_data)["prompts"][promptType.value]
    print(json_file)
    return json_file


return_json_information(PromptType.SMALL_PROMPT, TestType.BATCH_JOBS_PROMPT)


