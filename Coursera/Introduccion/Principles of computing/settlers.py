import random
#spearmans, archerc, swordsmans, generals
army = [0, 0, 0, 0]
day = 1
loosed = 0
won = 0
#resources: wood, food, stone, metal
res = [15, 15, 10, 0]
#houses, barracks, tower, wall, isbarracks, istower, iswall
builds = [4, '        ', '        ', '        ', 0, 0, 0]
#woodcutters, miners, fishermans, hunters, idlers, max_villagers
workers = [0, 0, 0, 0, 15, builds[0]*5]
all_ppl = workers[0]+workers[1]+workers[2]+workers[3]+workers[4]+army[0]+army[1]+army[2]+army[3]
#lists for table. All table is a bit overloaded but accesibly and can be changed everywhere.
bl1=['|   Resources', '|  Wood: ', '|  Stone: ', '|  Food: ', '|  Metal: ', '|             ']
bl7=['    Villagers', ' Woodcutters: ', ' Miners: ', ' Hunters: ', ' Fishermans: ', ' Idlers: ']
bl10=['      Army ', ' Spearmans: ',  ' Archers: ', ' Swordsmans: ', ' Generals: ', '       ']
#Strings for input messages
questions = ['Greetings, my lord. What do u want to do today?\n 1. Reassign villagers\n 2. Build something \n 3. Next turn \n 4. Exit game',
            'Choose workers to assign.\n1 - woodcutters, 2 - miners, 3 - hunters, 4 - fishermans',
            "Do u want reassign more? 1 for yes, 0 for no",
            'What do u want to build today?\n 1. House(20 wood, 20 stone, +5 dwelling places) \n 2. Barracks(70 wood, 20 stone) \n 3. Tower(100 wood, 100 stone, + 10 dmg in battle)\n 4. Wall(50 wood, 350 stone, + 20 dmg in battle\n 5. Turn village into the city(1500 wood, 1500 stone) \n 6. Nothing',
            "Do you want to train new soldiers?\n 1. Train spearmans(5 wood, 5 stone, 4 hp, 2 dmg)\n 2. Train archers(8 wood, 4 stone, 2 hp, 4 dmg)\n 3. Leave this idea"
            ]
#animals, fish
pools=[35,35]
def get_int(lines):
    #get int without value error
    while True:
        line = ''
        for l in lines:
            line += l
        try:        
            x = int(input(line))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
    return x
ad = [['', '', ''],['','',''],['','',''],['','',''],['','',''],['','',''],['|               |',' ','']]

def status_display():
    global table, bl12, ad
    if builds[4] == 1:
        ad = [[bl10[0], '', bl12[0]],[bl10[1],army[0],bl12[1]],[bl10[2],army[1],bl12[2]],['                |','',''],['                |','',''],['                |','',''],['|               |',' ','']]    
    #displays status table. Dont look here.
    hous_str = str(builds[0])+'('+str(workers[5])+')'
    bl3=['   |', ' ' * (7-len(str(res[0])))+'|' ,' '*(6-len(str(res[1])))+'| ',' '*(7-len(str(res[2])))+'| ',' '*(6-len(str(res[3])))+'| ', '  |']
    bl4=['    Buildings ', ' Houses: ', builds[1], builds[2], builds[3], '']
    bl6=['   |',' '*(6-len(str(builds[0]))-len(str(workers[5])))+'|', '    |', '    |', '    |', '             |']
    bl9=['    |', ' '*(3-len(str(workers[0])))+'|', ' '*(8-len(str(workers[1])))+'|', ' '*(7-len(str(workers[2])))+'|', ' '*(4-len(str(workers[3])))+'|', ' '*(8-len(str(workers[4])))+'|']
    bl12=['     |', ' '*(4-len(str(army[0])))+'|', ' '*(6-len(str(army[1])))+'|', ' '*(3-len(str(army[2])))+'|', ' '*(5-len(str(army[3])))+'|', '         |']
    table = [[bl1[0], '', bl3[0], bl4[0],        '', bl6[0], bl7[0],         '', bl9[0], ad[0][0], ad[0][1]    , ad[0][2]],
         [bl1[1], res[0], bl3[1], bl4[1], hous_str , bl6[1], bl7[1], workers[0], bl9[1], ad[1][0], ad[1][1]    , ad[1][2]],
         [bl1[2], res[1], bl3[2], bl4[2], '    '   , bl6[2], bl7[2], workers[1], bl9[2], ad[2][0], ad[2][1]    , ad[2][2]],
         [bl1[3], res[2], bl3[3], bl4[3], '    '   , bl6[3], bl7[3], workers[2], bl9[3], ad[3][0], ad[3][1]    , ad[3][2]],
         [ad[6][0], ad[6][1], ad[6][2], bl4[4], '    '   , bl6[4], bl7[4], workers[3], bl9[4], ad[4][0], ad[4][1]    , ad[4][2]],
         [bl1[5], ''    , bl3[5], bl4[5], '    '   , bl6[5], bl7[5], workers[4], bl9[5], ad[5][0], ad[5][1]    , ad[5][2]]
         ]
    i = 0
    for list1 in table:
        line = ''
        for elem2 in table[i]:
            line += str(elem2)
        i += 1
        print line
    print

