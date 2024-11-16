def les_song_contest(fil):
    years = []
    countries = []
    song_contest = {}

    for line in fil:
        kol = line.strip("\n").split()
        years.append(kol[0])
        countries.append(kol[1])
        song_contest[kol[0]] = kol[1]
    
    return song_contest

f = open("song_contest.txt", "r")
res = les_song_contest(f)
for ting in res:
    print(ting, res[ting])


f.close()
