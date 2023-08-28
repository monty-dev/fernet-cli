import os

import fire
from cryptography.fernet import Fernet


def generate_key() -> str:
    """Generate a new, URL safe Fernet key.

    Returns
    -------
        str: fernet key
    """
    return Fernet.generate_key().decode()


def encrypt(token: str, key: str = os.environ["FERNET_KEY"]) -> str:
    """Encrypt a token with Fernet.

    Args:
    ----
        token (str): String to be encrypted
        key (str, optional): Fernet Key. Defaults to env var FERNET_KEY

    Returns:
    -------
        str: Encrypted, URL safe payload
    """
    return Fernet(key).encrypt(token.encode()).decode()


def decrypt(token, key: str = os.environ["FERNET_KEY"]) -> str:
    """Decrypt a token with Fernet.

    Args:
    ----
        token (str): String to be decrypted
        key (str, optional): Fernet Key. Defaults to env var FERNET_KEY

    Returns:
    -------
        str: Decrypted payload
    """
    return Fernet(key).decrypt(token).decode()


def main():
    fire.Fire({"encrypt": encrypt, "decrypt": decrypt, "generate": generate_key})


if __name__ == "__main__":
    main()
