#import discord package
import discord
from discord import embeds
from discord.colour import Color
from discord.ext import commands

#client
client=commands.Bot(command_prefix='--')

@client.command(name='info')
async def info(context):


    myEmbed = discord.Embed(title="Administrator",description="Nimash Eshan \nJohnny JTH",color=0x00ff00)
    myEmbed.add_field(name="Partner",value="Githmi Paranahewa",inline=False)
    myEmbed.add_field(name="Co leaders",value="Waruna Usgoda \nVasula \nnA PEACE \nRukshan \nmisha",inline=False)
    myEmbed.add_field(name="Vip Members",value="Trey(ナ尺ツ) \nUmal Manjitha(bota malli) \nSisitha Liyanage(Fraddy Gaming) \nBunny",inline=False)
    myEmbed.add_field(name="Guest",value="Anuja Dampriya \nsenu gaming",inline=False)
    myEmbed.add_field(name="Version code:",value="v1.0.0",inline=False)
    myEmbed.add_field(name="Date released",value="March 21,2019",inline=False)
    myEmbed.set_image(url='https://cdn.discordapp.com/attachments/753250413058457712/823718466552332328/Screenshot_20210323-060920_1_1.png')
    myEmbed.set_footer(text="Thank you.Have a nice day")
    myEmbed.set_author(name="Rise Of Kingdom Srilankan Official Discord Server")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    #do stuff.....
    general_chanel = client.get_channel(753250363016216627)
    await general_chanel.send('HELLO WORLD')

@client.event
async def on_disconnect():

    general_chanel = client.get_channel(753250363016216627)
    await general_chanel.send('good bye kattiya')

@client.event
async def on_message(message):

    if message.content == 'what is this':
        general_chanel = client.get_channel(753250363016216627)

        myEmbed = discord.Embed(title="Administrator",description="Nimash Eshan \nJohnny JTH",color=0x00ff00)
        myEmbed.add_field(name="Partner",value="Githmi Paranahewa",inline=False)
        myEmbed.add_field(name="Co leaders",value="Waruna Usgoda \nVasula \nnA PEACE \nRukshan \nmisha",inline=False)
        myEmbed.add_field(name="Vip Members",value="Trey(ナ尺ツ) \nUmal Manjitha(bota malli) \nSisitha Liyanage(Fraddy Gaming \nBunny)",inline=False)
        myEmbed.add_field(name="Guest",value="Anuja Dampriya \nsenu gaming",inline=False)
        myEmbed.add_field(name="Version code:",value="v1.0.0",inline=False)
        myEmbed.add_field(name="Date released",value="March 21,2019",inline=False)
        myEmbed.set_footer(text="Thank you.Have a nice day")
        myEmbed.set_author(name="Rise Of Kingdom Srilankan Official Discord Server")

        await general_chanel.send(embed=myEmbed)
    await client.process_commands(message)

#run the client on the server
client.run('ODIyOTY2OTcwMDY3ODQ1MTIw.YFZ9tw.v1JL2A9FanhTBNaskDFntmE06BU')

