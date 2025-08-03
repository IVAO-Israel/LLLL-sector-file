from geopy.point import Point

def decimal_to_dms(decimal_coord, is_latitude):
    """
    Converts a decimal coordinate to DMS format with the convention NDD.MM.SS.SSS;EDD.MM.SS.SSS;
    """
    degrees, minutes = divmod(abs(decimal_coord) * 60, 60)
    minutes, seconds = divmod(minutes * 60, 60)
    direction = ('N' if is_latitude else 'E') if decimal_coord >= 0 else ('S' if is_latitude else 'W')
    return f"{direction}{int(degrees):03d}.{int(minutes):02d}.{seconds:06.3f}"

def convert_coordinates(data):
    """
    Converts the LONG and LAT fields in the JSON data to the required DMS format.
    """
    coo_list = ["//[VFRFIX]"]
    for key, value in data.items():
        vfr_type = -1
        if value['type'] == 'דרישה':
            vfr_type = 1
        else:
            vfr_type = 0
        
        if 'LONG' in value and 'LAT' in value:
            long_dms = decimal_to_dms(value['LONG'], is_latitude=False)
            lat_dms = decimal_to_dms(value['LAT'], is_latitude=True)
            value['DMS'] = f"{lat_dms};{long_dms};"
            aurora_format = f"{value['CODE']};;{value['DMS']}{vfr_type}"
            coo_list.append(aurora_format)
    return coo_list

if __name__ == "__main__":
    import json

    # Load the JSON data
    with open("Include/IL/scripts/vfr_heb.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Convert coordinates
    updated_data = convert_coordinates(data)

    # print('\n'.join(updated_data))

    # # Save the updated JSON data
    with open("Include/IL/LLBG/LLBG.vfi", "w", encoding="utf-8") as file:
        for line in updated_data:
            file.write(line + "\n")