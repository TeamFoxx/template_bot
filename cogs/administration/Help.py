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
import discord
from discord import Button, ButtonStyle
from discord.ext import commands

import config
from utils.utils import attachments, check_permissions


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤
def has_permissions():
    async def predicate(ctx):
        if await check_permissions(ctx):
            return True
        else:
            return False
    return commands.check(predicate)


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to display help information for all commands
    @commands.Cog.slash_command(
        name="help",
        description="Displays information about all commands."
    )
    async def help(self, ctx):
        # Check for missing permissions before executing the command
        # If the bot is missing required permissions, send a warning message and return
        if not await check_permissions(ctx):
            return

        # Create an embed for help information
        embed = discord.Embed(
            description="Here is a list of all available commands and their descriptions:\n"
                        "⏤",
            color=config.EMBED_COLOR
        )

        # Loop through all commands and add them to the embed
        for command in self.bot.application_commands:
            # Check if the command requires admin permissions
            if not command.default_member_permissions or ctx.author.guild_permissions.administrator:
                embed.add_field(
                    name=f"🔹/{command.name}",
                    value=f"- {command.description}" or "- No description provided.",
                    inline=False
                )

        embed.set_footer(
            text="Thank you for using our bot! 🤖 — Interested in having your own? Visit us at discord.gg/reelab")
        embed.set_author(name="Information & Help",
                         url="https://reelab.studio/",
                         icon_url='attachment://reelab_logo.png')

        # Setting an image for the embed
        embed.set_image(url="attachment://reelab_banner.gif")

        # Attachments for the embed
        banner_file, logo_file, _, _, _ = await attachments()

        buttons = [
            Button(
                style=ButtonStyle.url,
                emoji="🛡️",
                label="Privacy Policy",
                url=config.privacy_url
            )
        ]

        # Sending the help embed as a response
        await ctx.respond(embeds=[embed],
                          files=[banner_file, logo_file],
                          components=[buttons],
                          hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(Help(bot))
