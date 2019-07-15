#Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

from binascii import unhexlify
import base64

#https://www.reddit.com/r/learnpython/comments/2vj4o5/cryptography_bytes_vs_encoded_strings/
def hex_to_b64(hex_string):
  hex_bytes = unhexlify(hex_string)
  print hex_bytes
  print base64.b64encode(hex_bytes)


##### Original Solution
#def hex_to_b64_og(hex_string):
#  print hex_string.decode("hex").encode("base64")
  
#  return
  
hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
