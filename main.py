from parser import parser
from src.functions_def import *

if __name__ == "__main__":
    # parser returns arguments `pre-processed` for us
    player1, player2 = parser()
    # use this app to calculate the stats of every player in NBA
    # return 5 plots, and one dataset with stats infos.

    name = player1
    player1_table_api = create_final_table_api(name)
    table_player1 = create_final_table_selenium(2544)

    for x in table_player1.columns:
        try:
            table_player1[f'{x}']= table_player1[f'{x}'].astype(float)
        except:
            pass

    table_player1_selenium = merge_selenium_table(table_player1)
    table_player1_selenium['Player'] = f'{name.split()[0]} {name.split()[1]}'
    table_player1_final = pd.merge(player1_table_api, table_player1_selenium, on='Player', how='outer')

    pts = table_player1.groupby(['Year','PTS']).agg({'PTS': 'mean'})
    reb = table_player1.groupby(['Year','REB']).agg({'REB': 'mean'})
    ast = table_player1.groupby(['Year','AST']).agg({'AST': 'mean'})
    stl = table_player1.groupby(['Year','STL']).agg({'STL': 'mean'})
    blk = table_player1.groupby(['Year','BLK']).agg({'BLK': 'mean'})

    pts.plot(use_index= 1, rot=90)
    plt.savefig(r'output/points_{}.png'.format(name))
    reb.plot(use_index= 1, rot=90)
    plt.savefig(r'output/rebound_{}.png'.format(name))
    ast.plot(use_index= 1, rot=90)
    plt.savefig(r'output/assist_{}.png'.format(name))
    blk.plot(use_index= 1, rot=90)
    plt.savefig(r'output/block_{}.png'.format(name))
    stl.plot(use_index= 1, rot=90)
    plt.savefig(r'output/steals_{}.png'.format(name))

    table_player1.to_csv(r'output/all_stats_player.csv')
    table_player1_final.to_csv(r'output/resume_stats_player.csv')
    print(pts)
#
#
#
#
#
#
#
#
#
#
#
#


    name = player2
    player2_table_api = create_final_table_api(name)
    table_player2 = create_final_table_selenium('201939')

    for x in table_player2.columns:
        try:
            table_player2[f'{x}']= table_player2[f'{x}'].astype(float)
        except:
            pass

    table_player2_selenium = merge_selenium_table(table_player2)
    table_player2_selenium['Player'] = f'{name.split()[0]} {name.split()[1]}'
    table_player2_final = pd.merge(player2_table_api, table_player2_selenium, on='Player', how='outer')

    pts = table_player2.groupby(['Year','PTS']).agg({'PTS': 'mean'})
    reb = table_player2.groupby(['Year','REB']).agg({'REB': 'mean'})
    ast = table_player2.groupby(['Year','AST']).agg({'AST': 'mean'})
    stl = table_player2.groupby(['Year','STL']).agg({'STL': 'mean'})
    blk = table_player2.groupby(['Year','BLK']).agg({'BLK': 'mean'})

    pts.plot(use_index= 1, rot=90)
    plt.savefig(r'output/points_{}.png'.format(name))
    reb.plot(use_index= 1, rot=90)
    plt.savefig(r'output/rebound_{}.png'.format(name))
    ast.plot(use_index= 1, rot=90)
    plt.savefig(r'output/assist_{}.png'.format(name))
    blk.plot(use_index= 1, rot=90)
    plt.savefig(r'output/block_{}.png'.format(name))
    stl.plot(use_index= 1, rot=90)
    plt.savefig(r'output/steals_{}.png'.format(name))

    table_player2.to_csv(r'output/all_stats_player2.csv')
    table_player2_final.to_csv(r'output/resume_stats_player2.csv')
    print(pts)
    # TIP:
    # Check these 3 steps:
    # 1.Get parameters from shell command (input parameters "numbers, operation", output parameters "reverse")
    # 2.Process data according to input parameters
    # 3.Output result according to output parameters