# Footium Ampharos Algorithm v2
# @ruiesteves
# Data processor and plotter

# Imports
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import os
from os import listdir
import pickle
from ampharos_classes import *
import itertools
import pandas as pd

# Initial Constants
list_of_matches_dict = []
list_of_matches_obj = []
dict_formations = {}
dict_styles = {}
match_path = 'Match_database'

# Functions

# Goes to /Match_database/ directory and gets all match data (wrote as dicts in txt files)
def getDictsFromFiles():
    list_files = os.listdir(match_path)
    for file in list_files:
        file_path = match_path + "\\" + file
        with open(file_path,'rb') as f:
            dict = pickle.load(f)
        list_of_matches_dict.append(dict)
    #print(list_of_matches_dict)

# From a list of dicts, constructs objects to be processed later
def fromDictToObject(list_of_dicts):
    for dict in list_of_dicts:
        list_of_matches_obj.append(Match(dict['home team'],dict['away team'],dict['score home'],
        dict['score away'],dict['formation home'],dict['formation away'],dict['style home'],
        dict['style away'],dict['line up home'],dict['line up away'],dict['total shots home'],dict['total shots away'],dict['shots on target home'],
        dict['shots on target away'],dict['ratings home'],dict['ratings away']))
    #print(list_of_matches_obj)

def arrangeFormations(list_of_obj):
    list_formations = []
    for obj in list_of_obj:
        list_formations.append(obj.formation_h)
        list_formations.append(obj.formation_a)
    set_formations = set(list_formations)
    formation_combinations = list(itertools.combinations(set_formations, 2))
    for formation in set_formations:
        formation_combinations.append((formation,formation))
    for combo in formation_combinations:
        dict_formations[combo] = [0,0,0]  # KEY = COMBO, VALUE = [POINTS FORMATION 1, POINTS FORMATION 2, GAME COUNTER]
    #print(formation_combinations)
    return set_formations

def arrangeStyles(list_of_obj):
    list_styles = []
    for obj in list_of_obj:
        list_styles.append(obj.style_h)
        list_styles.append(obj.style_a)
    set_styles = set(list_styles)
    styles_combinations = list(itertools.combinations(set_styles, 2))
    for style in set_styles:
        styles_combinations.append((style,style))
    #print(styles_combinations)
    for combo in styles_combinations:
        dict_styles[combo] = [0,0,0]  # KEY = COMBO, VALUE = [POINTS FORMATION 1, POINTS FORMATION 2, GAME COUNTER]
    #print(formation_combinations)
    return set_styles

def formation_heatmap(list_of_obj):
    for obj in list_of_obj:
        obj.formationAnalysis()
        obj.avgStamina()
        obj.isGhost()
        if obj.ghost_h or obj.ghost_a:
            None
        else:
            match_result = obj.result
            match_form_tuple = (match_result[2],match_result[3])
            match_form_tuple_1 = (match_result[3],match_result[2])
            if match_form_tuple in dict_formations:
                dict_formations[match_form_tuple] = [sum(x) for x in zip(dict_formations[match_form_tuple], [match_result[0],match_result[1],1])]
            elif match_form_tuple_1 in dict_formations:
                dict_formations[match_form_tuple_1] = [sum(x) for x in zip(dict_formations[match_form_tuple_1], [match_result[1],match_result[0],1])]

    formation_plot = {}
    for formation_1 in set_formations:
        list_average = []
        for formation_2 in set_formations:
            if (formation_1,formation_2) in dict_formations:
                if dict_formations[(formation_1,formation_2)][2] == 0:
                    avg = None
                    list_average.append(avg)
                else:
                    avg = dict_formations[(formation_1,formation_2)][0]/dict_formations[(formation_1,formation_2)][2]
                    list_average.append(avg)
            elif (formation_2,formation_1) in dict_formations:
                if dict_formations[(formation_2,formation_1)][2] == 0:
                    avg = None
                    list_average.append(avg)
                else:
                    avg = dict_formations[(formation_2,formation_1)][1]/dict_formations[(formation_2,formation_1)][2]
                    list_average.append(avg)
            else:
                list_average.append(None)
        formation_plot[formation_1] = list_average
    formation_df = pd.DataFrame(formation_plot,index=set_formations)
    #formation_df = pd.DataFrame(formation_plot)
    #formation_df = formation_df.pivot(index=set_formations, columns=set_formations)
    print(formation_df)
    cmap = sb.cm.rocket_r
    ax = sb.heatmap(formation_df, annot = True, cmap = cmap)
    plt.title('Formation heatmap')
    plt.show()

def style_heatmap(list_of_obj):
    for obj in list_of_obj:
        obj.formationAnalysis()
        match_result = obj.result
        match_form_tuple = (match_result[4],match_result[5])
        match_form_tuple_1 = (match_result[5],match_result[4])
        if match_form_tuple in dict_styles:
            dict_styles[match_form_tuple] = [sum(x) for x in zip(dict_styles[match_form_tuple], [match_result[0],match_result[1],1])]
        elif match_form_tuple_1 in dict_styles:
            dict_styles[match_form_tuple_1] = [sum(x) for x in zip(dict_styles[match_form_tuple_1], [match_result[1],match_result[0],1])]

    style_plot = {}
    for style_1 in set_styles:
        list_average = []
        for style_2 in set_styles:
            if (style_1,style_2) in dict_styles:
                if dict_styles[(style_1,style_2)][2] == 0:
                    avg = None
                    list_average.append(avg)
                else:
                    avg = dict_styles[(style_1,style_2)][0]/dict_styles[(style_1,style_2)][2]
                    list_average.append(avg)
            elif (style_2,style_1) in dict_styles:
                if dict_styles[(style_2,style_1)][2] == 0:
                    avg = None
                    list_average.append(avg)
                else:
                    avg = dict_styles[(style_2,style_1)][1]/dict_styles[(style_2,style_1)][2]
                    list_average.append(avg)
            else:
                list_average.append(None)
        style_plot[style_1] = list_average
    style_df = pd.DataFrame(style_plot,index=set_styles)
    print(style_df)
    cmap = sb.cm.rocket_r
    ax = sb.heatmap(style_df, annot = True, cmap = cmap)
    plt.title('Style heatmap')
    plt.show()

    #print(dict_formations)

# Script
getDictsFromFiles()
fromDictToObject(list_of_matches_dict)
arrangeFormations(list_of_matches_obj)
set_formations = arrangeFormations(list_of_matches_obj)
set_styles = arrangeStyles(list_of_matches_obj)
formation_heatmap(list_of_matches_obj)
style_heatmap(list_of_matches_obj)
#list_of_matches_obj[0].avgStamina()
#print(list_of_matches_obj[0].stamina_h_avg,list_of_matches_obj[0].stamina_a_avg)
