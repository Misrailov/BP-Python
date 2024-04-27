from API import GPT

from Mongo import MongoWriter
from Prompts import json_helper
from Prompts.json_helper import TestType, PromptType



prompt_category = "atl-test"
model = "GPT"

# Small Prompt
sp_system_message = json_helper.return_json_information(testType=TestType.ATL_PROMPT
                                                        , promptType=PromptType.SYSTEM_SMALL_PROMPT)
sp_prompt = json_helper.return_json_information(testType=TestType.ATL_PROMPT
                                                        , promptType=PromptType.SMALL_PROMPT)
sp_model = ""
sp_temperature = ""

sp_result, sp_time_result = GPT.send_message_to_api_and_return_request(sp_system_message,
                                                                       sp_prompt,
                                                                       sp_model,
                                                                       sp_temperature)
MongoWriter.create_item(prompt_category, len(sp_prompt), sp_prompt, sp_result, sp_time_result,model)

# Medium Prompt

mp_system_message = json_helper.return_json_information(testType=TestType.ATL_PROMPT
                                                        , promptType=PromptType.SYSTEM_MEDIUM_PROMPT)
mp_prompt = json_helper.return_json_information(testType=TestType.ATL_PROMPT
                                                        , promptType=PromptType.MEDIUM_PROMPT)
mp_model = ""
mp_temperature = ""
mp_result, mp_time_result = GPT.send_message_to_api_and_return_request(mp_system_message,
                                                                       mp_prompt,
                                                                       mp_model,
                                                                       mp_temperature)
MongoWriter.create_item(prompt_category, len(mp_prompt), mp_prompt, mp_result, mp_time_result,model)

# Large Prompt


lp_system_message = json_helper.return_json_information(testType=TestType.ATL_PROMPT
                                                        , promptType=PromptType.SYSTEM_LARGE_PROMPT)
lp_prompt = json_helper.return_json_information(testType=TestType.ATL_PROMPT
                                                        , promptType=PromptType.LARGE_PROMPT)
lp_model = ""
lp_temperature = ""
lp_result, lp_time_result = GPT.send_message_to_api_and_return_request(lp_system_message,
                                                                       lp_prompt,
                                                                       lp_model,
                                                                       lp_temperature)

MongoWriter.create_item(prompt_category, len(lp_prompt), lp_prompt, lp_result, lp_time_result,model)
