import random, string
from colorama import init, Fore

init(convert=True)

print('%sKoavuGen : How much do u wanna generate:%s ' % (Fore.CYAN, Fore.WHITE), end='')
amount = int(input())
for i in range(amount):
    code = "https://discordapp.com/gifts/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
    print('Code: %s' % (code))
    with open('nitros.txt', 'a') as f:
        f.write('%s\n' % (code))