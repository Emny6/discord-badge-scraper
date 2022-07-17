import discum, time, colorama, os
from colorama import Fore
from sty import fg
reset = colorama.Fore.RESET

os.system("cls")

text1 = f'''

          $$\      $$\  $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ 
          $$$\    $$$ |$$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ \____$$  |
          $$$$\  $$$$ |$$ /  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|    $$  / 
          $$\$$\$$ $$ |$$ |  $$ |$$ |  $$ |$$ $$\$$ |\$$$$$$\     $$  /  
          $$ \$$$  $$ |$$ |  $$ |$$ |  $$ |$$ \$$$$ | \____$$\   $$  /   
          $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$\   $$ | $$  /    
          $$ | \_/ $$ | $$$$$$  | $$$$$$  |$$ | \$$ |\$$$$$$  |$$$$$$$$\ 
          \__|     \__| \______/  \______/ \__|  \__| \______/ \________|
                                                                 
                                                                 
                                                                 
                                                                 
                            [+] DISCORD BADGE SCRAPPER [+]
'''

text = text1.replace('$', f'{fg(240, 179, 255)}$').replace('\\', reset+'\\').replace('|', reset+'|').replace('/', reset+'/').replace('>', reset+'>')+reset

print(text)
token = input(f"{Fore.LIGHTGREEN_EX}    [+] Account Token: ")
guild_id = input("\n    [+] Server ID: ")
channel_id = input("\n    [+] Channel ID: ")
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(f'\n\n{Fore.LIGHTCYAN_EX}[-] Successfully scraped '+str(lenmembersfetched)+' users! (Press Enter to Close)')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

print(f'\n\n{Fore.LIGHTMAGENTA_EX}[-] Scraping users, wait...')
bot.gateway.run()

def __get_badges(flags) -> list[str]:
    
        BADGES = {
           #  1 << 0:  'Discord Employee',
            1 << 1:  'Partnered Server Owner',
            1 << 2:  'HypeSquad Events',
             1 << 3:  'Bug Hunter Level 1',
            1 << 9:  'Early Supporter',
             1 << 10: 'Team User',
           #  1 << 12: 'System',
             1 << 14: 'Bug Hunter Level 2',
            # 1 << 16: 'Verified Bot',
            1 << 17: 'Early Verified Bot Developer'
        }

        zeeckt = []

        for badge_flag, badge_name in BADGES.items():
            if flags & badge_flag == badge_flag:
                zeeckt.append(badge_name)

        return zeeckt


with open('ids.txt', 'a+', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        zeecktid = str(memberID)
        zeeckttemp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        zeecktuser = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        zeecktdisc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{zeecktuser}#{zeecktdisc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(zeecktid) >> 22) + 1420070400000) / 1000)))
        if zeeckttemp != None:
            z = __get_badges(zeeckttemp)
            if len(z) != 0:
                zeeckt = ', '.join(z)
                file.write(f'{zeecktid}\n')