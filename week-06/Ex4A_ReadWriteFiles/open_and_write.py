f = open('about_me.txt', 'a')
f.close()

# Open in append mode to add to existing content
f = open('about_me.txt', 'a')

f.write('\n')
f.write('Perfect night out:\n')
f.write('My perfect night out would be dinner at a great restaurant,\n')
f.write('followed by live music or a comedy show with close friends.\n')

f.close()