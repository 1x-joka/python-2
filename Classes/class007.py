# ============== LISTS ==============

results = ['Mario', 'Luigi'] # brackets (english) = colchetes (português)

results.append('Princess') # append adds a new element to the end in list
results.append('Yoshi')
results.append('Koopa Troopa')
results.append('Toad')

results.append(['Bowser', 'Donkey Kong Jr.'])
results.remove(['Bowser', 'Donkey Kong Jr.'])
results.extend(['Bowser', 'Donkey Kong Jr.']) # takes each of the elements of the list (['Bowser', 'Donkey Kong Jr.']) and add, individually, in our original list, without "[]"

results.remove('Bowser') # remove is a list method who search the first instance of Bowser and remove that element

results.insert(0, 'Bowser') # let's say Bowser wants stay in first of the podium (represented for zero, the first argument), we have add him with list method "instance" because "append" add for the last place in our list

results.reverse() # Donkey Kong Jr stay in first place, Toad in second...

print(results)