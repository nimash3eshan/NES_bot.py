#import discord package
import discord
from discord import embeds
from discord.colour import Color
from discord.ext import commands

#client
client=commands.Bot(command_prefix='--')

@client.command(name='info')
async def info(context):


    myEmbed = discord.Embed(title="Administrator",description="Nimash Eshan \nJohnny JTH \n࿐༒ҜƗŇǤ STRÎKÊR༒࿐ ",color=0x00ff00)
    myEmbed.add_field(name="Co leaders",value="BUNNY💓 \nWaruna Usgoda \nVasula \nnA PEACE \nmisha",inline=False)
    myEmbed.add_field(name="Vip Members",value="Trey(ナ尺ツ) \nUmal Manjitha(bota malli) \nSisitha Liyanage(Fraddy Gaming) \nBunny",inline=False)
    myEmbed.add_field(name="University Of Moratuwa",value="Eshan \nUmal Manjitha \nGithmi Paranahewa \nVidith \nDilshan \nshehan \nPubudu \nhasathcharu \nHntr-Kllr \nThejan_B_W \nVidath Chamikara",inline=False)
    myEmbed.add_field(name="Game Partners",value="Anuja Dampriya \nsenu gaming \nMikeHunt666 \n[SA81] ERA",inline=False)
    myEmbed.add_field(name="Version code:",value="v2.0.0",inline=False)
    myEmbed.add_field(name="Date released",value="March 21,2019",inline=False)
    myEmbed.set_image(url='https://cdn.discordapp.com/attachments/673595467581358085/838903903868813362/giphy.gif')
    myEmbed.set_footer(text="Thank you.Have a nice day")
    myEmbed.set_author(name="Rise Of Kingdom Srilankan Official Discord Server")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    activity = discord.Game(name="Rise Of Kingdom Srilanka  |--info|", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    #do stuff.....
    general_chanel = client.get_channel(753250363016216627)
    await general_chanel.send('HELLO WORLD')

@client.event
async def on_disconnect():

    general_chanel = client.get_channel(753250363016216627)
    await general_chanel.send('good bye kattiya')
   



#run the client on the server
client.run('ODIyOTY2OTcwMDY3ODQ1MTIw.YFZ9tw.v1JL2A9FanhTBNaskDFntmE06BU')

