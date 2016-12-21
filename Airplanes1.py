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

lax_dict = []
for d in aviation_dict_list:
    if 'LAX94LA336' in d.values():
        lax_dict.append(d)

state_accidents = {}
for d in aviation_dict_list:
    try:
        location = d["Location"].split(", ")
        state = location[1]
    except Exception:
        state = d["Location"]
    if state in state_accidents:
        state_accidents[state] += 1
    else:
        state_accidents[state] = 1
for key, value in state_accidents.items():
    if value == max(state_accidents.values()):
        print(key,": ",value)