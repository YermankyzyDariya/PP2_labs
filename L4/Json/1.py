import json
with open("/Users/daryaermankyzy/Desktop/Новая папка/L4/Json/sample-data.json" , "r") as f:
    data = json.load(f)
print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-"*80)


for item in data["imdata"]:
    
    attr = item["l1PhysIf"]["attributes"]
    dn = attr["dn"] if "dn" in attr else "N/A"
    descr = attr["descr"] if "descr" in attr else "N/A"
    speed = attr["speed"] if "speed" in attr else "N/A"
    mtu = attr["mtu"] if "mtu" in attr else "N/A"
    
   
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")