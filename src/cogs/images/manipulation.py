import discord
from discord.ext import commands
import asyncio
import aiohttp
import datetime
import io
class manipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def horny(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as session:
         async with session.get(
            f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png")}'
        ) as af:
            if 300 > af.status >= 200:
                fp = io.BytesIO(await af.read())
                file = discord.File(fp, "horny.png")
                em = discord.Embed(
                    title="bonk",
                    color=ctx.author.color,
                )
                em.set_image(url="attachment://horny.png")
                await ctx.send(embed=em, file=file)
            else:
                await ctx.send('No horny :(')
            await session.close()

    @commands.command()
    async def trigger(self,ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
            
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                
                await trigSession.close() # closing the session and;
                
                await ctx.reply(file=discord.File(imageData, 'triggered.gif')) 

    @commands.command()
    async def gay(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author 
            
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                
                await trigSession.close() # closing the session and;

                await ctx.reply(file=discord.File(imageData, 'gay.gif'))

    @commands.command()
    async def glass(self, ctx, member: discord.Member=None):
        if not member: 
            member = ctx.author
            
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f'https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                
                await trigSession.close() # closing the session and;

                await ctx.reply(file=discord.File(imageData, 'glass.png'))

    @commands.command()
    async def wasted(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author 
            
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
                
                await trigSession.close() # closing the session and;

                await ctx.reply(file=discord.File(imageData, 'wasted.png'))


    
                

def setup(bot):
    bot.add_cog(manipulation(bot))
