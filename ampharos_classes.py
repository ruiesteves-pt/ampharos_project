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
