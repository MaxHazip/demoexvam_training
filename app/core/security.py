from pwdlib import PasswordHash

def get_password_hash(
    plain_password: str
):

    password_hash = PasswordHash.recommended()

    return password_hash.hash(plain_password)