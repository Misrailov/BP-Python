import vertexai
from vertexai.language_models import CodeChatModel, TextGenerationModel
from vertexai.preview.generative_models import GenerativeModel
from datetime import datetime


def create_and_return_client():
    vertexai.init(project="centering-keep-420313")


# Chat model
def send_message_to_api_and_return_request(_system_message, _prompt, _model, _temperature):
    create_and_return_client()
    parameters = {
        "temperature": _temperature,
        "max_output_tokes": 4096,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained(model_name=_model)
    message = model.predict(_prompt, **parameters)
    response = message.text
    return response


def send_message_to_api_and_return_request_gemini(_prompt, _temperature):
    time_start = datetime.now()

    create_and_return_client()
    parameters = {
        "temperature": _temperature,
        "max_output_tokes": 4096,
        "top_p": 0.8,
        "top_k": 40
    }
    model = GenerativeModel("gemini-1.5-pro-preview-0409")

    message = model.generate_content([_prompt])
    time_end = datetime.now()
    time_result = time_end - time_start
    response = {message.text, time_result}

    return response


# Code Model

def send_message_to_api_and_return_request_code(_system_message, _prompt, _model, _temperature):
    create_and_return_client()
    parameters = {
        "temperature": _temperature,
        "max_output_tokens": 2048,
    }

    code_chat_model = CodeChatModel.from_pretrained(model_name=_model)
    chat = code_chat_model.start_chat()

    message = chat.send_message(_prompt, **parameters)
    response = message.text
    return response
