import random

direction=["L","M","R","UL","UR"]
teams=['Argentina','Brazil','Germany','Spain','Portugal','France','Belgium','England','Croatia','Uruguay','Colombia','India']

gk_arg=['Sergio Romero','Willy Caballero']
gk_br=['Ederson','Alisson Becker']
gk_ger=['Manuel Neuer','Marc-Andre Ter Stegen']
gk_por=['Anthony Lopes','Rui Patiricio']
gk_esp=['David de Gea','Kepa Arrizabalaga']
gk_fra=['Hugo Lloris','Alphonse Areola']
gk_bel=['Thibaut Courtois','Simon Mignolet']
gk_eng=['Jack Butland','Jordan Pickford']
gk_cro=['Danijel Subasic','Lovre Kalinic']
gk_uru=['Fernando Muslera','Martin Silva']
gk_col=['David Ospina','Camilo Vargas']
gk_ind=['Subrata Pal','Gurpreet Singh Sandhu']

onfield_arg=['Lionel Messi','Sergio Aguero','Gonzalo Higuan','Paulo Dybala','Angel Di Maria']
onfield_br=['Neymar Jr.','Philippe Coutinho','Gabriel Jesus','Roberto Firmino','Willian']
onfield_ger=['Marcos Reus','Mesut Ozil','Tony Kroos','Timo Werner','Thomas Muller']
onfield_por=['Cristiano Ronaldo','Bernado Silva','Andre Silva','Ricardo Quaresma','Pepe']
onfield_esp=['Diego Costa','Sergio Ramos','Andres Iniesta','Isco','David Silva']
onfield_fra=['Antoine Griezmann','Kylian Mbappe','Paul Pogba','Olivier Giroud','Ousmane Dembele']
onfield_bel=['Eden Hazard','Kevin de Bruyne','Romelu Lukaku','Dries Mertens','Yannick Carrasco']
onfield_eng=['Harry Kane','Dele Alli','Jesse Lingard','Raheem Sterling','Marcus Rashford']
onfield_cro=['Luka Modric','Ivan Rakitic','Mario Mandzukic','Ivan Perisic','Mateo Kovacic']
onfield_uru=['Luis Suarez','Edinson Cavani','Diego Godin','Jose Gimenez','Lucas Torreira']
onfield_col=['James Rodriguez','Radamel Falcao','Juan Cuadrado','Juan Quintero','Yerry Mina']
onfield_ind=['Sunil Chhetri','Jeje Lalpekhlua','Sandesh Jhingan','Jackichand Singh','Lalrindika Ralte']

ShooterScore=0
KeeperScore=0
print("-----WELCOME TO THE PYTHON PENALTY SHOOTOUT----")
print("      ________________________________     ")
print("      |                              |     ")
print("      |                              |     ")
print("      |      !!Penalty Shootout!!    |     ")
print("      |                              |     ")
print("______|______________________________|_____")
print("\n\nNote: This game's inputs are case sensitive. Kindly check the Caps Lock when not needed")
print("The options you can choose are:\nL for Left\nR for Right\nM for Middle\nUR for Upper Right\nUL for Upper Left")
print("----------------AVAILABLE TEAMS:--------------------------\n",teams)

