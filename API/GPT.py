from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

def create_and_return_client():
    load_dotenv()
    key_for_api = os.getenv("openai_api_key")
    client = OpenAI(
        api_key=key_for_api
    )
    return client


def send_message_to_api_and_return_request(_system_message, _prompt, _model, _temperature):
    time_start = datetime.now()

    client = create_and_return_client()
    message = client.chat.completions.create(
        model=_model,
        temperature=_temperature,
        messages=[
            {"role": "system", "content": _system_message},
            {"role": "user", "content": _prompt}
        ]
    )

    time_end = datetime.now()
    time_result = time_end - time_start
    result_message = {message.choices[0].message.content,time_result}
    return result_message
