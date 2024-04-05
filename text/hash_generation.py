"""
Hash generation and decoding
"""

from base64 import b64encode, b64decode


def hash_encode(message_id: str) -> str:
    """
    Encoding of the message id
    :param message_id: message id
    """
    message_id_bytes = message_id.encode('utf-8')
    base64_bytes = b64encode(message_id_bytes)
    base64_message_id = base64_bytes.decode('utf-8')
    return base64_message_id


def hash_decode(message_hash: str) -> str:
    """
    Decoding the hash of the message id
    :param message_hash: hash of the message id
    """
    base64_bytes = message_hash.encode('utf-8')
    message_bytes = b64decode(base64_bytes)
    message_id = message_bytes.decode('utf-8')
    return message_id
