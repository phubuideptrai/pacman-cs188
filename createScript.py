import os



layout = os.listdir('./layouts')
algorithms = ['MinimaxAgent', 'AlphaBetaAgent', 'ExpectimaxAgent']
functions = ['finalEvaluationFunction', 'oldEvaluationFunction']
for func in functions:
    for level in layout:
        for al in algorithms:
            command = f'python pacman.py -n 5 -l {level[:-4]} -p {al} -a depth=2,evalFn={func} -q\n'
            f = open("script.sh", "a")
            f.write(command)
            f.close()