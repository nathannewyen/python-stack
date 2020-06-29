import json
from urllib.request import urlopen

with urlopen("https://raw.githubusercontent.com/ngryman/lol-champions/master/champions.json") as response:
    source = response.read()


data = json.loads(source)
keys = data.keys()
# dictionary
champdict = data.get('data')
champvals = champdict.values()
# print(champvals)

# champvals_keys = champvals.keys()
print(len(champvals))
# print(source)

for values in champdict.values():
    print(values['image'])
    pass
# for i in champvals:
#     print(i['title'])


# "data":{"Aatrox":{"version":"10.9.1","id":"Aatrox","key":"266","name":"Aatrox","title":"the Darkin Blade","blurb":"Once honored defenders of Shurima against the Void, Aatrox and his brethren would eventually become an even greater threat to Runeterra, and were defeated only by cunning mortal sorcery. But after centuries of imprisonment, Aatrox was the first to find...","info":{"attack":8,"defense":4,"magic":3,"difficulty":4},"image":{"full":"Aatrox.png","sprite":"champion0.png","group":"champion","x":0,"y":0,"w":48,"h":48},"tags":["Fighter","Tank"],"partype":"Blood Well","stats":{"hp":580,"hpperlevel":90,"mp":0,"mpperlevel":0,"movespeed":345,"armor":38,"armorperlevel":3.25,"spellblock":32.1,"spellblockperlevel":1.25,"attackrange":175,"preen":3,"hpregenperlevel":1,"mpregen":0,"mpregenperlevel":0,"crit":0,"critperlevel":0,"attackdamage":60,"attackdamageperlevel":5,"attackspeedperlevel":2.5,"attackspeed":0.651}},"Ahri":{"version":"10.9.1","id":"Ahri","key":"103","name":"Ahri","title":"the Nine-Tailed Fox","blurb":"Innately connected to the latent power of Runeterra,
