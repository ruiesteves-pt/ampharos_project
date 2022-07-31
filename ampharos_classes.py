# Footium Ampharos algorithm v1
# @ruiesteves
# Class definitions


class Match:

    # Constructor class
    def __init__(self,team_h,team_a,score_h,score_a,formation_h,formation_a,style_h,
    style_a,line_up_h,line_up_a,total_shots_h,total_shots_a,shots_target_h,shots_target_a,rating_h,rating_a):
        self.team_h = team_h                # String
        self.team_a = team_a                # String
        self.score_h = score_h              # Integer
        self.score_a = score_a              # Integer
        self.formation_h = formation_h      # String
        self.formation_a = formation_a      # String
        self.style_h = style_h              # String
        self.style_a = style_a              # String
        self.line_up_h = line_up_h          # List of players (Class)
        self.line_up_a = line_up_a          # List of players (Class)
        self.total_shots_h = total_shots_h  # Integer
        self.total_shots_a = total_shots_a  # Integer
        self.shots_target_h = shots_target_h  # Integer
        self.shots_target_a = shots_target_a  # Integer
        self.rating_h = rating_h            # List of integers
        self.rating_a = rating_a            # List of integers


    # formationAnalysis sees which formation and style won and lost, assigns points to each (BETTER WAY TO DO THIS?)
    def formationAnalysis(self):
        if self.score_h > self.score_a:
            self.result = [3,0,self.formation_h,self.formation_a,self.style_h,self.style_a] # [points home, points away, formation home, formation away, style home, style away]
        elif self.score_h == self.score_a:
            self.result = [1,1,self.formation_h,self.formation_a,self.style_h,self.style_a] # [points home, points away, formation home, formation away, style home, style away]
        else:
            self.result = [0,3,self.formation_h,self.formation_a,self.style_h,self.style_a] # [points home, points away, formation home, formation away, style home, style away]


    def avgStamina(self):
        list_lineups = [self.line_up_h, self.line_up_a]
        #list_lineups = [self.line_up_h]
        stamina_avg = []
        for lineup in list_lineups:
            stamina_list = []
            l = range(len(lineup))
            for i in l:
                if i == 0:
                    None
                elif i <= 10 and i >= 1:
                    stamina = int(lineup[i]['stamina'].replace('%',''))
                    stamina_list.append(stamina)
                    #print(stamina_list)
                else:
                    None
            a = 0
            for i in stamina_list:
                a = a + i
            stamina_single_avg = a/len(stamina_list)
            #print(stamina_single_avg)
            stamina_avg.append(stamina_single_avg)
        self.stamina_h_avg = stamina_avg[0]
        self.stamina_a_avg = stamina_avg[1]

    def isGhost(self):
        if self.stamina_h_avg <= 45 and self.stamina_a_avg <= 45:
            self.ghost_h = True
            self.ghost_a = True
        elif self.stamina_h_avg <= 45 and self.stamina_a_avg > 45:
            self.ghost_h = True
            self.ghost_a = False
        elif self.stamina_h_avg > 45 and self.stamina_a_avg <= 45:
            self.ghost_h = False
            self.ghost_a = True
        else:
            self.ghost_h = False
            self.ghost_a = False
        #print(self.ghost_h, self.ghost_a)
