"""Top-level package for yfk_custom_nodes."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """fkYang"""
__email__ = "fukai.yang@foxmail.com"
__version__ = "0.0.1"

from .src.yfk_custom_nodes.nodes import NODE_CLASS_MAPPINGS
from .src.yfk_custom_nodes.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
