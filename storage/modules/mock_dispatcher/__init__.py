"""Mock dispatcher module used for integration testing.

Expose send_message(envelope: dict) -> dict
"""
from .dispatch_adapter import send_message
