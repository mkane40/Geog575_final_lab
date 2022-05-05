import csv, json

ds = r'C:\Users\mjkan\Documents\GitHub\final_lab\data\shots_2021_.csv'
csvfile = open(ds, 'r')
jsonfile = open(r'C:\Users\mjkan\Documents\GitHub\final_lab\data\shots_2021.json', 'w')
reader = csv.DictReader(csvfile)
for row in reader:
    json.dump({row['shotID']: (
    row['arenaAdjustedXCord'], row['arenaAdjustedYCord'], row['shooterName'], row['shotType'], row['team'],
    row['teamCode'], row['coords'])}, jsonfile)
    jsonfile.write('\n')

