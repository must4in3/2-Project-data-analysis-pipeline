from argparse import ArgumentParser
from src.functions_def import *

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="Este programa está pensado para comparar las estadisticas de dos jugadores de NBA")
    # Add argument
    parser.add_argument("player1",type=str, help= 'poner el nombre y el apellido del primer jugador NBA de los ultimos 50 años')
    parser.add_argument("player2",type=str, help= 'poner el nombre y el apellido del segundo jugador NBA de los ultimos 50 años')
    # Retrieve Arguments
    args = parser.parse_args()
    # Accessing different variables in args
    player1 = args.player1
    player2 = args.player2
    return player1, player2
    #table_player1_selenium