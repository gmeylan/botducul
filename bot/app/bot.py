import os

import arrow
import discord
import random

token = os.getenv("DISCORD_TOKEN")

client = discord.Client()


async def seoul_swiss_time(message):
    utc = arrow.utcnow()

    swiss_time = utc.to("Europe/Zurich")
    seoul_time = utc.to("Asia/Seoul")
    swiss_formatted_time = swiss_time.format("HH:mm:ss")
    korean_formatted_time = seoul_time.format("HH:mm:ss")
    response = (
        "Il est "
        + swiss_formatted_time
        + " en Suisse\nEt "
        + korean_formatted_time
        + " en Corée (pas du nord) !"
    )
    await message.channel.send(response)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for mention in message.mentions:
        if str(mention) == "gasegg#7082":
            await seoul_swiss_time(message)
        if str(mention) == "botducul#3369":
            await message.channel.send("Je suis ton maître !")

    if message.content == "/time":
        await seoul_swiss_time(message)

    if message.content == "/help":
        await message.channel.send("Ne sois pas un retard")

    if message.content.startswith("/rand"):
        rand_array = [1, 100]
        message_content = message.content
        args = message_content.split(" ")
        if len(args) > 1:
            rand_array = args[1].split('-')
        try:
            result = random.randint(int(rand_array[0]), int(rand_array[1]))
        except ValueError:
            await message.channel.send("Arrête de faire le retard et utilise moi correctement")
            return
        await message.channel.send(result)

client.run(token)
