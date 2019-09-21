import discord
import arrow

token = "NjIzOTU5MDI5NTU0NjEwMTg4.XYKEVQ.5J80GoNUjpIUzb7iQwE-cXrbY3w"

client = discord.Client()

async def seoul_swiss_time(message):
        utc = arrow.utcnow()

        swiss_time = utc.to('Europe/Zurich')
        seoul_time = utc.to('Asia/Seoul')
        swiss_formatted_time = swiss_time.format('HH:mm:ss')
        korean_formatted_time = seoul_time.format('HH:mm:ss')
        response = 'Il est ' + swiss_formatted_time + ' en Suisse\nEt ' + korean_formatted_time + ' en Corée (pas du nord) !'
        await message.channel.send(response)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for mention in message.mentions:
        if str(mention) == 'gasegg#7082':
            await seoul_swiss_time(message)
        if str(mention) == 'botducul#3369':
            await message.channel.send("Je suis ton maître !")

    if message.content == '/time':
        await seoul_swiss_time(message)
    
client.run(token)
