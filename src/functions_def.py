# pandas for data manipulation and analysis
import pandas as pd
# numpy to manipulate multi-dimensional arrays and matrices
import numpy as np
# re - regex to provides regular expression matching operations
import re
# the OS module in Python provides a way of using operating system dependent functionality
import os
# the requests module allows you to send HTTP requests using Python
import requests
# python-dotenv to read the key-value pair from . env file and adds them to environment variable.
from dotenv import load_dotenv
#Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
# The selenium package is used to automate web browser interaction from Python
from selenium import webdriver
# to simplify management of binary drivers for different browsers
#import chromedriver_binary 
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt

def import_dataset():
    df = pd.read_csv('inputs/datasets_Nba_Players.csv', encoding = 'latin-1')
    df = df.rename({'collage':'college'}, axis=1)
    return df


def save_api_key_in_env():
    load_dotenv()
    apikey = os.getenv("APIKEY")
    return apikey


def url_web_api():
    # enviar una request. Si sale un numero que empieza con 2 todo bien, 
    # o si no ver los errores de los gatos a ver que dicen!
    url = 'http://api.probasketballapi.com/player'
    res = requests.post(url)
    return url


def player_name():
    first_name = input('Insert the name of an NBA player')
    last_name = input('Insert the last_name of an NBA player')
    return first_name, last_name


def call_player(player_name):
    try:
        query = {'api_key': f'{apikey}', 'first_name':f'{player_name[0]}', 'last_name':f'{player_name[1]}'}
        r = requests.post(url, data=query)
        player_api =r.json()[0]
        table_api = pd.DataFrame(player_api, index=[0])
        return table_api.head()
    except:
        print('Player not in database. Try another one')
        return call_player(input('Insert new player'))

def merge_info_api(player_name, player_table):
    query_player = df[(df['Player']==f'{player_name[0]} {player_name[1]}')]
    # Rename the column with the common data
    player_table = player_table.rename({'player_name':'Player'}, axis=1)
    # Merge of the two tables
    query_player_update = pd.merge(query_player, player_table, on='Player', how='outer')
    # Eliminate redundant information
    query_player_update = query_player_update[['Unnamed: 0', 'Player', 'first_name', 'last_name', 
    'born', 'birth_date','birth_city', 'college','height', 'weight','position', 'dk_position']]
    # Result compared to the original data)
    return query_player_update

def getPage(url):
    # This function show a basic way to make a get requests used Selenium
    # First line to to avoid this error:
    # WebDriverException: Message: 'chromedriver' executable needs to be available in the path.
    # driver.execute_script(..) to scroll the page in Selenium untill the bottom
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #box = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[1]/div[1]/input')
    #box.send_keys('LeBron James')
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    driver.quit()
    return soup


# different way to scraping the webpabge, using CSS selector or tags
# Ex.1 - just columns name
def scraping_columnas(soup):
    columnas = [table.text.split() for table in soup.select("thead")]
    return columnas
def scraping_lenght(soup):
    # Ex.2 - all value in the table
    lenght = [table.text.split() for table in soup.select("tbody")]
    return lenght
def scraping_row(soup):
    row = [table.text.split() for table in soup.select("tbody > tr")]
    return row
# I use the years variable to store the information of the athlete's years of activity, 
#which is different for each athlete. This way I can create a generic scraping that works for most players


def cleaning_variable(row):
    # clean the variable from unnecessary fields, to facilitate the process of creating dictionaries
    new_row = []
    for x in row:
        if len(x)>1:
            new_row.append(x)
    return new_row


def creacolumnas(columnas, empty_dict):
    # this function allows you to create the keys of each dictionary
    for column in columnas:
        empty_dict[column] = []  


def creafilas(row, numpari, empty_dict, years):
    # this function allows you to fill the data tables
    for i,value in enumerate(empty_dict.keys()):
        for x in range(years):
            try:
                empty_dict[value].append(row[x+(numpari*years)][i])
            except:
                pass


def cleaning_tabla1(columnas, number):
    # an additional procedure for cleaning the keys that will be inserted in each dictionary
    columnas_tabla1 =columnas[0][number::]
    return columnas_tabla1


def create_selenium_player(number):
    soup1 = getPage(f"https://stats.nba.com/player/{number}")
    print(number)
    columnas_player1 = scraping_columnas(soup1)
    lenght_player1 = scraping_lenght(soup1)
    row_player1 = scraping_row(soup1)
    years_player1 = len(lenght_player1[1])
    Traditional_Splits_player1  = dict()
    new_row_player1 = cleaning_variable(row_player1)
    if 'career' in str(number):
        columnas_tabla_player1 = cleaning_tabla1(columnas_player1, 0)
    else:
        columnas_tabla_player1 = cleaning_tabla1(columnas_player1, 1)
    creacolumnas(columnas_tabla_player1, Traditional_Splits_player1 )
    creafilas(new_row_player1, 0, Traditional_Splits_player1 , years_player1)
    table1 = pd.DataFrame(Traditional_Splits_player1)
    return table1


def merge_selenium_table(table):
    # Change the type of each column in float in order to calculate its average of values
    table = table[['GP','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%',
        'OREB','DREB','REB','AST','TOV','STL','BLK','PF']].astype(float)
    # The new selenium dataset with the average statistics of the player's entire career
    table_mean_stats = pd.DataFrame(table.mean()).T
    return table_mean_stats


def create_new_columns_to_merge_dataset(players_name, table):
    table['Player'] = f'{players_name[0]} {players_name[1]}'
    return table


def merge_info_selenium(table_before_selenium, table_selenium):
    # Merge of the two tables
    final_table = pd.merge(table_before_selenium, table_selenium, on='Player', how='outer')
    return final_table


def create_final_table_api(name):
    players1_name = name.split()
    players1_table = call_player(players1_name)
    player1_table_api = merge_info_api(players1_name, players1_table)
    return player1_table_api

def create_final_table_selenium(numero):
    table_player1 = create_selenium_player(numero)
    return table_player1

df = import_dataset()
apikey = save_api_key_in_env()
url = url_web_api()