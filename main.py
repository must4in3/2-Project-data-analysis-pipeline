import random
from voices import getVoice
from argparse import ArgumentParser
import sys
import os
import subprocess

def bash_command(cmd):
    proc = subprocess.Popen(['/bin/bash', '-c', cmd])
    return proc.wait()


def saluda(lugar, lang="es"):
    a = random.choice(["Felipe", "Amanda", "Marc"])
    if lang == "es":
        return f"Hola {a} desde {lugar}"
    elif lang == "en":
        return f"Hello {a} from {lugar}"
    elif lang == "pt":
        return f"olá {a} de {lugar}, tudo bem?"
    else:
        return "Unrecognized language"


parser = ArgumentParser(description="Este programa es para saludar a los TA")
parser.add_argument(
    "--lang", help="Configura el idioma del progama", default="es")
parser.add_argument("--lugar", help="Configura el lugar",
                    default=os.getenv("LUGAR"))
parser.add_argument("--debug", help="Configura el lugar",
                    default=False, action="store_true")
parser.add_argument("--say", help="Dilo en voz alta",
                    default=False, action="store_true")
parser.add_argument("--times", help="Repitelo N veces", default=1, type=int)


args = parser.parse_args()
if args.debug:
    print(args)
data = saluda(args.lugar, args.lang)
print(data)
if args.say:
    voice = getVoice(args.lang)
    print(f"Lo digo en voz alta con voz de {voice}")

    bash_command(f"say -v '{voice}' '{data*args.times}'")