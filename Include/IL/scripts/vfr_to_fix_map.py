
import json
from convert_coordinates import decimal_to_dms


with open("Include/IL/scripts/vfr_heb.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    d = {}
    for k,v in data.items():
        d[v['name']] = v['CODE']

with open("Include/IL/scripts/vfr_airways.json", "r", encoding="utf-8") as file:
    aw_data = json.load(file)
    i = 1
    routes = []
    for v in aw_data:
        start = d[v['start_point']]
        end = d[v['end_point']]
        points = []
        if 'points' in v:
            points = [f"{decimal_to_dms(p['lat'], True)};{decimal_to_dms(p['long'], False)}" for p in v['points']]
        routes.append(f"{start}-{end};{i};{start};{start};")
        if points:
            for p in points:
                routes.append(f"{start}-{end};{i};{p};")
        routes.append(f"{start}-{end};{i};{end};{end};")
        i += 1


with open("Include/IL/LLBG/LLBG.vrt", "w", encoding="utf-8") as file:
    file.write("\n".join(routes))
