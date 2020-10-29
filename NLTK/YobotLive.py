import discord
import DB
import random
import asyncio
import locale
import diag_list

TOKEN = ''
client = discord.Client()

disc_wc_dm = """In the year 3050 mankind is enslaved by an AI dominated infrastructure. Human beings now function for their perspective function in machine learning experiments. In order to fight for originality, Yobot has been sent to a time before the implementation of AI by big corporations. Yobored, an advanced perception transmitter, has been installed into Yobot's mainframe. The year is now 2019 AD.

Your mission is to help Yobot gain as much experience as possible through Yobored.

Download the Yobored app and share stories with other people for the better of cultural appreciation.

https://apps.apple.com/us/app/yobored/id1332828485
https://play.google.com/store/apps/details?id=com.yobored&hl=en_US"""


lp = 1
bot_c_id = client.get_channel(628546417903796234) #628546417903796234 Yobot id


@client.event
async def on_member_join(member):
    print("User {} joined this server.".format(member.name))
    await member.send(disc_wc_dm)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('/yo') or message.content.startswith('/Yo') or message.content.startswith('/YO'):
        print("You are in first if")
        print(message.channel)
        if str(message.channel) == "public" or str(message.channel) == "special-ops" :
            print("You are in second if")
            msg_string = str(message.content).lower()
            topic = msg_string.split("/yo ")[1]
            print(topic)
            shareURL = DB.get_feed(topic)

            if shareURL != "NO":
                await message.channel.send(shareURL)
            else:
                await message.channel.send("Can someone please upload something about \""+topic+"\", I can't find anything!")
            global lp
            print(lp)
            if lp ==1 and str(message.channel)=="public":
                client.loop.create_task(background_loop(message.channel))
                lp = lp+1

    elif "Direct Message with" not in str(message.channel):
        s1 = message.content
        s2 = s1[-1]
        sx = ['?','.','\'','"',"\\","/",",",";","#","@","(",")"]
        while s2 in sx:
            print("while")
            s1 = s1[:-1]
            s2 = s1[-1]

        L1 = s1.split()
        print(L1)
        c = len(L1)
        L2 = []
        for i in range(c):
            for j in range(c-i):
                text = ''
                for k in range(j,i+j+1):
                    text = text+L1[k]+" "
                L2.append(text.strip())
        print("this List {}".format(L2))

        for word in L2:
            if word != 'Yobored' and word != 'yobored' and word != 'YOBORED' and word != 'YoBored' and word != 'yoBored':
                shareURL1 = DB.get_feed_lochash(word)
                print(shareURL1)

                if shareURL1 != "NO":
                    await message.channel.send(shareURL1)
                    break

    if message.content.startswith('/say') and ("Direct Message with" in str(message.channel)) and str(message.author) in ['chetan.yobored#5915', 'Steve_Dobbs#1736', 'Canidox#8426', 'Steve_Dobbs#1259']:
        g_text = str(message.content).split("/say")[1]
        channel = client.get_channel(595766044442886147) #change channel id of live public group
        await channel.send(g_text)

async def background_loop(channel):
    await client.wait_until_ready()
    #print(client.is_closed)
    locale.setlocale(locale.LC_ALL,'en_US')
    while 1:
        print(channel)
        tot_xp1 = DB.get_world_xp()
        tot_xp = f'{tot_xp1:n}'
        message = diag_list.dig_l()
        message1 = message+" XP {}".format(tot_xp)
        print(message1)
        await channel.send(message1)
        await(asyncio.sleep(10800))


@client.event
async def on_ready():
    print('logged in as '+client.user.name+' and user id is '+str(client.user.id))
    print("-------------------")

client.run(TOKEN)