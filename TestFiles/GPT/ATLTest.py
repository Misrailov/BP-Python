from API import GPT

from Mongo import MongoWriter
from Prompts import json_helper
from Prompts.json_helper import PromptType

prompt_category = "atl-test"
gpt_4 = "gpt-4-turbo"
gpt_3_5 = "gpt-3.5-turbo-0125"
# Small Prompt
sp_system_message = json_helper.return_json_information_atl(promptType=PromptType.SYSTEM_SMALL_PROMPT)
sp_prompt = json_helper.return_json_information_atl(promptType=PromptType.SMALL_PROMPT)
sp_model = gpt_4
sp_temperature =0

result = GPT.send_message_to_api_and_return_request(sp_system_message,
                                                    sp_prompt,
                                                    sp_model,
                                                    sp_temperature)

sp_result = result["res"]
sp_time_result = result["time_res"]
MongoWriter.create_item(prompt_category, len(sp_prompt), sp_prompt, sp_result, sp_time_result, sp_model,_size="small")

# Medium Prompt

mp_system_message = json_helper.return_json_information_atl(promptType=PromptType.SYSTEM_MEDIUM_PROMPT)
mp_prompt = json_helper.return_json_information_atl(promptType=PromptType.MEDIUM_PROMPT)
mp_model = gpt_4
mp_temperature = 0
result = GPT.send_message_to_api_and_return_request(mp_system_message,
                                                    mp_prompt,
                                                    mp_model,
                                                    mp_temperature)
mp_result = result["res"]
mp_time_result = result["time_res"]
MongoWriter.create_item(prompt_category, len(mp_prompt), mp_prompt, mp_result, mp_time_result, mp_model,_size="medium")

# Large Prompt


lp_system_message = json_helper.return_json_information_atl(promptType=PromptType.SYSTEM_LARGE_PROMPT)
lp_prompt = json_helper.return_json_information_atl(promptType=PromptType.LARGE_PROMPT)
lp_model = gpt_4
lp_temperature = 0

result = GPT.send_message_to_api_and_return_request(lp_system_message,
                                                    lp_prompt,
                                                    lp_model,
                                                    lp_temperature)
lp_result = result["res"]

lp_time_result = result["time_res"]

MongoWriter.create_item(prompt_category, len(lp_prompt), lp_prompt, lp_result, lp_time_result, lp_model,_size="large")
