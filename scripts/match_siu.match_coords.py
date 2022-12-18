import csv

lookup = {}

# DO NOT USE, this does not work AT ALL
# can't match coordinates reliably
# misses by far (i get like 100 chests off)

def trim(x):
    d = 1000 # round to nearest d
    return round(x/d)*d

def get_key(x,y):
    x = float(x) if x else 0
    y = float(y) if y else 0
    key = (trim(x), trim(y))
    return key

c = csv.DictReader(open('DLC2_Complete.csv'))
for o in c:
    x = o['location_x']
    y = o['location_y']
    key = get_key(x,y)
    lookup[key] = o

init = True
total = 0
matched = 0
c = csv.DictReader(open('chests.orig.csv'))
for o in c:
    x = o['x']
    y = o['y']
    key = get_key(x,y)

    total += 1
    if key in lookup:
        o['id'] = lookup[key]['object_name']
        matched += 1
    else:
        o['id'] = ''

    if init:
        init = False
        w = csv.DictWriter(open('chests.matched.csv', 'w'), o.keys())
        w.writeheader()

    w.writerow(o)

print('%d total, %d matched, %d unmatched' %(total, matched, total-matched))
