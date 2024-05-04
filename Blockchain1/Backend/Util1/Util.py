import hashlib

def hash256(s):
    """Two rounds of SHA256"""
    # Encode the input string before hashing
    encoded_s = s.encode('utf-8')
    ans=hashlib.sha256(hashlib.sha256(encoded_s).digest()).hexdigest()
    print(ans)
    return ans


