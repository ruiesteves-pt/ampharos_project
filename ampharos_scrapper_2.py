# Footium Ampharos Algorithm v2
# @ruiesteves
# Ampharos Web Scrapper with Selenium (second try to activate Metamask)

# Imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from ampharos_classes import *
import time
import pickle

# Initial Constants
#URL_init = 'https://footium.club/beta/tournaments/3/match/21/0'
#URL_list = [URL_init]


def main(division,round_num,match_num):
    URL_list = []
    for r in range(5,round_num):
        for m in range(match_num):
            URL_assemble = 'https://footium.club/beta/tournaments/' + str(division) + '/match/' + str(r) + '/' + str(m)
            #print(URL_assemble)
            URL_list.append(URL_assemble)
    for URL in URL_list:
        match ={}
        line_up_h = []
        line_up_a = []
        browser = webdriver.Firefox()
        browser.get(URL)
        time.sleep(12)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        html = browser.page_source
        results = browser.find_elements_by_class_name('d-flex')
        l = len(results)
        r = range(l-1)
        for i in r:                 # To find out the indexes of data
            a = i+1
            b = results[a].text
            #print(b)
            if i == 1:
                split_b = b.split()
                if split_b[1].isdigit():
                    team_h = split_b[0]
                    score_h = int(split_b[1])
                    score_a = int(split_b[2])
                    if split_b[4].isdigit():
                        team_a = split_b[3]
                    else:
                        team_a = split_b[3] + split_b[4]
                elif not split_b[2].isdigit():
                    team_h = split_b[0] + split_b[1] + split_b[2]
                    score_h = int(split_b[3])
                    score_a = int(split_b[4])
                    if split_b[6].isdigit():
                        team_a = split_b[5]
                    else:
                        team_a = split_b[5] + split_b[6]
                else:
                    team_h = split_b[0] + split_b[1]
                    score_h = int(split_b[2])
                    score_a = int(split_b[3])
                    if split_b[5].isdigit():
                        team_a = split_b[4]
                    else:
                        team_a = split_b[4] + split_b[5]

                #print('Home team:',team_h)
                #print('Away team:',team_a)
                #print('Score home:',score_h)
                #print('Score away:',score_a)

            elif i == 11:
                split_b = b.split()
                total_shots_h = int(split_b[0])
                total_shots_a = int(split_b[1])
                #print('Total shots home:',total_shots_h)
                #print('Total shots away:',total_shots_a)

            elif i == 13:
                split_b = b.split()
                shots_target_h = int(split_b[0])
                shots_target_a = int(split_b[1])
                #print('Shots target home:',shots_target_h)
                #print('Shots target away:',shots_target_a)
            elif i == 16:
                split_b = b.split()
                rating_h = [int(split_b[0])]
            elif i == 17:
                split_b = b.split()
                rating_h.append(int(split_b[0]))
            elif i == 18:
                split_b = b.split()
                rating_h.append(int(split_b[0]))
                #print('Ratings home:',rating_h)
            elif i == 19:
                formation_h = b
                #print('Formation home:',formation_h)
            elif i == 20:
                style_h = b
                #print('Style home:',style_h)
            elif (i >= 21) & (i <= 37):
                player = {}
                split_b = b.split()
                player['position'] = split_b[0]
                player['rating'] = int(split_b[1])
                player['stamina'] = split_b[2]
                player['name'] = split_b[3] + split_b[4]
                line_up_h.append(player)
                #print(player)
                #line_up_h = []
                # href_find = results[a].find_elements_by_tag_name("a") MAYBE USEFUL IN THE FUTURE FOR LINK SEARCHING
                # print(href_find[0].text)
            elif i == 46:
                split_b = b.split()
                rating_a = [int(split_b[0])]
            elif i == 47:
                split_b = b.split()
                rating_a.append(int(split_b[0]))
            elif i == 48:
                split_b = b.split()
                rating_a.append(int(split_b[0]))
                #print('Ratings away:',rating_a)
            elif i == 49:
                formation_a = b
                #print('Formation away:',formation_a)
            elif i == 50:
                style_a = b
                #print('Style away:',style_a)
            elif (i >= 51) & (i <= 67):
                player = {}
                split_b = b.split()
                player['position'] = split_b[0]
                player['rating'] = int(split_b[1])
                player['stamina'] = split_b[2]
                player['name'] = split_b[3] + split_b[4]
                line_up_a.append(player)
                #print(player)

        match['home team'] = team_h
        match['away team'] = team_a
        match['score home'] = score_h
        match['score away'] = score_a
        match['total shots home'] = total_shots_h
        match['total shots away'] = total_shots_a
        match['shots on target home'] = shots_target_h
        match['shots on target away'] = shots_target_a
        match['ratings home'] = rating_h
        match['formation home'] = formation_h
        match['style home'] = style_h
        match['line up home'] = line_up_h
        match['ratings away'] = rating_a
        match['formation away'] = formation_a
        match['style away'] = style_a
        match['line up away'] = line_up_a
        #print(match)

        # Initiate file dumping with pickle
        URL_clean = URL.replace(":","")
        URL_clean = URL_clean.replace("/","")
        URL_clean = URL_clean.replace(".","")
        file_name = URL_clean + ".txt"
        file = open(file_name,'wb')
        pickle.dump(match, file)
        file.close()

        # FOR NOW, KEEP THIS COMMENTED, USEFUL IN READING CASES
        #with open(file_name,'rb') as f:
        #    match_test = pickle.load(f)
        #print(match_test)

        #print('Index',i,':',b) PHASE 1 DEBUG

main(4,22,6)
