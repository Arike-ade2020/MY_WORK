names = {'john', 'jacob', 'anabel', 'jonathan', 'jack', 'tabita', 'winfred', 'jalong',}

#for names that start with 'j'
for i in names: 
    if i .startswith('j'): 
        i == True 
        print ('its {} that {} begins with a "j"' .format(True, i))
    else: 
        i == False
        print ('its {} that {} begins with a "j"' .format(False, i))
# FOR LONGEST WORD 
print ('the longestword is {}' .format (max(names, key=len)))
#FOR SORT AND INDEX 
names.sort()
for idx, val in enumerate(names):
    print ('{} has an index of {}' .format(val,idx))

# for lenth of words 
#for i in names:
    #print('{} = {}'.format(i,len(i),))