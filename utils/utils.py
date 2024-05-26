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
import config


# ⏤ { embed functions } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

async def header():
    """
    Creates and returns an embed for the header with the Reelab Studio information.
    Attachments: >> banner_file, logo_file, _, _, _ <<
    """
    header = discord.Embed(colour=config.HEADER_COLOR)
    header.set_author(
        name="www.reelab.studio",
        url="https://reelab.studio/",
        icon_url="attachment://reelab_logo.png"
    )
    header.set_image(
        url="attachment://reelab_banner.gif"
    )
    return header


async def attachments():
    """
    Prepares and returns the attachments for the Reelab Studio message.
    >> banner_file, logo_file, footer_file, footer_warning_file, footer_error_file <<
    """
    header_path = "./data/pictures/utils/reelab_banner.gif"
    banner_file = discord.File(header_path, filename="reelab_banner.gif")

    icon_path = "./data/pictures/utils/reelab_logo.png"
    logo_file = discord.File(icon_path, filename="reelab_logo.png")

    footer_path = "./data/pictures/utils/reelab_footer.png"
    footer_file = discord.File(footer_path, filename="reelab_footer.png")

    footer_warning_path = "./data/pictures/utils/reelab_warning_footer.png"
    footer_warning_file = discord.File(footer_warning_path, filename="reelab_warning_footer.png")

    footer_error_path = "./data/pictures/utils/reelab_error_footer.png"
    footer_error_file = discord.File(footer_error_path, filename="reelab_error_footer.png")

    return banner_file, logo_file, footer_file, footer_warning_file, footer_error_file


async def no_permission():
    """
    Create the "no_permission" embed.
    Attachments: >> _, _, _, footer_warning_file, _ <<
    """
    # Create an embed for permission denial
    no_permission_embed = discord.Embed(
        description="`⚠️` **- Permission denied!** — You do not have permission to use this command. Please contact the [developer](https://reelab.studio) for access.",
        color=config.ERROR_COLOR
    )
    no_permission_embed.set_footer(text="Access Control • Powered by Reelab Studios")
    no_permission_embed.set_image(url="attachment://reelab_error_footer.png")

    return no_permission_embed


async def check_permissions(ctx):
    required_permissions = config.bot_required_permissions
    bot_permissions = ctx.guild.me.guild_permissions
    missing_permissions = [perm for perm in required_permissions if not getattr(bot_permissions, perm)]

    if missing_permissions:
        missing_permissions_names = '\n- '.join([perm.replace('_', ' ').title() for perm in missing_permissions])
        embed = discord.Embed(
            description=f"`⚠️` **- Missing permissions!** - The bot needs the following permissions in order to work properly:\n\n- {missing_permissions_names}",
            color=config.WARNING_COLOR
        )
        embed.set_footer(text="Access Control • Powered by Reelab Studios")
        embed.set_image(url="attachment://reelab_warning_footer.png")

        # Attachments for the embed
        _, _, _, footer_warning_file, _ = await attachments()

        await ctx.respond(embed=embed,
                          files=[footer_warning_file],
                          hidden=True)
        return False
    return True
