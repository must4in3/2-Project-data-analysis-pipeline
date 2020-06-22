from parser import parser
from final import *

if __name__ == "__main__":
    # parser returns arguments `pre-processed` for us
    player1, player2 = parser()
    # use calc to calculate result of our program
    Player1 = create_final_table_player()
    # check variable res to give appropriate visualization
    print(Player1.head())

    # TIP:
    # Check these 3 steps:
    # 1.Get parameters from shell command (input parameters "numbers, operation", output parameters "reverse")
    # 2.Process data according to input parameters
    # 3.Output result according to output parameters