import random
print("If you want to exit type 0 in any of number inputs")
Exit=""
while(Exit!="Exit"):
    e = 1
    while(e>0):
        LiczbaGraczy = int(input('Wpisz Liczbę Graczy '))
        if(LiczbaGraczy==0):
            exit()
        LiczbaTeamów = int(input('Wpisz Liczbę Teamów '))
        if(LiczbaTeamów==0):
            exit()
        LiczbaGraczyWTeamie = int(input('Wpisz Liczbę Graczy w Teamie '))
        if(LiczbaGraczyWTeamie==0):
            exit()
        if(LiczbaGraczy>LiczbaTeamów*LiczbaGraczyWTeamie):
            print("Liczba Graczy jest za duża lub ilość teamów jest za mała.")
        else:
            if(LiczbaGraczy<LiczbaTeamów):
              print("Liczba graczy nie może być większa od liczby teamów")
            else:
                if(LiczbaGraczy<=LiczbaTeamów*LiczbaGraczyWTeamie and LiczbaGraczy>=LiczbaTeamów):
                  break
    ListaGraczy=[]
    i = 1
    c = LiczbaTeamów
    d = LiczbaGraczy
    while(d%c != 0):
        ListaGraczy+=[i]
        d+=1
        if(d%c == 0):
            break
    while(i>0):
         print('Wpisz ',i,' Gracza')
         Gracz = [input()]
         ListaGraczy += Gracz
         i += 1
         if(i>LiczbaGraczy):
            break
    a = 1
    b = 1
    while(a>0):
         print(a,'Team to:')
         while(b>0):
          Gracz1 = random.choice(ListaGraczy)
          ListaGraczy.remove(Gracz1)
          print('-',Gracz1)
          b+=1
          if(b>LiczbaGraczyWTeamie):
              break
         b-=LiczbaGraczyWTeamie
         a+=1
         if(a>LiczbaTeamów):
             break
    print("Jeśli chcesz wyjść Wpisz \"Exit\"")
    Exit = input()
