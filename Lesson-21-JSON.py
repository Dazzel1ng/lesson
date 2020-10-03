import _json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'Playername' : 'Dazzeling',
    'Score' : 456,
    'awards' : ["OR", "NV", "NY"]
}

player2 = {
    'Playername' : 'Toppaer',
    'Score' : 104,
    'awards' : ["MA", "MAK", "NOM"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)
   #---------SAVE by JSON----------
_json.dump(myplayers, myfile)
myfile.close()

  #----------- LADO by JSON----------------

myfile = open(filename, mode='r', encoding='Latin=1')
_json_data = _json.load(myfile)

for user in _json_data:
    print("player Name is:" + str(user['PlayerName']))
    print("Player Score is:" + str(user['Score']))
    print("play Award №1" + str(user['Awards'][0]))
    print("play Award №2" + str(user['Awards'][1]))
    print("play Award №3" + str(user['Awards'][2]))
    print("-----------------------\n\n")