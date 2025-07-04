import os
import random

ticks: int = 0
keys: int = 0
totalmultiplier: int = 1
usactive: bool = False
upglevel: int = 0
paused: bool = False
inputstr: str = ""
basekeygain: float = 1

#strings
insuffkeys = "not enough keys\n"
purcomplete = "purchase complete\n"
existingupgrade = "you already have this upgrade\n"
downgradeconf = "are you sure you want to downgrade???\nplease type 'i am completely aware of the consequences of this action and am responsible for any acceleration loss that could happen upon downgrading' to confirm\n"
downgradeconffail = "you didn't type it right idiot\n"
downgradeconfyes = "have fun with your downgrade\n"

downgradeconftext = "i am completely aware of the consequences of this action and am responsible for any acceleration loss that could happen upon downgrading"

sentencesofthesession = [
  "replit ghostwriter i hate you",
  "have you ever tried to disable replit ghostwriter",
  "i hate ai being shoved in my face, but it's my only way to go with replit :/",
  "i'm sorry ghostwriter, i forgive you",
]
helptext = """-----------

keybinds
  [enter] - tick (dont you dare type enter literaly)
  [us] - upgrade shop
  [u] - upgrades
  [s] - save game
  [l] - load game  
  [q] - quit
  [h] - help
  
  -----------"""

def init():
  os.system("clear")
  print("""-----------
  
  welcome to keyincrementals (0.0)
  a game made by naterhythm using python (naterhythm.netlify.app)
  
  keybinds
  [enter] - tick (dont you dare type enter literaly)
  [us] - upgrade shop
  [u] - upgrades
  [s] - save game
  [l] - load game  
  [q] - quit
  [h] - help
  
  -----------
  
  sentence of the session: """ + random.choice(sentencesofthesession) + "\n\n  ----------")


init()


def tick():
  global ticks
  global keys
  global totalmultiplier
  global paused
  global basekeygain
  
  #check increments
  if upglevel == 1:
    totalmultiplier = 5
  elif upglevel == 2:
    totalmultiplier = 20
  elif upglevel == 3:
    totalmultiplier = 100
  else:
    totalmultiplier = 1

  #base key gain incrementation checker
  if upglevel >= 1 and upglevel <= 3:
    basekeygain += 0.001

  #incrementation time!!
  if paused:
    pass
  else:
    ticks += 1
    keys += basekeygain * totalmultiplier

  print("ticked!")

# main loop
while True:
  #inputstrings
  inregular = "\n\n[>] sesh\n[bkg:" + str(basekeygain) + "] [mul:" + str(totalmultiplier) + "]\n[t:" + str(ticks) + "] [k:" + str(keys) + "] >> "
  inpaused = "\n\n[||] sesh\npaused >> "
  indebug = "\n\n[>] paused: " + str(paused) +"\nsesh\n[t:" + str(ticks) + "] [k:" + str(keys) + "] DEBUG >> "

  inputstr = inregular
  
  pinput = input(inputstr)
  
  #inputstrinthingactually
  if paused:
    inputstr = inpaused
  elif pinput == "debug":
    inputstr = indebug
  elif pinput == "regular":
    inputstr = inregular
  
  elif pinput == "q":
    break
  elif pinput == "":
    print("[>] output")
    tick()
  elif pinput == "enter":
    print("you typed enter literally, you idiot (if you want to tick, just press enter) (ghostwriter typed this)")
  elif pinput == "h":
    print(helptext)
  elif pinput == "us":
    paused = True
    usactive = True
    print("""-----------
    upgrade shop (type exit to go back to game) 
    -----------
    {x} - upgrade - price - effect
    -----------
    
    {1} - milestone 1 - 10 keys - 5x multiplier - base key gain increments +0.001 per tick
    {2} - milestone 2 - 1k keys - 20x multiplier
    {3} - milestone 3 - 10k keys - 100x multiplier
    {mk} - monster keys - 100k keys - new currency (monster keys) - base key gain increments +0.05 per tick
    {4} - milestone 4 - 10m keys + 100 monster keys - 1k multiplier
    ----------
    """)
  else:
    print("unknown command (press h for help)")
  if usactive:
    
    if pinput == "1":
      if keys <= 10:
        print(insuffkeys)
      elif keys >= 10 and upglevel == 1 or upglevel >= 1:
        print(existingupgrade)
      else:
        keys -= 10
        upglevel = 1
        print(purcomplete)

    if pinput == "2":
      if keys <= 1000:
        print(insuffkeys)
      elif keys >= 1000 and upglevel == 2 or upglevel >= 2:
        print(existingupgrade)
      else:
        keys -= 1000
        upglevel = 2
        print(purcomplete)

    if pinput == "3":
      if keys <= 10000:
        print(insuffkeys)
      elif keys >= 10000 and upglevel == 3 or upglevel >= 3:
        print(existingupgrade)
      else:
        keys -= 10000
        upglevel = 3
        print(purcomplete)
        
    elif pinput == "exit":
      paused = False
      usactive = False
    else:
      print("type exit to go back to game")
