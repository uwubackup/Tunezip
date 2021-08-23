import discord
from discord import colour
from discord import embeds
from discord.asset import VALID_AVATAR_FORMATS
from discord.ext import commands 
import platform
import DiscordUtils

from discord.ext.commands.core import command
from discord.mixins import EqualityComparable

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True, aliases = ['hlp'])
    async def help(self, ctx):
        embed = discord.Embed(title= "**Help commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name= "**Moderation**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Misc**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Fun**", value= "\uFEFF", inline= False)
        embed.add_field(name = "**Music**", value= "\uFEFF", inline= False)
        embed.add_field(name= "**Config**", value= "\uFEFF", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}. Also consider voting for me by typing <your prefix>vote :D")
        await ctx.send(embed = embed)

    @help.command(aliases = ["mod"])
    async def moderation(self, ctx):
        embed = discord.Embed(title= "**Moderation commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name=f"**Warn**", value= "Warns a member with the provided reason \uFEFF", inline= False)
        embed.add_field(name=f"**Warns**", value= "Gives warnings received by the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Removewarn**", value= "Removes specified warn for the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Kick**", value="Kicks the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Ban**", value="Bans the mentioned member \uFEFF", inline= False)
        embed.add_field(name=f"**Unban**", value="Unban a user using their ID \uFEFF", inline= False)
        embed.add_field(name=f"**Clear**", value="Purge mentioned amount of messages \uFEFF", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command()
    async def music(self, ctx):
        embed= discord.Embed(title = "**Music commands!**", description = "\uFEFF", colour = ctx.author.colour)
        embed.add_field(name = f"**Play**", value = "Play's the specified song in vc")
        embed.add_field(name = "**Disconnect**", value = "Disconnect the bot from the vc")
        embed.add_field(name = "**Playing/np**", value = "Get details about the song playing currently")
        embed.add_field(name = "**Pause**", value= "Pause the song")
        embed.add_field(name = "**Stop**", value= "Stop the playback in vc")
        embed.add_field(name = "**Next**", value= "Play the next song in queue")
        embed.add_field(name = "**Previous**", value= "Play the previous song in queue")
        embed.add_field(name  = "**Shuffle**", value = "Shuffle the queue")
        embed.add_field(name = "**Repeat**", value = "Set the queue mode to repeat")
        embed.add_field(name = "**Queue**", value= "View the queue")
        embed.add_field(name = "**Volume**", value= "Set the music volume ranging from 0% to 150%")
        embed.add_field(name = "**Lyrics**", value= "Get lyrics for the specified song")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command(aliases = ["miscellaneous"])
    async def misc(self, ctx):
        embed = discord.Embed(title= "**Miscellaneous commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name = "**Stats**", value="Get stats about me", inline= False)
        embed.add_field(name = "**Ping**", value="Get bots ping", inline= False)
        embed.add_field(name = "**Serverinfo**", value="Get info about the guild", inline= False)
        embed.add_field(name = "**Userinfo**", value="Get info about the mentioned user", inline= False)
        embed.add_field(name = "**Roleinfo**", value="Get info about the specified role", inline= False)
        embed.add_field(name = "**User**", value="Get a user's avatar", inline= False)
        embed.add_field(name = "**Server**", value="Get the server's avatar", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command()
    async def fun(self, ctx):
        embed = discord.Embed(title= "**Fun commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name = "**Roleplay**", value="Show a list of roleplay commands!", inline= False)
        embed.add_field(name = "**Fact**", value="Show a list of fact commands!", inline= False)
        embed.add_field(name = "**Compliment**", value="Compliment someone", inline= False)
        embed.add_field(name = "**Quote**", value="Get a random anime quote", inline= False)
        embed.add_field(name = "**Image**", value="Get a random image, use `<your prefix>help image` for help ", inline= False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command()
    async def config(self, ctx):
        embed = discord.Embed(title= "**Fun commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name= "**Setprefix**", value= "Set a prefix for your guild")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command(aliases = ["rp"])
    async def roleplay(self, ctx):
        embed1 = discord.Embed(color=ctx.author.color).add_field(name=f"Pat - Pat a user\n\nHug - Hug a user\n\nCuddle - Cuddle with a user\n\nLick - Lick a user\n\nBully - Bully a user", value="Page 1")
        embed2 = discord.Embed(color=ctx.author.color).add_field(name=f"Poke - Poke a user\n\nSlap - Slap a user\n\nSmug - Give a smug look\n\nKiss - Kiss a user\n\nCry - Cry", value="Page 2")
        embed3 = discord.Embed(color=ctx.author.color).add_field(name=f"Bonk - Bonk a user\n\nYeet - Yeet a user\n\nHighfive - HighFive a user\n\nBlush - Blush uwu\n\nSmile - Smile", value="Page 3")
        embed4 = discord.Embed(color=ctx.author.color).add_field(name=f"Wave - Wave o/\n\nHappy - Be happy\n\nDance - Dance\n\nCringe - Cringe ig", value="Page 4")
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('🔐', "lock")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [embed1, embed2, embed3, embed4]
        await paginator.run(embeds)

    @help.command(aliases = ["facts"])
    async def fact(self, ctx):
        embed = discord.Embed(title= "**Fact commands!**", description="\uFEFF", colour = ctx.author.colour)
        embed.add_field(name= "**Catfact**", value= "Get a random cat fact")
        embed.add_field(name= "**Dogfact**", value= "Get a random dog fact")
        embed.add_field(name= "**Pandafact**", value= "Get a random panda fact")
        embed.add_field(name= "**Birdfact**", value= "Get a random bird fact")
        embed.add_field(name= "**Foxfact**", value= "Get a random fox fact")
        embed.add_field(name= "**Koalafact**", value= "Get a random koala fact")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    @help.command(aliases = ['img'])
    async def image(self, ctx):
        embed = discord.Embed(title= "**Image commands!**", description="Usage: `<yourprefix>image [the following categories]`", colour = ctx.author.colour)
        embed.add_field(name= "**Dog**", value= "Get a random dog image")
        embed.add_field(name= "**Cat**", value= "Get a random cat image")
        embed.add_field(name= "**Bird**", value= "Get a random birb image")
        embed.add_field(name= "**Panda**", value= "Get a random panda image")
        embed.add_field(name= "**Fox**", value= "Get a random fox image")
        embed.add_field(name= "**Koala**", value= "Get a random koala image")
        embed.add_field(name= "\uFEFF", value= "**Image Manipulation**\n usage: `<prefix>[category] [member mention]`")
        embed.add_field(name= "\uFEFF", value= "**Categories:**", inline = False)
        embed.add_field(name= "**Trigger**", value= "Trigger someone", inline = False)
        embed.add_field(name= "**Gay**", value= "A rainbow overlay to an image", inline = False)
        embed.add_field(name= "**Wasted**", value= "GTA wasted overlay", inline = False)
        embed.add_field(name= "**Glass**", value= "Overlays a glass texture over an image", inline = False)
        embed.add_field(name= "**Horny**", value= "Horny pass or not horny >:D")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)

    
    


def setup(bot):
    bot.add_cog(help(bot))