def number_to_worker(number):
    if number == 1:
        worker = 'woodcutter'
    elif number == 2:
        worker = 'miner'
    elif number == 3:
        worker = 'hunter'
    elif number == 4:
        worker = 'fisherman'
    else: 
        worker = "??"
    return worker
        
        
def reassign():
    #function for reassigning workers
    is_reassign_end = 1
    while is_reassign_end:
        print
        choice = 0
        while not (1 <= choice <= 4):
            choice = get_int(questions[1])
        amount = ''
        while not (-workers[choice-1] <= amount <= workers[4]):
            try:
                amount = int(input('How many '+ number_to_worker(choice)+ 's you want reassign? Put negative value if u want to release workers.'))
            except ValueError:
                input('Enter integer value.')
        if not (-workers[choice-1] <= amount <= workers[4]):
            input('You havent enought workers for that action! Press enter to continue.')          
        if 0 < amount <= workers[4]:
            workers[4] -= amount
            workers[choice-1] += amount
        elif -workers[choice-1] <= amount < 0:
            workers[4] -= amount
            workers[choice-1] += amount    
        print 'Now you have: woodcutters: '+str(workers[0]) + ', miners: ' + str(workers[1]) + ',\nhunters: ' + str(workers[2]) + ', fishermans: ' + str(workers[3]) + ', idlers: '+ str(workers[4]) + '.'
        is_reassign_end = ''
        while (is_reassign_end != 0 and is_reassign_end != 1):
            is_reassign_end = get_int(questions[2])

def build_menu():
    global table, bl12, questions, won
    choice = 0
    while not (1 <= choice <= 6):
        choice = get_int(questions[3])
    if choice == 1 and res[0] >= 20 and res[1] >= 20:
        builds[0] += 1
        res[0] -= 20
        res[1] -= 20
        workers[5] = builds[0]*5
        print 'Our villagers built another house! (+5 max villagers)\n' 
    elif 2 <= choice <= 4 and builds[choice+2] == 1:
        input('You already built one!')
    elif choice == 6:
        return
    elif choice == 2 and res[0] >= 70 and res[1] >= 20 and builds[4] == 0:
        i = 0
        for el in builds:
            if el == '        ':
                builds[i] = 'Barracks'
                break
            i += 1
        
        builds[4] = 1
        res[0] -= 70
        res[1] -= 20
        questions[0] += '\n 5. Train soldiers'
        print 'Our villagers built Barracks!(now u can train soldiers)\n'
    elif choice == 3 and res[0] >= 100 and res[1] >= 100 and builds[5] == 0:
        i = 0
        for el in builds:
            if el == '        ':
                builds[i] = 'Tower   '
                break
            i += 1
        builds[5] = 1
        res[0] -= 100
        res[1] -= 100
        print 'Our villagers built Tower!\n'
    elif choice == 4 and res[0] >= 50 and res[1] >= 350 and builds[6] == 0:
        i = 0
        for el in builds:
            if el == '        ':
                builds[i] = 'Wall    '
                break
            i += 1
        builds[6] = 1
        res[0] -= 50
        res[1] -= 350
        print 'Our villagers built Wall!\n'
    elif choice == 5 and res[0] >= 1500 and res[1] >= 1500:
        won = 1
        return
    else:
        input('You haven\'t enough resources for this action.')
    return

