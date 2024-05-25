# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# »› Developed by Foxx
# »› Copyright © 2024 Aurel Hoxha. All rights reserved.
# »› GitHub: https://github.com/TeamFoxx
# »› For support and inquiries, please contact info@aurelhoxha.de
# »› Use of this program is subject to the terms of the MIT licence.
# »› A copy of the license can be found in the "LICENSE" file in the root directory of this project.
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#
# ⏤ { imports } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤
import os
from datetime import datetime

import discord
import psutil
import requests
from discord.ext import commands

import config
from main import start_time
from utils.utils import attachments, header, no_permission


# ⏤ { configurations } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

class Metrics(commands.Cog):
    def __init__(self, reelab):
        self.bot: commands.Bot = reelab

    # ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to display bot's metrics
    @commands.Cog.slash_command(
        name="metrics",
        description="Displays various metrics and statistics about the bot's performance and usage.",
        default_required_permissions=discord.Permissions(administrator=True)
    )
    async def show_metrics(self, ctx):
        # Check if the user has permission to reload cogs
        if ctx.author.id in config.developer or ctx.author.id in config.staff:

            # Check Server - Bot latency
            latency = round(self.bot.latency * 1000)

            # Get CPU usage using psutil
            cpu_percent = psutil.cpu_percent()

            # Get bot's specific resource usage
            bot_process = psutil.Process(os.getpid())
            bot_memory = bot_process.memory_info().rss
            bot_memory_mb = bot_memory / (1024 ** 2)

            # Calculate uptime
            now = datetime.now()
            uptime = now - start_time

            # Format uptime as days, hours, minutes, and seconds
            days = uptime.days
            hours, remainder = divmod(uptime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            uptime_str = ""
            if days:
                uptime_str += f"{days} day{'s' if days > 1 else ''}, "
            if hours:
                uptime_str += f"{hours} hour{'s' if hours > 1 else ''}, "
            if minutes:
                uptime_str += f"{minutes} minute{'s' if minutes > 1 else ''}, "
            uptime_str += f"{seconds} second{'s' if seconds != 1 else ''}"

            # Gather server and user information
            if config.public:
                total_servers = len(self.bot.guilds)
                total_users = sum(guild.member_count for guild in self.bot.guilds)
                server_info = f"{total_servers} Servers"
            else:
                total_users = ctx.guild.member_count
                server_info = ""

            # Get server location
            response = requests.get('https://ipinfo.io/json')
            location_data = response.json()
            city = location_data.get('city', 'Unknown City')
            region = location_data.get('region', 'Unknown Region')
            country = location_data.get('country', 'Unknown Country')
            server_location = f"{city}, {region}, {country}"

            # Create an embed for metrics
            metrics_embed = discord.Embed(
                title="Bot Metrics",
                color=config.EMBED_COLOR
            )
            metrics_embed.add_field(name="⏳ Uptime", value=f"```fix\n{uptime_str}\n```", inline=False)
            metrics_embed.add_field(name="💾 Memory Usage", value=f"```fix\n{bot_memory_mb:.2f}MB\n```", inline=True)
            metrics_embed.add_field(name="💻 CPU Usage", value=f"```fix\n{cpu_percent:.2f}%\n```", inline=True)
            metrics_embed.add_field(name="🏓 Latency", value=f"```fix\n{latency}ms\n```", inline=True)
            metrics_embed.add_field(name="🌍 Server Location", value=f"```fix\n{server_location}\n```", inline=True)
            if config.public:
                metrics_embed.add_field(name="🌐 Running on", value=f"```fix\n{server_info}\n```", inline=True)
            metrics_embed.add_field(name="👥 Bot Users", value=f"```fix\n{total_users} Users\n```", inline=True)

            metrics_embed.set_footer(text="Bot Metrics • Powered by Reelab Studios")
            metrics_embed.set_image(url="attachment://reelab_footer.png")

            # Send header message
            embed_header = await header()

            # Attachments
            banner_file, logo_file, footer_file = await attachments()

            # Sending the metrics embed as a response
            await ctx.respond(embeds=[embed_header, metrics_embed],
                              files=[banner_file, logo_file, footer_file],
                              hidden=True)
        else:
            # Send header message
            embed_header = await header()

            # Create an embed for permission denial
            no_permission_embed = await no_permission()

            # Attachments
            banner_file, logo_file, footer_file = await attachments()

            # Sending the permission denial embed as a response
            await ctx.respond(embeds=[embed_header, no_permission_embed],
                              files=[banner_file, logo_file, footer_file],
                              hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(Metrics(bot))
