print('')
print('')
print('                         ************')
print('                         * QUESTERS *')
print('                         ************')
print('')
print('                 Version: 0.1.0')
print('               Copyright: The Scriba Family 2019')

config=open('questers.config','r')

line=config.readline()

screens={}

while line:
    linelist=line.strip('\n').split('|')

    if len(linelist)==4:
        if linelist[0] not in screens:
            screens[linelist[0]]={}
        if linelist[1] not in screens[linelist[0]]:
            screens[linelist[0]][linelist[1]]={}
        screens[linelist[0]][linelist[1]][linelist[2]]=linelist[3]
    line=config.readline()

current_screen='0'
selection=current_screen

while selection!='q':
    
    print('')
    print(' ======================================================')
    print('')
    print(' *********************************************')
    if selection!='0':
        try:
            current_screen=screens[current_screen][selection]['d']
        except:
            print('   Invalid choice. Please try again...')
            print('')
    print('   ' + str(screens[current_screen]['0']['t']))
    print(' *********************************************')
    print('')
    print('What would you like to do?')
    if len(screens[current_screen])>1:
        for i in screens[current_screen]:
            if i!='0':
                print (str(i)+': '+str(screens[current_screen][str(i)]['t']))
    print('q: Quit the game')
    print('')

    selection=input('Choose your option:')
    
