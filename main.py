import discord
from discord.ext import commands

client = commands.Bot(command_prefix="@")
@client.event
async def on_ready():
  print("online")


client.remove_command("help")

@client.command()
async def help(ctx):
 await ctx.channel.send("pomoc")



#TO ZAWSZE NA KOŃCU
client.run("OTEzNDYxMjE0MDI0MTk2MTQ2.YZ-1DA.EWSBNZ-Fdxks61_TjIEl3n1hQYs")
