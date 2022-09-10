# Automating Decision-Making
# Choose ANIME to watch

anime = ['Attack on Titan', 'Death Note', 'Fullmetal Alchemist', 'One Punch Man', 'Sword Art Online', 'Naruto']
themes = ['Military', 'Psychological', 'Gore', 'Parody', 'Video Games', 'Martial Arts']

print("Hi! Today I'll help you to choose an anime to watch!")
print('First, one question...')
print('Choose from this THEMES: Military, Psychological, Gore, Parody, Video Games, Martial Arts')

theme = input('What is your theme? ')

for items in themes:
    if theme == themes[0]:
        print('Watch ' + anime[0])
    elif theme == themes[1]:
        print('Watch ' + anime[1])
    elif theme == themes[2]:
        print('Watch ' + anime[2])
    elif theme == themes[3]:
        print('Watch ' + anime[3])
    else:
        print('no')
        break
