import csv

yearInReview = 'Spotify_YIR_2016.csv'

artistDict = {}
artistList = []

with open(yearInReview) as csvfile:  # change name here to change filename
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        artists = row[1].split(', ')
        for artist in artists:
            artistList.append(artist)


for artist in artistList:
    artistDict.setdefault(artist, 0)
    artistDict[artist] += 1


sortedDict = [(k, artistDict[k]) for k in sorted(artistDict, key=artistDict.get, reverse=True)]

copyString = ''
print('Artist: Number of times they appeared')
for artist in sortedDict:
    print(artist[0] + ': ' + str(artist[1]))
    copyString = copyString + '\n' + str(artist)


