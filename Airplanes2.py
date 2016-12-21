f = open("AviationData.txt")
aviation_data = f.readlines()
aviation_list = [line.split(' | ') for line in aviation_data]
for element in aviation_list:
    element.remove('\n')

aviation_dict_list = []
keys = aviation_list[0]

for flight in aviation_list[1:]:
    d = {}
    for i, element in enumerate(flight):
        d[keys[i]] = element
    aviation_dict_list.append(d)

monthly_injuries = {}
for d in aviation_dict_list:
    if d["Event Date"] != "":
        date_list = d["Event Date"].split("/")
        month = date_list[0]
        year = date_list[2]
    else:
        month, year = 'Unknown', 'Unknown'
    try:
        fatal_injuries = int(d["Total Fatal Injuries"])
    except Exception:
        fatal_injuries = 0
    try:
        serious_injuries = int(d["Total Serious Injuries"])
    except Exception:
        serious_injuries = 0
    injuries = fatal_injuries + serious_injuries
    key = "-".join((year, month))
    if key in monthly_injuries:
        monthly_injuries[key] += injuries
    else:
        monthly_injuries[key] = injuries
print(monthly_injuries)
sorted_dates = sorted(monthly_injuries)
sorted_fatalities = []
for date in sorted_dates:
    sorted_fatalities.append(monthly_injuries[date])
for i in range(len(sorted_fatalities)):
    print(sorted_dates[i],":",sorted_fatalities[i])