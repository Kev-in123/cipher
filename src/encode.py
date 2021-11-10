s = """
the quick brown fox jumps over the lazy dog
"""

def encode(message, shift):
  d = {}
  for c in (65, 97):
    for i in range(26):
      d[chr(i + c)] = chr((i + shift) % 26 + c)
  return "".join(d.get(c, c) for c in message)

print(encode(s, 10))
#output:
#dro aesmu lbygx pyh tewzc yfob dro vkji nyq
