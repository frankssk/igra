player = {"health": 100, "damage": 10}
enemy = {"health": 100, "damage": 15}
imy1 = "player1"
imy2 = "player2"
def imy(i):
    b = str(input(f"vvedi svoe imy {i} "))
    return b
player["name"] = imy(imy1)
enemy["name"] = imy(imy2)
def fite(a, b):
    c = a - b
    return c
def pl1():
    player["health"] = fite(player["health"], enemy["damage"])
def pl2():
    enemy["health"] = fite(enemy["health"], player["damage"])

while player["health"] > 0:
    print(player)
    print(enemy)
    pl1()
    print(player)
    if player["health"] <= 0:
        print("pobedil " + enemy["name"])
        break
    pl2()
    print(enemy)
    if enemy["health"] <= 0:
        print("pobedil " + player["name"])
        break
print("end")