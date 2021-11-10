s = """

"""

def decrypt(message):
  msg = message.lower()
  replace = ("\n", "\t", " ")
  for i in replace:
    msg = msg.replace(i, "")
  m_char = max(msg, key = msg.count)
  push = ord(m_char) - 101
  d = {}
  for c in (65, 97):
    for i in range(26):
      d[chr(i + c)] = chr((i - push) % 26 + c)
  return "".join(d.get(c, c) for c in message)
    
print(decrypt(s))