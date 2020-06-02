import discord

def read_token():
    with open("token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_message(msg):
    if msg.content.lower().find("alex") !=-1:
       return await msg.channel.send("Sup FOO!")
    if msg.content.lower().find("sex") !=-1:
       return await msg.channel.send("Go jerk off you horny fuck!")
    if msg.content.lower().find("butters") !=-1:
       return await msg.channel.send("thats a cyoot fuckin kittyyyy!")
    if msg.content.lower().find("araz") !=-1:
       return await msg.channel.send("kid can't play that good!")
    if msg.content.lower().find("dub") !=-1:
       return await msg.channel.send("ya'll ain't gon win shiiiii!")

client.run(token)