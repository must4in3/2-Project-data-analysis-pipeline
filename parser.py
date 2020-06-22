from argparse import ArgumentParser
from functions import *

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="Comparar dos players de NBA")
    # Add argument
    parser.add_argument("player1",type=str)
    #parser.add_argument("player2",type=str)
    # Boolean Argument
    # cancel parser.add_argument("-reverse", action='store_true')
    # Group of arguments, mutually exclusive
    #group = parser.add_mutually_exclusive_group(required=True)
    #group.add_argument("-sum", dest="oper", action='store_const', const=player)
    #group.add_argument("-prod", dest="oper", action='store_const', const=prod)
    # Retrieve Arguments
    args = parser.parse_args()
    # Accessing different variables in args
    player1 = args.player1
    #player2 = args.player2
    return player1#, player2