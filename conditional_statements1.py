colour = input('What is you favourite colour?')
print('I like '+colour+' too.')

#Let us see an example of an if statement
if colour == 'blue':
    #Only if the colour is exactly 'blue' will we say "Good choice ..."
    print('Good choice - blue is my favourite colour too.')


#Let us see an example of an if-else statement
#If the colour is 'blue' then we will say "Good choice ..." or ELSE we
#will say that we like the colour the user has supplied
if colour =='blue':
    print('Good choice - blue is my favourite colour too.')
else:
    print('I like '+colour+' too!')


    
#Let us see an example of an if-elif statement
#If the colour is 'blue' we will print "Good choice..." or else we
#will check another condition, if the colour was 'red' then we will
#display that we do not like red or else we like whatever colour the
#user has supplied
if colour =='blue':
    print('Good choice - blue is my favourite colour too.')
elif colour =='red':
    print('Sorry, I do not like red!')
else:
    print('I like '+colour+' too!')
