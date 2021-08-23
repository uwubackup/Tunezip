import discord
from discord.ext import commands
import platform

import src.json

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["setprefix"])
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx, *, pre='+'):
        data = src.json.read_json('prefixes')
        data[str(ctx.message.guild.id)] = pre
        src.json.write_json(data, 'prefixes')
        await ctx.send(f"The guild prefix has been set to `{pre}` . Use `{pre}setprefix <prefix>` to change it again!")


def setup(bot):
    bot.add_cog(Prefix(bot))