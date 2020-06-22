from parser import parser
from functions import *

if __name__ == "__main__":
    # parser returns arguments `pre-processed` for us
    player1 = parser()
    # use calc to calculate result of our program
    #Player1 = create_final_table_player()
    # check variable res to give appropriate visualization
    #df = import_dataset()
    #apikey = save_api_key_in_env()
    #url = url_web_api()

    Player1 = create_final_table_player(player1)
    print(Player1)
    #Player1 = create_final_table_player()
    #Player1.head()
    # TIP:
    # Check these 3 steps:
    # 1.Get parameters from shell command (input parameters "numbers, operation", output parameters "reverse")
    # 2.Process data according to input parameters
    # 3.Output result according to output parameters