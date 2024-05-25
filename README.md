# 🪴 Reelab_Template_Bot

> Reelab_Template_Bot is a versatile bot designed to streamline your workflow and enhance your Discord experience. Below are the key commands and features of the bot:

## ⚙️ Administration

---

- **`/credits`**
  - **Description:** Displays the credits and acknowledgements for the bot.
  - **Usage:** Use this command to view information about the developers and contributors to the bot.

- **`/reload`**
  - **Description:** Reloads a specified cog within the bot.
  - **Usage:** This command is useful for developers who need to update or refresh specific functionalities without restarting the entire bot.
  - **Example:** `/reload [cog_name]` where `[cog_name]` is the name of the cog you wish to reload.

- **`/metrics`**
  - **Description:** Provides various metrics and statistics about the bot's performance and usage.
  - **Usage:** Use this command to get insights into how the bot is performing, including data on commands used, uptime, and more.

- **📝 Config File**
  - **Description:** A configuration file where emojis, version, roles, and channels can be defined.
  - **Usage:** Customize the bot's behavior and appearance by editing the config file. This includes setting up specific emojis for reactions, defining the version of the bot, assigning roles, and specifying channels for various bot functions.

## ✨ Features

---

### 📜 Commands

- **`/help`**
  - **Description:** Lists all available commands and their descriptions.
  - **Usage:** Use this command to get a comprehensive list of what the bot can do.
  - **Example:** `/help`

### 🎉 Events

- **`on_member_join`**
  - **Description:** Triggered when a new member joins the server.
  - **Usage:** Can be used to send a welcome message or assign a role to new members.
  - **Example Implementation:** 
    ```python
    @bot.event
    async def on_member_join(member):
        welcome_channel = bot.get_channel('your-welcome-channel-id')
        await welcome_channel.send(f"Welcome to the server, {member.mention}!")
    ```

- **`on_message`**
  - **Description:** Triggered when a message is sent in the server.
  - **Usage:** Can be used for message filtering, logging, or triggering specific responses.
  - **Example Implementation:** 
    ```python
    @bot.event
    async def on_message(message):
        if message.content == 'hello':
            await message.channel.send('Hello!')
        await bot.process_commands(message)
    ```

### 🔧 Other Functionalities

- **🤖 Auto-Role Assignment**
  - **Description:** Automatically assigns a specified role to new members.
  - **Usage:** Useful for onboarding new members with default roles.
  - **Example Implementation:** 
    ```python
    @bot.event
    async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)
    ```

- **📅 Scheduled Announcements**
  - **Description:** Sends scheduled announcements to a specified channel.
  - **Usage:** Can be used for regular updates or reminders.
  - **Example Implementation:** 
    ```python
    import asyncio

    async def scheduled_announcement():
        await bot.wait_until_ready()
        channel = bot.get_channel('your-channel-id')
        while not bot.is_closed():
            await channel.send("This is a scheduled announcement.")
            await asyncio.sleep(3600) # 1 hour

    bot.loop.create_task(scheduled_announcement())
    ```

---

## 🧑‍💻 Developer / Publisher
»› Developed by Foxx \
»› Copyright © 2024 Aurel Hoxha. All rights reserved. \
»› GitHub: https://github.com/TeamFoxx \
»› For support and inquiries, please contact [info@aurelhoxha.de](mailto:info@aurelhoxha.de) \
»› Use of this program is subject to the terms of the MIT licence. \
»› A copy of the license can be found in the "LICENSE" file in the root directory of this project.
