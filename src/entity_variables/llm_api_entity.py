from dataclasses import dataclass
from pathlib import Path
import json
from src.CONSTANT import *







@dataclass(frozen=True)
class AnthropicKeyVariables:
    base64_string:str
    anthropict_api_key:str = ANTHROPIC_API_KEY
    prompt:str
    anthropic_model:str



@dataclass(frozen=True)
class OpenaiKeyVariables:
    base64_string:str
    openai_api_key:str = OPEN_AI_KEY
    prompt:str
    openai_model:str


@dataclass(frozen=True)
class DocumentaiKeyVariables:
    PROJECT_ID:str = PROJECT_ID
    LOCATION:str = LOCATION
    PROCESSOR_ID:str = PROCESSOR_ID
    credentials = credentials


