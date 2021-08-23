import discord
from typing import Optional
from discord.ext import commands
from discord.ext.commands.core import command


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["logout"])
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):

        await ctx.send("Logging out now\N{HORIZONTAL ELLIPSIS}")
        await ctx.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *, msg):
        """Say something with the bot."""
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.bot.get_command(command)

        if command is None:
            await ctx.send("I cant find a command with that name")

        elif ctx.command == commands:
            await ctx.send("You cannot disable this command")

        else:
            
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"I have {ternary} {command}")
def setup(bot):
    bot.add_cog(Owner(bot))