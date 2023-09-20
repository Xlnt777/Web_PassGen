import secrets

punctuation = "!@#$%^&*()_-+=/[\]{|}?"

def create_new(length: int, charactesrs: str) -> str:
	return ''.join(secrets.choice(charactesrs) for _ in range(length))




