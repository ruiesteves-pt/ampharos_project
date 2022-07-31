# ampharos_project
Scrapper, base de dados e data processing de dados do Footium

# Ampharos_scrapper.py
Scrapper - main(tournament_number,round_number,match_number), retira os dados de cada jogo e formata-os em dictionary.
Daqui guarda cada dict individualmente num ficheiro txt, encontrado em /Match_database/

# Ampharos_classes.py
Definicao de classes, neste momento apenas a class Match esta definida, pode ser expandido depois. As funcoes de calculo para processamento de dados serao aqui adicionadas

# Ampharos_processor.py
Neste momento faz plot dos heatmaps das formações e estilos de jogo. Composta pelas seguintes funções:
getDictsFromFiles(): vai ao directorio definido e organiza todos os ficheiros de txt em dictionaries
fromDictToObject(list_of_dicts): constroi objetos da class Match a partir dos dicts obtidos de ficheiros txt
arrangeFormations(list_of_obj): de uma lista de objectos Match, organiza todas as formações utilizadas num set de formações únicas e depois num dictionary de combinações não repetidas de formações.
arrangeStyles(list_of_obj): igual à arrangeFormations() mas para estilos
formation_heatmap(list_of_obj): organiza e calcula a média de pontos obtidos entre cada confronto de formações. Por uma série de processamento de dados, compila os dados numa DataFrame de Pandas e dá plot num heatmap.
style_heatmap(list_of_obj): o mesmo mas para estilos.

# /Match_database/
Directorio com ficheiros .txt de todos os jogos
