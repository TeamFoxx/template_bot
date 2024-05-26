# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# »› Developed by Foxx
# »› Copyright © 2024 Aurel Hoxha. All rights reserved.
# »› GitHub: https://github.com/TeamFoxx
# »› For support and inquiries, please contact info@aurelhoxha.de
# »› Use of this program is subject to the terms of the MIT licence.
# »› A copy of the license can be found in the "LICENSE" file in the root directory of this project.
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#
# ⏤ { config } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

# Version Configuration: Defines the current version of the bot
version = "v1.0"

# Public Mode Configuration: Toggle to determine if the bot should operate in public mode (multiple servers) or private mode (single server)
public = False

# Privacy Policy URL: URL directing to the bot's privacy policy page
privacy_url = 'https://reelab.studio/privacy'

# Access Control: Identifies the unique IDs for developers and staff members for privileged actions
developer = {59920451372266293}
staff = {59920451372266293}

# Styling: Configures colors used in embeds throughout the bot's responses
EMBED_COLOR = 0x48689b  # primary color for embeds
HEADER_COLOR = 0x2b2d31  # color used for header sections in embeds
WARNING_COLOR = 0xd4ce82  # color used for warning messages
ERROR_COLOR = 0x834455  # color used for error messages

# Bot Required Permissions: List of permissions required by the bot to operate effectively
bot_required_permissions = [
    'read_message_history',  # Allows the bot to read the history of messages in channels
    'view_channel',  # Allows the bot to view channels
    'send_messages',  # Allows the bot to send messages in channels
    'send_messages_in_threads',  # Allows the bot to send messages in threads
    'create_public_threads',  # Allows the bot to create public threads
    'create_private_threads',  # Allows the bot to create private threads
    'attach_files',  # Allows the bot to attach files to messages
    'embed_links',  # Allows the bot to embed links in messages
    'use_external_emojis'  # Allows the bot to use external emojis
]

# Emoji Configuration: Defines custom emoji IDs for rich presence and interaction feedback
community_owner = 1217203408516284516,
community_admin = 1217203398802280631,
community_artist = 1217203397409636362,
community_developer = 1217203400593117256,
community_advisor = 1217203395434385438,
community_member = 1217203405316030595,
community_manager = 1217203403709612073,
community_eventhost = 1217203402237280488,
community_planner = 1217203741279653968,
function_emergency = 1217203837295792129,
function_tick = 1217203424425152582,
function_cross = 1217203796065648691,
function_time = 1217203427361165403,
log_link = 1217203432906297414,
promo = 1231695279200272435,
log_timeoutremoved = 1217203449654018128,
log_rolesadd = 1217203440472555710,
log_membershipscreening = 1217203998659055797,
log_timeout = 1217203448005791795,
log_memberjoin = 1217203966450860093,
log_memberleave = 1217203436551016688,
plantbig_plant = 1217203467777474640,
plant_plant = 1217204087884611665,
role_star = 1217203475004526613
