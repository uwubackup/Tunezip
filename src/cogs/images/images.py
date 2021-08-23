import discord
import aiohttp
import io
from io import BytesIO
from discord.ext import commands


class Facts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True, aliases = ["img"])
    async def image(self, ctx):
        await ctx.send("Please use a sub command")

    @image.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/dog') as r:
                await ctx.send((await r.json())['link'])

    @image.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/cat') as r:
                await ctx.send((await r.json())['link'])

    @image.command()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/panda') as r:
                await ctx.send((await r.json())['link'])

    @image.command(aliases = ['birb'])
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/birb') as r:
                await ctx.send((await r.json())['link'])

    @image.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/fox') as r:
                await ctx.send((await r.json())['link'])

    @image.command()
    async def koala(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/koala') as r:
                await ctx.send((await r.json())['link'])



def setup(bot):
    bot.add_cog(Facts(bot))