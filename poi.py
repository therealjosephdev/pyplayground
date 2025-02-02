import time
import sys

def typewriter_effect(text, delay=0.05):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

intro_text = """
>>> SYSTEM BOOTING... 
>>> INITIALIZING MACHINE... 
>>> RUNNING SURVEILLANCE PROTOCOLS...
"""

monologue = """
"You are being watched.
The government has a secret system
A machine
that spies on you every hour of every day.

I know, because I built it.
I designed the Machine to detect acts of terror,
but it sees everything.
Violent crimes involving ordinary people.
People like you.

Crimes the government considered irrelevant.
They wouldn't act, so I decided I would.
But I needed a partner,
someone with the skills to intervene.

Hunted by the authorities, we work in secret.
You'll never find us.
But, victim or perpetrator,
if your number's up, we'll find you."
"""

access_granted = "\n>>> ACCESS GRANTED"

time.sleep(1)
typewriter_effect(intro_text, 0.07)
time.sleep(1)
typewriter_effect(monologue, 0.05)
time.sleep(1.5)
typewriter_effect(access_granted, 0.1)