import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
from dotenv import load_dotenv
import os


load_dotenv()
from db import users,conn
# mycursor = mydb.cursor()

intents=discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(member)
    channel = discord.utils.get(member.guild.text_channels, name="general")
    await channel.send(f"{member} has arrived!")
    

#just !test to see if everything wors fine
@client.command()
async def test(ctx,*args):
    print("works")
    await ctx.send("works")

# create and give role to user on !role rolename
@client.command()
async def role(ctx,*args):
    if(len(args)>0):
        member=ctx.author
        role = get(ctx.guild.roles,name=args[0])
        if(role==None):
            role=await ctx.guild.create_role(name=args[0])
        print(member,role)
        await member.add_roles(role)

# add name to db on !register 
@client.command()
async def register(ctx,*args):
    if(len(args)>0):
        name = args[0]
        print(name)
        sel=users.select().filter_by(name=name)
        data=conn.execute(sel).fetchall()
        print(data)
        # print()
        if(len(data)>0):
            await ctx.send("Name already registered")
        else:
            ins=users.insert().values(name=name)
            conn.execute(ins)
            await ctx.send("Registered Successfully")


# list all names in !names
@client.command()
@commands.has_role('nikhil')
async def names(ctx):  
    draft=""
    sel=users.select()
    data=conn.execute(sel).fetchall()
    print(data)
    for i in range(len(data)):
        draft+=data[i][1]+"\n"
    await ctx.send(draft)
       

# to report emoji reaction
@client.event
async def on_raw_reaction_add(reaction):
    channel=client.get_channel(reaction.channel_id)
    message=await channel.fetch_message(reaction.message_id)
    if(reaction.emoji.id==None):
        emoji=reaction.emoji.name
    else:
        emoji=f"<:{reaction.emoji.name}:{reaction.emoji.id}>"
    await channel.send(f"{reaction.member.name} reacted with {emoji} to {message.author.name}'s message")


client.run(os.getenv('discord'))

