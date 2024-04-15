from API import Claude
from Mongo import MongoWriter

prompt_category = "unit-test"
model = "Claude"
# Small Prompt
sp_system_message = ""
sp_prompt = ""
sp_model = ""
sp_temperature = ""

sp_result, sp_time_result = Claude.send_message_to_api_and_return_request(
    sp_system_message,
    sp_prompt,
    sp_model,
    sp_temperature)

MongoWriter.create_item(prompt_category, len(sp_prompt), sp_prompt, sp_result, sp_time_result,model)
# Medium Prompt

mp_system_message = ""
mp_prompt = ""
mp_model = ""
mp_temperature = ""

mp_result, mp_time_result = Claude.send_message_to_api_and_return_request(
    mp_system_message,
    mp_prompt,
    mp_model,
    mp_temperature)

MongoWriter.create_item(prompt_category, len(mp_prompt), mp_prompt, mp_result, mp_time_result,model)


# Large Prompt
lp_system_message = ""
lp_prompt = ""
lp_model = ""
lp_temperature = ""

lp_result, lp_time_result = Claude.send_message_to_api_and_return_request(
    lp_system_message,
    lp_prompt,
    lp_model,
    lp_temperature)

MongoWriter.create_item(prompt_category, len(lp_prompt), lp_prompt, lp_result, lp_time_result,model)

