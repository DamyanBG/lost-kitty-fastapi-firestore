from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def check_hashed_password(hashed_password, received_password):
    return check_password_hash(hashed_password, received_password)
