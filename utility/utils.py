import hashlib

def calculate_decision_hash(decision, salt):
    decision_hash = hashlib.sha256(bytes(decision) + hashlib.sha256(salt.encode()).digest()).hexdigest()
    return decision_hash

def make_decision(decision, salt):
    hash_value = hashlib.sha256(salt.encode()).digest()
    salt_hash = hashlib.sha256(hash_value).hexdigest()
    decision_hash = hashlib.sha256(bytes(decision) + hash_value).hexdigest()
    return decision_hash, salt_hash

def decode_decision(decision_hash, salt_hash):
    hash_value = bytes.fromhex(salt_hash)
    decision = bytes.fromhex(decision_hash)[:1]
    return decision == b"\x01"