def res_calc():
    global news
    died_workers = 0
    if workers[0] > 0:
        harvested_wood = 0
        for i in range(0, workers[0]):
            harvested_wood += random.randint(1,3)
        news += 'Woodcutters harvested ' + str(harvested_wood) + ' wood.\n'
        res[0] += harvested_wood
    if workers[1] > 0:
        harvested_stone = 0
        for i in range(0, workers[1]):
            harvested_stone += random.randint(1,3)
        news += 'Miners harvested ' + str(harvested_stone) + ' stone.\n'
        res[1] += harvested_stone
    if workers[2] > 0:
        harvested_an = 0
        if pools[0] > workers[2]:
            for i in range(0, workers[2]):
                harvested_an += 1
            res[2] += harvested_an
            pools[0] -= workers[2]
            news += 'Hunters harvested ' + str(harvested_an) + ' food.\n'
        else:
            for i in range(0, pools[0]):
                harvested_an += 1
            pools[0] = 0
            res[2] += harvested_an
            news += 'Hunters harvested ' + str(harvested_an) + ' food. Animals is almost gone.\n'
    if workers[3] > 0:
        harvested_fh = 0
        if pools[1] > workers[3]:
            for i in range(0, workers[3]):
                harvested_fh += 1
            res[2] += harvested_fh
            pools[1] -= workers[3]
            news += 'Fishermans harvested ' + str(harvested_fh) + ' food.\n'
        else:
            for i in range(0, pools[1]):
                harvested_fh += 1
            res[2] += harvested_fh
            pools[1] = 0
            news += 'Fishermans harvested ' + str(harvested_fh) + ' food. Fish is almost gone.\n'
    res[2] -= (all_ppl+4) // 5
    news += 'Our people ate %s food.' %((all_ppl+4)//5,)
    if res[2] < 0:
        while res[2] != 0:
            res[2] += 1
            died_workers += 1
            killed = 0
            while not killed:
                for i in range(0, 5):
                    if workers[i] > 0:
                        workers[i] -= 1
                        killed = 1
        news += 'Our people suffering without food! Died %s workers!\n' %(died_workers,)      
        return 

def ppl_calc():
    global news
    all_ppl = workers[0]+workers[1]+workers[2]+workers[3]+workers[4]
    born_ch = all_ppl
    all_ppl += army[0]+army[1]+army[2]+army[3]
    newppl = 0
    workers[5] = builds[0]*5
    while born_ch >= 10:
        if random.randint(1,4) == 4:
            newppl += 1
        born_ch -= 10
    if newppl > 0:
        news += str(newppl) + ' new villagers were born! Strange, but after a few hours they were adult\nenough to cope with a weapon or tool.\n'
    if random.randint(1,8) == 1:
        news += 'A few people have heard about your village and decided to join.\n'
        newppl += random.randint(3,6)
    if newppl <= workers[5]-all_ppl:
        workers[4] += newppl
    elif newppl > workers[5]-all_ppl:
        workers[4] += workers[5]-all_ppl
        news += 'The village haven\'t enough dwelling places and some people had to leave.'
    return

def army_menu():
    #menu for soldiers training. Lists is for choice code optimization.
    res_cost = [5,5,8,4]
    s_name = ['spearmans', 'archers']
    choice = 0
    while choice != 3:	
        quantity = None
        choice = 0
        while not (1 <= choice <= 3):
            choice = get_int(questions[4])
        if 1 <= choice <= 2:
            while not(0 <= quantity <= workers[4]):
                quantity = get_int('How many '+s_name[choice-1]+' you want train? There ' + str(workers[4]) +' idlers.')
            if (res[0] < res_cost[(choice-1)*2]*quantity) or (res[1] < res_cost[(choice-1)*2+1]*quantity):
                input('You havent enough resources for this action!')
            else:
                workers[4] -= quantity
                army[choice-1] += quantity
                res[0] -= res_cost[(choice-1)*2]*quantity
                res[1] -= res_cost[(choice-1)*2]*quantity
                print 'Now '+str(army[choice-1])+' '+s_name[choice-1]+' defends our village.\n'
                
no_attacks = 5  
band_num = 0
def bandits():
    global no_attacks, band_num, news, attackers
    band_num = 0
    if random.randint(1, no_attacks) == 1:
        for i in range(0, (day*3)//7):
            band_num += random.randint(0,1)
        attackers = band_num
        if band_num:
            news += '\nOur village was attacked by %s bandits' %(attackers,)
            band_fight(band_num)
        no_attacks = 5
    else:
        no_attacks -= 1

def pl_army_kill(band_num):
    global loosed, news
    killed_s = 0
    killed_a = 0
    band_stats = band_num*2
    melee_hp = army[0] * 4
    archer_hp = army[1] * 2
    pl_dmg = army[0] * 2 + army[1] * 4
    if melee_hp >= band_stats:
        killed_s = band_stats // 4
    else:
        killed_s = army[0]
        band_attack = (band_stats-(killed_s * 4))
        if archer_hp >= band_attack:
            killed_a = band_attack // 2
        else:
            killed_a = army[1]
            band_attack -= killed_a * 2
            loosed = 1
            return
    band_stats -= army[0] * 2 + army[1] * 4
    army[0] -= killed_s
    army[1] -= killed_a
    band_num = band_stats / 2
    news += '\nWas killed %s spearmans and %s archers' %(killed_s, killed_a)
    return band_num
          
def band_fight(band_num):  
    global news
    build_bonus = builds[5]*10 + builds[6]*20
    band_num -= build_bonus//2
    if band_num > 0:
        while band_num > 0:
            band_num = pl_army_kill(band_num)
    else:
        news += '\nThe enemies were killed on the way to the village.'    
        return
    if not loosed:
        news += '\nAfter a heavy battle we had defended the village.'
     
def day_choice():
    global won

    choice = None
    while choice != 4:
        if won:
            return 3
        choice = get_int(questions[0])
        if choice == 1:
            reassign()
        elif choice == 2:
            build_menu()
        elif choice == 5 and builds[4] == 1:
            army_menu()
        elif choice == 3:
            return 1
        elif choice == 4:
            return 2

def new_turn():
    global news, all_ppl
    for k in range(0,2):
        if pools[k] <= 50:
            pools[k] += 5
    news = 'News:\n'
    res_calc()
    ppl_calc()
    if day >= 10:
        bandits()  
    all_ppl = workers[0]+workers[1]+workers[2]+workers[3]+workers[4]+army[0]+army[1]+army[2]+army[3]
    return    
               
def main():
    global news, loosed, day, won
    end_turn = None
    while(end_turn != 2):
        if won:
            print 'The village turned into a big prosperous city. Glory to you, my lord.\nYou are the winner!'
            return
        print """
======================================================================
================================  NEW DAY  ===========================
======================================================================
              """
        news = ''
        if day != 1:
            new_turn()
        if loosed:
            print "Our village was destroyed by %s bandits!\nDont cry and try again. \nYou survived for %s days" %(attackers, day,)
            return

        else:
            #print "all_ppl", all_ppl, "day", day

            print 'Today is day ' + str(day) + '\nVillage population: ' + str(all_ppl) #%(day)
            status_display()
            print news
            end_turn = 0
            while not end_turn:
                end_turn = day_choice()
            day += 1
print '''
You and some of your compatriots have decided to run 
away from his kingdom ruled by an evil tyrant. After 
long wanderings you have found a lovely village with 
adjacent lakes and forests. Hastily built a few houses 
you start to think about plans for the future ... 
Rules of the game: 
The player can choose to work for the people. 
Resources are added each new move. 
After some time, the village is attacked by bandits. 
Buildings inflict damage on the enemy before the fight. 
To win you have to build a city.
'''
main()