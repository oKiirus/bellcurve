import random as rd
import plotly.figure_factory as px

rolls = []



for i in range(1, 1000):
    dice1 = rd.randint(1, 6)
    dice2 = rd.randint(1, 6)

    rolls.append(dice1 + dice2)

    

graph = px.create_distplot([rolls], ['hi'])

graph.show()



