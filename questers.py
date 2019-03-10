print('')
print('')
print('                         ************')
print('                         * QUESTERS *')
print('                         ************')
print('')
print('                 Version: 0.1.1')
print('               Copyright: The Scriba Family 2019')

config=open('questers.config','r')

line=config.readline()

scenes={}

while line:
    linelist=line.strip('\n').split('|')

    if len(linelist)==4:
        if linelist[0] not in scenes:
            scenes[linelist[0]]={}
        if linelist[1] not in scenes[linelist[0]]:
            scenes[linelist[0]][linelist[1]]={}
        if linelist[2] not in scenes[linelist[0]][linelist[1]]:
            scenes[linelist[0]][linelist[1]][linelist[2]]={}
        scenes[linelist[0]][linelist[1]][linelist[2]][str(len(scenes[linelist[0]][linelist[1]][linelist[2]]))]=linelist[3]
    line=config.readline()

current_scene='0'
selection=current_scene

while selection!='q':
    
    print('')
    print(' ======================================================')
    print('')
    print(' *********************************************')
    if selection!='0':
        try:
            current_scene=scenes[current_scene][selection]['d']['0']
        except:
            print('   Invalid choice. Please try again...')
            print('')
    for i in scenes[current_scene]['0']['t']:
        print('   ' + str(scenes[current_scene]['0']['t'][i]))
    print(' *********************************************')
    print('')
    print('What would you like to do?')
    if len(scenes[current_scene])>1:
        for i in scenes[current_scene]:
            if i!='0':
                if 't' in scenes[current_scene][str(i)]:
                    for j in scenes[current_scene][str(i)]['t']:
                        if j=='0':
                            print (str(i)+': '+str(scenes[current_scene][i]['t'][j]))
                        else:
                            print ('   '+str(scenes[current_scene][i]['t'][j]))
    print('q: Quit the game')
    print('')

    selection=input('Choose your option: ')
    
