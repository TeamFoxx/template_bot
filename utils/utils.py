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
    Keep in mind: banner_file & logo_file has to be attached as image file.
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
    >> banner_file - logo_file - footer_file <<
    """
    header_path = "./data/pictures/utils/reelab_banner.gif"
    banner_file = discord.File(header_path, filename="reelab_banner.gif")

    icon_path = "./data/pictures/utils/reelab_logo.png"
    logo_file = discord.File(icon_path, filename="reelab_logo.png")

    footer_path = "./data/pictures/utils/reelab_footer.png"
    footer_file = discord.File(footer_path, filename="reelab_footer.png")

    return banner_file, logo_file, footer_file


async def no_permission():
    """
    Create the "no_permission" embed.
    Keep in mind: footer_file has to be attached as image file.
    """
    # Create an embed for permission denial
    no_permission_embed = discord.Embed(
        description="`⚠️` **- Permission Denied!** — You do not have permission to use this command. Please contact the [developer](https://reelab.studio) for access.",
        color=config.EMBED_COLOR
    )
    no_permission_embed.set_footer(text="Access Control • Powered by Reelab Studios")
    no_permission_embed.set_image(url="attachment://reelab_footer.png")

    return no_permission_embed
