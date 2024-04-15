import os

import anthropic
from dotenv import load_dotenv
import re

from datetime import datetime


def create_and_return_client():
    load_dotenv()
    key_for_api = os.getenv("anthropic_api_key")
    client = anthropic.Anthropic(api_key=key_for_api)
    return client


def send_message_to_api_and_return_request(_system_message, _prompt, _model, _temperature):
    time_start = datetime.now()
    client = create_and_return_client()
    message = client.messages.create(
        model=_model,
        max_tokens=4096,
        temperature=_temperature,
        system=_system_message,
        messages=[
            {"role": "user", "content": _prompt}
        ]
    )
    time_end = datetime.now()
    time_result = time_end - time_start
    result_message = {message.content[0].text, time_result}
    return result_message
