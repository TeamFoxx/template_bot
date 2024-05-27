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
import logging

import discord
from discord.ext import commands

import config
from utils.utils import attachments, check_permissions, check_licence


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

# Configure logging
logger = logging.getLogger(__name__)


def has_permissions():
    async def predicate(ctx):
        if await check_permissions(ctx):
            return True
        else:
            logger.warning(f"Missing permissions for command: {ctx.command} invoked by user: {ctx.author}")
            return False
    return commands.check(predicate)


def has_valid_license_and_permissions():
    async def predicate(ctx):
        # Check license first
        if not await check_licence(ctx):
            logger.warning(f"License expired for command: {ctx.command} invoked by user: {ctx.author}")
            return False
        # Check permissions if license is valid
        if not await check_permissions(ctx):
            return False
        return True
    return commands.check(predicate)


class Credits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Command to send a live announcement
    @commands.Cog.slash_command(
        name="credits",
        description="Displays the developer credits and branding of Reelab Studios."
    )
    async def credits(self, ctx):
        # Check for license expiry before executing the command
        # If the license has expired, send a warning message and return
        if not await check_licence(ctx):
            return

        # Check for missing permissions before executing the command
        # If the bot is missing required permissions, send a warning message and return
        if not await check_permissions(ctx):
            return

        logger.info(f"Credits command invoked by user: {ctx.author}")

        # Creating an embed message
        embed = discord.Embed(
            description="This bot was developed by [Aurel Hoxha](https://github.com/TeamFoxx) and is part of Reelab Studios.\n"
                        "⏤",
            color=config.EMBED_COLOR
        )
        embed.add_field(
            name="👨‍💻 Developer — Aurel Hoxha",
            value=(
                "- Discord: `teamfoxx`\n"
                "- Email: `admin@aurelhoxha.de`\n"
                "- Website: [`www.aurelhoxha.de`](https://www.aurelhoxha.de)"
            ),
            inline=True
        )
        embed.add_field(
            name="🚀 Branding — Reelab Studios",
            value=(
                "- Email: `info@reelab.studio`\n"
                "- Website: [`www.reelab.studio`](https://www.reelab.studio)"
            ),
            inline=True
        )
        embed.set_footer(
            text="Thank you for using our bot! 🤖 — Interested in having your own? Visit us at discord.gg/reelab")
        embed.set_author(name="Developers and Contributors",
                         url="https://reelab.studio/",
                         icon_url='attachment://reelab_logo.png')

        # Setting an image for the embed
        embed.set_image(url="attachment://reelab_banner.gif")

        # Attachments for the embed
        banner_file, logo_file, _, _, _ = await attachments()

        # Sending the embed with attachments
        await ctx.respond(embed=embed, files=[banner_file, logo_file], hidden=True)


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

def setup(bot):
    bot.add_cog(Credits(bot))
