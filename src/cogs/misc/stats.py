import discord
from discord.activity import Spotify
from discord.ext import commands 
import platform
import json
import aiohttp
import datetime
import humanize
from discord.ext.commands.core import command
import datetime, time


class misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        global startTime
        startTime = time.time

    @commands.command()
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))

        embed = discord.Embed(title = f"{self.bot.user.name}'s stats", description = '\uFEFF', colour = ctx.author.colour, timestamp = ctx.message.created_at)
        embed.add_field(name = "Bot Version: ", value = "0.0.1", inline=False)
        embed.add_field(name = "Python Version ", value=pythonVersion)
        embed.add_field(name = "Discord.py Version: ", value=dpyVersion)
        embed.add_field(name = "Total guilds: ", value=serverCount)
        embed.add_field(name = "Total Members: ", value=memberCount)
        embed.add_field(name = "Uptime ", value=uptime)
        embed.add_field(name = "Bot Developers ", value="<@467631169358528513>")
        await ctx.send(embed = embed)

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(
            name="Ping",
            value=f":ping_pong:{round(self.bot.latency * 1000)}ms",
            inline=True,
        )
        embed.set_footer(text=f"Pong request by {ctx.message.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["sinfo", "ginfo", "guildinfo"])
    async def serverinfo(self, ctx: commands.Context, guild: discord.Guild = None):
        if guild is None:
            guild = ctx.guild

        weird_stuff = {
            "ANIMATED_ICON": ("Animated Icon"),
            "BANNER": ("Banner Image"),
            "COMMERCE": ("Commerce"),
            "COMMUNITY": ("Community"),
            "DISCOVERABLE": ("Server Discovery"),
            "FEATURABLE": ("Featurable"),
            "INVITE_SPLASH": ("Splash Invite"),
            "MEMBER_LIST_DISABLED": ("Member list disabled"),
            "MEMBER_VERIFICATION_GATE_ENABLED": ("Membership Screening enabled"),
            "MORE_EMOJI": ("More Emojis"),
            "NEWS": ("News Channels"),
            "PARTNERED": ("Partnered"),
            "PREVIEW_ENABLED": ("Preview enabled"),
            "PUBLIC_DISABLED": ("Public disabled"),
            "VANITY_URL": ("Vanity URL"),
            "VERIFIED": ("Verified"),
            "VIP_REGIONS": ("VIP Voice Servers"),
            "WELCOME_SCREEN_ENABLED": ("Welcome Screen enabled"),
        }
        guild_features = [
            f"✅ {name}\n"
            for weird_stuff, name in weird_stuff.items()
            if weird_stuff in guild.features
        ]
        embed = discord.Embed(title=guild.name)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(
            name="Owner", value=f"Name: **{guild.owner}**\nID: **{guild.owner_id}**", inline=True
        )
        embed.add_field(name="Server ID", value=f"**{guild.id}**", inline=True)
        embed.add_field(name="Creation Time", value=guild.created_at.strftime("%c"), inline=False)
        embed.add_field(name="Region", value=str(guild.region).upper(), inline=True)
        embed.add_field(name="Member Count", value=f"**{guild.member_count}**", inline=True)
        embed.add_field(name="Role Count", value="**{}**".format(len(guild.roles)), inline=False)
        embed.add_field(
            name="Channel Count",
            value=f"Categories: **{len(guild.categories)}**\nText: **{len(guild.text_channels)}**\nVoice: **{len(guild.voice_channels)}**\nTotal: **{len(guild.text_channels) + len(guild.voice_channels)}**",
            inline=True,
        )
        embed.add_field(name="Emoji Count", value="**{}**".format(len(guild.emojis)), inline=True)
        if guild_features:
            embed.add_field(name="Features", value="".join(guild_features), inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['av'])
    async def user(self, ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author
            embed = discord.Embed(description=f'[URL]({member.avatar_url})', color=member.color)
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(description=f'[URL]({member.avatar_url})', color=member.color)
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(alises = ['sav'])
    async def server(self, ctx):
        embed = discord.Embed(
            description=f'[URL]({ctx.guild.icon_url})',
            color=ctx.author.color
        )
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["uinfo", "memberinfo", "minfo"])
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userinfo(self, ctx: commands.context, user: discord.Member = None):
        if user is None:
            user = ctx.author

        user_flags = "\n".join(i.replace("_", " ").title() for i, v in user.public_flags if v)
        roles = user.roles[-1:0:-1]
        embed = discord.Embed(color=user.color or self.bot.ok_color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Name", value=user)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(
            name="Account Creation",
            value=user.created_at.strftime("%c"),
        )
        embed.add_field(
            name=f"{ctx.guild} Join Date", value=user.joined_at.strftime("%c"), inline=False
        )
        if roles:
            embed.add_field(
                name=f"Roles **{(len(user.roles) - 1)}**",
                value=", ".join([x.mention for x in roles[:10]]),
                inline=False,
            )
        if user_flags:
            embed.add_field(name="Public User Flags", value=user_flags.upper(), inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["rinfo"])
    async def roleinfo(self, ctx: commands.Context, *, role: discord.Role):
        await ctx.send(
            embed=discord.Embed(title=f"Role info for {role.name}", color=role.color)
            .add_field(name="ID", value=role.id, inline=True)
            .add_field(name="Color", value=role.color, inline=True)
            .add_field(name="Creation Time", value=role.created_at.strftime("%c"), inline=True)
            .add_field(name="Members", value=len(role.members), inline=True)
            .add_field(name="Hoisted", value=role.hoist, inline=True)
            .add_field(name="Mentionable", value=role.mentionable, inline=True)
            .add_field(name="Position", value=role.position, inline=True)
            .add_field(
                name="Permissions",
                value=f"Click [Here](https://cogs.fixator10.ru/permissions-calculator/?v={role.permissions.value})",
                inline=True,
            )
        )

    @commands.command(aliases=["einfo", "emoteinfo"])
    async def emojiinfo(self, ctx: commands.Context, emoji: discord.Emoji):
        await ctx.send(
            embed=discord.Embed(title="Emoji Information")
            .add_field(name="ID", value=emoji.id, inline=False)
            .add_field(name="Animated", value=emoji.animated, inline=False)
            .add_field(name="Link", value=emoji.url, inline=False)
            .set_image(url=emoji.url)
        )

def setup(bot):
    bot.add_cog(misc(bot))