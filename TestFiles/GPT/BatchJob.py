from API.GPT import send_message_to_api_and_return_request

from Mongo import MongoWriter
from Prompts import json_helper
from Prompts.json_helper import PromptType

prompt_category = "batch-job"

gpt_4 = "gpt-4-turbo"
gpt_3_5 = "gpt-3.5-turbo-0125"

# Small Prompt
sp_system_message = json_helper.return_json_information_batch(promptType=PromptType.SYSTEM_SMALL_PROMPT)

sp_prompt = json_helper.return_json_information_batch(promptType=PromptType.SMALL_PROMPT)
sp_model = gpt_4
sp_temperature = 0

result = send_message_to_api_and_return_request(sp_system_message,
                                                                       sp_prompt,
                                                                       sp_model,
                                                                       sp_temperature)
sp_result = result["res"]
sp_time_result = result["time_res"]
MongoWriter.create_item(_category=prompt_category, _prompt_length=len(sp_prompt), _prompt=sp_prompt, _result=sp_result,
                        _total_time=sp_time_result, _model=sp_model,_size="small")
# # Medium Prompt

mp_system_message = json_helper.return_json_information_batch(promptType=PromptType.SYSTEM_MEDIUM_PROMPT)
mp_prompt = json_helper.return_json_information_batch(promptType=PromptType.MEDIUM_PROMPT)
mp_model = gpt_4
mp_temperature = 0
result = send_message_to_api_and_return_request(
    _system_message=mp_system_message,
    _prompt=mp_prompt,
    _model=mp_model,
    _temperature=mp_temperature)
mp_result = result["res"]
mp_time_result = result["time_res"]
MongoWriter.create_item(_category=prompt_category, _prompt_length=len(mp_prompt), _prompt=mp_prompt, _result=mp_result,
                       _total_time=mp_time_result, _model=mp_model,_size="medium")

# # Large Prompt

lp_system_message = json_helper.return_json_information_batch(promptType=PromptType.SYSTEM_LARGE_PROMPT)
lp_prompt = json_helper.return_json_information_batch(promptType=PromptType.LARGE_PROMPT)
lp_model = gpt_4
lp_temperature = 0

result = send_message_to_api_and_return_request(
    _system_message=lp_system_message,
    _prompt=lp_prompt,
    _model=lp_model,
    _temperature=lp_temperature)
lp_result = result["res"]
lp_time_result = result["time_res"]

MongoWriter.create_item(_category=prompt_category, _prompt_length=len(lp_prompt), _prompt=lp_prompt, _result=lp_result,
                        _total_time=lp_time_result, _model=lp_model,_size="large")
