import random
print("If you want to exit type 0 in any of number inputs")
Exit=""
while(Exit!="Exit"):
    e = 1
    while(e>0):
        NumOfPlayers = int(input('Type in Number of Players '))
        if(NumOfPlayers==0):
            exit()
        NumOfTeams = int(input('Type in Number of Teams '))
        if(NumOfTeams==0):
            exit()
        NumOfPlayersInTeam = int(input('Type in Number of Players w Teamie '))
        if(NumOfPlayersInTeam==0):
            exit()
        if(NumOfPlayers>NumOfTeams*NumOfPlayersInTeam):
            print("NumOf Players jest za duża lub ilość teamów jest za mała.")
        else:
            if(NumOfPlayers<NumOfTeams):
              print("NumOf graczy nie może być większa od liczby teamów")
            else:
                if(NumOfPlayers<=NumOfTeams*NumOfPlayersInTeam and NumOfPlayers>=NumOfTeams):
                  break
    ListaPlayers=[]
    i = 1
    c = NumOfTeams
    d = NumOfPlayers
    while(d%c != 0):
        ListaPlayers+=[i]
        d+=1
        if(d%c == 0):
            break
    while(i>0):
         print('Type in ',i,' Player')
         Player = [input()]
         ListaPlayers += Player
         i += 1
         if(i>NumOfPlayers):
            break
    a = 1
    b = 1
    while(a>0):
         print(a,'Team is:')
         while(b>0):
          Player1 = random.choice(ListaPlayers)
          ListaPlayers.remove(Player1)
          print('-',Player1)
          b+=1
          if(b>NumOfPlayersInTeam):
              break
         b-=NumOfPlayersInTeam
         a+=1
         if(a>NumOfTeams):
             break
    print("If you want to leave Type "Exit"")
    Exit = input()
