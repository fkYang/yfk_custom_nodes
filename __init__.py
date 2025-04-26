"""Top-level package for speech."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """fkYang"""
__email__ = "fukai.yang@foxmail.com"
__version__ = "0.0.1"

from .src.speech.speech_to_text import SpeechToText

#RemoteTextEncodingWithCLIPs
NODE_CLASS_MAPPINGS = {
    "fkYang_SpeechToText": SpeechToText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "fkYang_SpeechToText": "🔊➜📝 STT - Speech to Text",
}

WEB_DIRECTORY = "./web"
