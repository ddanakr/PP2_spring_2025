import json

json_file = 'sample_data.json'

with open(json_file, 'r') as file:
    data = json.load(file)


elements = data["imdata"][:3]
print("Interface Status")
print("=" * 85)
print(f"{'DN':<50}{'Descriptions':<20}{'Speed':<10}{'MTU'}")
print("-"*85)


for i in elements:
    attr = i["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    speed = attr.get("speed", "")
    mtu = attr.get("mtu", "")
    print(f"{dn:<50}{'':<20}{speed:<10}{mtu}")