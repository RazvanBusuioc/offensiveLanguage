import csv
import os
import plotly.graph_objects as go

file = open("HSOL.csv", "r")
reader = csv.reader(file)
header = next(reader)

count = []
classes = []

for row in reader:
    count.append(int(row[1]))
    classes.append(int(row[5]))

hateNr = len([x for x in classes if x == 0])
offNr = len([x for x in classes if x == 1])
neitherNr = len([x for x in classes if x == 2])

fig = go.Figure(data=[go.Bar(
    x=['Hate', 'Offensive', 'Neither'],
    y=[hateNr, offNr, neitherNr],
    texttemplate="%{y}",
    marker_color=["red", "purple", "green"] # marker color can be a single color value or an iterable
)])
fig.update_layout(yaxis=dict(
        title='Number of tweets',
        titlefont_size=16,
        tickfont_size=14,
    ),xaxis=dict(
        titlefont_size=16,
        tickfont_size=14,
    ))
fig.show()




file = open("HSWS.csv", "r")
reader = csv.reader(file)
header = next(reader)

count = []
classes = []

for row in reader:
    classes.append(str(row[4]))

hateNr = len([x for x in classes if x == "hate"])
noHateNr = len([x for x in classes if x == "noHate"])
skipNr = len([x for x in classes if x == "idk/skip"])
relationNr = len([x for x in classes if x == "relation"])

print(hateNr, noHateNr, skipNr, relationNr)

fig = go.Figure(data=[go.Bar(
    x=['Hate', 'NoHate', 'Skip', 'Relation'],
    y=[hateNr, noHateNr, skipNr, relationNr],
    texttemplate="%{y}",
    marker_color=["red", "purple", "green", "blue"] # marker color can be a single color value or an iterable
)])
fig.update_layout(yaxis=dict(
        title='Number of sentences',
        titlefont_size=16,
        tickfont_size=14,
    ),xaxis=dict(
        titlefont_size=16,
        tickfont_size=14,
    ))
fig.show()
#ZOOM IN AT 200% AND SS