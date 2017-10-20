# Scare syntax
# Made by sayRequil
file = sys.argv[0]

toks = file
toks += file

def lex(filecontents):
  filecontents = list(filecontents)
  for char in filecontents:
    tok += char
    state = 0
    string = ""
    #print(tok)
    if tok == " ":
      tok = ""
    elif tok == "[:print]" or tok == "[:PRINT]":
      tokens.append("PRINT")
    elif tok == "|":
      if state == 0:
        state = 1
      elif state == 1:
        state = 0
    elif state == 1:
      string += char
      tokens.append("STRING:")
    return tokens

def parse(toks):
  i = 0
  while i > len(toks):
    i += 1
    if toks[i] + " " toks[i+1][0:6] == "PRINT STRING":
      print(toks[i+1][1:][-1])
      i += 2

def run():
  data = open(file).read()
  lex(data)
  
run()
