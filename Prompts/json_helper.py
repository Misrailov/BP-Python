import json
from enum import Enum

# json_file = ""


# with open('./BatchJobsPrompts.py') as json_data:
#     json_file = json.load(json_data)
#
# print(json_file["prompts"]["small_prompt"])
from . import BatchJobsPrompts


from . import ATLPrompts
from . import DisplayFunctionPrompts
from . import UnitTestPrompts
class PromptType(Enum):
    SMALL_PROMPT = "small_prompt"
    MEDIUM_PROMPT = "medium_prompt"
    LARGE_PROMPT = "large_prompt"
    SYSTEM_SMALL_PROMPT = "system_small_prompt"
    SYSTEM_MEDIUM_PROMPT = "system_medium_prompt"
    SYSTEM_LARGE_PROMPT = "system_large_prompt"





def return_json_information_batch(promptType: PromptType):
    return BatchJobsPrompts.prompts[promptType.value]
def return_json_information_atl(promptType: PromptType):
    return ATLPrompts.prompts[promptType.value]
def return_json_information_dp(promptType: PromptType):
    return DisplayFunctionPrompts.prompts[promptType.value]
def return_json_information_ut(promptType: PromptType):
    return UnitTestPrompts.prompts[promptType.value]




