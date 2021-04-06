from os import getenv
from discord import Client, Game, Status
from dotenv import load_dotenv
from random import choice
from gitvalidate import validate


load_dotenv()
BOT_TOKEN = getenv('KEY')

key = 'DB-Cnc-1'

client = Client()

words = open('rando_mwords.txt', 'r').read().split('\n')


@client.event
async def on_ready():
    if validate(key) is False:
        raise AttributeError('Invalid Key')
    game = Game('SPAM')
    await client.change_presence(status=Status.idle, activity=game)

async def update():
    await client.wait_until_ready()
    num = int(input('Spam Number\n>>> '))
    for i in range(num):
        for guild in client.guilds:
            for i in guild.channels:
                channel = client.get_channel(i.id)
                if str(channel.type) == 'text':
                    await channel.send(f'{choice(words)}')
    exit()


client.loop.create_task(update())
client.run(BOT_TOKEN)
