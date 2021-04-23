import discord
import random
from spellchecker import SpellChecker

client = discord.Client()
spell = SpellChecker()

BOT_TOKEN = ''   # initialize Token value here

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    print(message)  # log all message information
    
    if message.author == client.user:
        return  # so that the bot doesn't respond to itself

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello there {message.author.name}!')

    if 'roll' in message.content:   # rolling a die example
    	num = random.randint(1,6)
    	emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
    	await message.add_reaction(emojis[num-1])

    if message.content.startswith('$spellcheck '):  # spellcheck message string
    	words = message.content.split(' ')
    	misspelled = spell.unknown(words[1:])   # ignore the invocation command
    	stri = ""
    	flag = False
    	for word in words[1:]:
    		if word in misspelled:
    			word = spell.correction(word)
    			flag = True
    		stri += word
    		stri += " "

    	if flag == False:
    		await message.add_reaction('✅')
    	else:
    		await message.add_reaction('❌')
    		await message.channel.send('Correction : ' + stri.strip())

    
client.run(BOT_TOKEN)