def Get_Players():
    
  gk_team = input("\nChoose  Team of Goalkeeper: ")
  if gk_team == 'Argentina':
    print("Available Goalkeeper: ", gk_arg)
    ch = input("Choose One: ")
  elif gk_team == 'Uruguay':
    print("Available Goalkeeper: ", gk_uru)
    ch = input("Choose One: ") 
  elif gk_team == 'Brazil':
    print("Available Goalkeeper: ", gk_br)
    ch = input("Choose One: ")
  elif gk_team == 'Portugal':
    print("Available Goalkeeper: ", gk_por)
    ch = input("Choose One: ")
  elif gk_team == 'Germany':
    print("Available Goalkeeper: ", gk_ger)
    ch = input("Choose One: ")       
  elif gk_team == 'Spain':
    print("Available Goalkeeper: ", gk_esp)
    ch = input("Choose One: ")
  elif gk_team == 'Belgium':
    print("Available Goalkeeper: ", gk_bel)
    ch = input("Choose One: ")
  elif gk_team == 'France':
    print("Available Goalkeeper: ", gk_fra)
    ch = input("Choose One: ")
  elif gk_team == 'England':
    print("Available Goalkeepers: ", gk_eng)
    ch = input("Choose One: ")
  elif gk_team == 'Croatia':
    print("Available Goalkeepers: ", gk_cro)
    ch = input("Choose One: ")
  elif gk_team == 'Colombia':
    print("Available Goalkeepers: ", gk_col)
    ch = input("Choose One: ")
  elif gk_team == 'India':
    print("Available Goalkeepers: ", gk_ind)
    ch = input("Choose One: ")         

  pl_team = input("\nChoose Team of Shooter: ")
  if pl_team == 'Argentina':
    print("Available Players:", onfield_arg)
    c = input("Choose One: ")
  elif pl_team == 'Uruguay':
    print("Available Players: ", onfield_uru)
    c = input("Choose One: ") 
  elif pl_team == 'Brazil':
    print("Available Players: ", onfield_br)
    c = input("Choose One: ")
  elif pl_team == 'Portugal':
    print("Available Players: ", onfield_por)
    c = input("Choose One: ")
  elif pl_team == 'Germany':
    print("Available  Players: ", onfield_ger)
    c = input("Choose One: ")       
  elif pl_team == 'Spain':
    print("Available Players: ", onfield_esp)
    c = input("Choose One: ")
  elif pl_team == 'Belgium':
    print("Available Players: ", onfield_bel)
    c = input("Choose One: ")
  elif pl_team == 'France':
    print("Available Players: ", onfield_fra)
    c = input("Choose One: ")
  elif pl_team == 'England':
    print("Available Players: ", onfield_eng)
    c = input("Choose One: ")
  elif pl_team == 'Croatia':
    print("Available Players: ", onfield_cro)
    c = input("Choose One: ")
  elif pl_team == 'Colombia':
    print("Available Players: ", onfield_col)
    c = input("Choose One: ")
  elif pl_team == 'India':
    print("Available Players: ", onfield_ind)
    c = input("Choose One: ")     

  goals = ['He strikes it clean. The Keeper had no chance what so ever','Its a GOAAALLLLLL!!','He puts it in the net!!']
  val = int(input("Press 1 to start play as shooter\nPress 2 to start play as goalkeeper"))
  if val == 1:
    for i in range(5):
      penaltyFor(c, ch, goals)
    Score_Shooter() 
  elif val == 2:
    for i in range(5):
      penaltyAgainst(c, ch, goals)
    Score_Keeper()
  else:
    print("You didn't choose a valid input")

def penaltyFor(c, ch, g):
    global ShooterScore
    playerShotDirection=input("Pick your spot:").lower()
    keeperDive=random.choice(direction)
    print("The keeper dives to the "+ keeperDive.upper())
    if playerShotDirection=="L" and keeperDive=="R":
        print ( "And it's a save! Brilliant work by %s to dive on his right" % ch)
    elif playerShotDirection=="R" and keeperDive=="L":
        print ("It's a save! %s Misses it this time" % c)
    elif playerShotDirection=="M" and keeperDive=="M":
        print ("And % saves it! My god.. this can be very crucial miss by %s" % (ch, c))
    elif playerShotDirection=="UR" and keeperDive=="UL":
        print("It's a save! Good work by %s" % ch)
    elif playerShotDirection=="UL" and keeperDive=="UR":
        print("It's a save!")        
    else:
        print("     ________________________________     ")
        print("     |                              |     ")
        print("     |                              |     ")
        print("     |       !!GOAAALLLLLL!!        |     ")
        print("     |                              |     ")
        print("_____|______________________________|_____")
        print(random.choice(g))
        print("%s scores" % c)
        ShooterScore+=1

def penaltyAgainst(c, ch, g):
    global KeeperScore
    playerKeeperDive=input("Choose dive direction:").lower()
    computerShotDirection=random.choice(direction)
    print ("%s hits the ball to the " % (c) +computerShotDirection)
    if computerShotDirection=="L" and playerKeeperDive=="R":
        print ( "And it's a save! Brilliant work by %s to dive on his right"% ch)
        KeeperScore +=1
    elif computerShotDirection=="R" and playerKeeperDive=="L":
        print ("It's a SAVE!!!!!! How crucial can this be?")
        KeeperScore +=1
    elif computerShotDirection=="M" and playerKeeperDive=="M":
        print ("It's a save! %s Misses it this time" % c)
        KeeperScore +=1
    elif computerShotDirection=="UR" and playerKeeperDive=="UL":
        print(" Oh my god! Are we witnessing the best goalkeeper. He saves it")
        KeeperScore += 1
    elif computerShotDirection=="UL" and playerKeeperDive=="UR":
        print("Oh what a save!! %s at his best" % ch )
        KeeperScore += 1
    else:
        print("     ________________________________     ")
        print("     |                              |     ")
        print("     |                              |     ")
        print("     |       !!GOAAALLLLLL!!        |     ")
        print("     |                              |     ")
        print("_____|______________________________|_____")
        print("%s Scores!!" % c)
        print(random.choice(g))

def Score_Shooter():
    print("You scored %d out of 5" % ShooterScore)
def Score_Keeper():
    print("You saved %d out of 5" % KeeperScore)    
Get_Players()
