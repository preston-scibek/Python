import csv

champs = {}
total_games = 28  + 31 + 63 + 78  + 73 + 77 + 80 + 77 + 120 + 114 + 121

with open("wcs.csv") as csvfile:
    c = csv.reader(csvfile)
    for row in c:
        try:
            int(row[1])
        except ValueError:
            continue
        champ = row[0]
        games = int(row[1])
        pickban_per = float(row[2][0:-1])
        ban = int(row[3]) if row[3] != '-' else 0
        pick = int(row[4]) if row[4] != '-' else 0
        champs[champ] = champs.get(champ, {})
        champs[champ]['total_presence'] = champs[champ].get('total_presence', 0) + games
        champs[champ]['bans'] = champs[champ].get('bans', 0) + ban
        champs[champ]['picks'] = champs[champ].get('picks', 0) + pick
        champs[champ]['total_presence_per'] = (champs[champ].get('total_presence_per', 0) + pickban_per ) / 2

champs_presence = [(k,v) for k,v in sorted(champs.items(), key=lambda x: x[1]['total_presence'])]

total_champs = len(champs_presence)
ten_percent = total_champs * .10
top_10percent = champs_presence[::-1][0:int(ten_percent) + 1]

for champ, count in top_10percent:
    print(f"{champ}: {count}")

print("\n"*4)
champs_picks = [(k,v) for k,v in sorted(champs.items(), key=lambda x: x[1]['picks'])]

total_champs = len(champs_picks)
ten_percent = total_champs * .10
top_10percent = champs_picks[::-1][0:int(ten_percent) + 1]

for champ, count in top_10percent:
    print(f"{champ}: {count}")

print("\n"*4)
champs_presence_per = [(k,v) for k,v in sorted(champs.items(), key=lambda x: x[1]['total_presence_per'])]

total_champs = len(champs_presence_per)
ten_percent = total_champs * .10
top_10percent = champs_presence_per[::-1][0:int(ten_percent) + 1]

for champ, count in top_10percent:
    print(f"{champ}: {count}")

