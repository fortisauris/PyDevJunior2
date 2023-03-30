
'''
JSON -
'''

import json

a = ['Data', {'World': 56746, 'Amerika':6547, 'Europa':[234,654,765]}]
vystup = json.dumps(a)
print(vystup)

vystup = json.dumps(a, separators=(',',':'))
print(vystup)

vystup = json.dumps(a, separators=(',',':'), sort_keys=True)
print(vystup)

vystup = json.dumps(a, separators=(',',':'), sort_keys=True, indent=4)
print(vystup)

vstup = json.loads(vystup)
print(vstup)


'''
def save_json_file(filename_w_path: str, data: dict):
    with open(filename_w_path, mode='w', encoding='utf8') as f:
        json.dump(data, f, indent=4, sort_keys=True)
        return

save_json_file(filename_w_path='skuska.json', data=a)
'''

def load_json_file(filename_w_path: str):
    with open(filename_w_path, mode='r', encoding='utf8') as f:
        loaded_data = json.load(f)
    return loaded_data


data = load_json_file('skuska.json')
print(data)
for i in data:
    print(i)
