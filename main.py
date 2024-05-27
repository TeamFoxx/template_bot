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
import platform
import time
from datetime import datetime
from pathlib import Path

import discord
from colorama import Fore, Style, init
from discord.ext import commands
from tqdm import tqdm

import config
from data.secrets import token


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

# Set bot start time
start_time = datetime.now()


class Reelab(commands.Bot):
    def __init__(self):
        super(Reelab, self).__init__(
            intents=discord.Intents.all(),
            command_prefix=commands.when_mentioned_or("."),
            sync_commands=True,
            auto_check_for_updates=True
        )
        self.remove_command("help")
        self.base_path = Path(__file__).resolve().parent

        # Reset color formatting from colorama
        init(autoreset=True)

    # ⏤ { codebase } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

    # Configure logging
    logging.basicConfig(
        level=config.log_level,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Format for log messages
        handlers=[
            logging.FileHandler(config.log_file),  # Log to a file
        ]
    )
    logger = logging.getLogger(__name__)

    def load_cogs(self):
        """
        Loads all cogs, excluding '__init__.py' files, and handles errors during the load process.
        This function updates the loading progress and reports any issues encountered.
        """
        cog_directory = './cogs'
        cog_paths = [path for path in Path(cog_directory).rglob('*.py') if path.stem != '__init__']
        start_time = time.time()
        loaded_cogs_count = 0
        failed_cogs = []

        progress_bar_format = (
            f"{Fore.GREEN}Loaded:{{percentage:3.0f}}%{Fore.WHITE}|{{bar:25}}{Fore.WHITE}| "
            f"{Fore.GREEN}{{n_fmt}}/{Fore.GREEN}{{total_fmt}} "
            f"{Fore.WHITE}{{desc}}"
        )

        with tqdm(total=len(cog_paths), desc="Loading cogs", leave=False, bar_format=progress_bar_format) as progress:
            for path in cog_paths:
                cog_module = str(path).replace('/', '.').replace('\\', '.')[:-3]

                # Check if the cog's feature is enabled
                cog_name = cog_module.split('.')[-1]
                if not config.cogs.get(cog_name, False):
                    continue

                try:
                    self.load_extension(cog_module)
                    progress.set_description(f"{cog_module}")
                    progress.update(1)
                    loaded_cogs_count += 1
                    time.sleep(0.1)
                except Exception as e:
                    failed_cogs.append((cog_module, str(e)))

        load_duration = time.time() - start_time
        self.report_loading_results(failed_cogs, loaded_cogs_count, len(cog_paths), load_duration)

    @staticmethod
    def report_loading_results(failed_cogs, loaded_cogs_count, total_cogs, load_duration):
        """
        Reports the results of the cog loading process, indicating success or failure details.
        """
        cog_label = "cog" if len(failed_cogs) == 1 else "cogs"
        if failed_cogs:
            print(f"{Fore.RED}Failed {Fore.WHITE}to load {Fore.RED}{len(failed_cogs)} {cog_label} "
                  f"{Fore.WHITE}out of {total_cogs}.")
            for cog, error in failed_cogs:
                print(f"{Fore.RED}Error in {Fore.WHITE}{cog}: {Fore.LIGHTBLACK_EX}{error}")
            print(f"{Fore.GREEN}Successfully {Fore.WHITE}loaded {Fore.GREEN}{loaded_cogs_count} "
                  f"{Fore.WHITE}/{Fore.GREEN}{total_cogs} {Fore.WHITE}cogs in {load_duration:.2f} seconds.")
        else:
            print(f"{Fore.WHITE}All {Fore.GREEN}{total_cogs} cogs "
                  f"{Fore.WHITE}loaded successfully in {load_duration:.2f} seconds.")

    @staticmethod
    def display_startup_info(bot_user):
        """Displays startup information once the bot is ready."""
        border = f"{Fore.LIGHTBLACK_EX}{'━' * 54}"
        print(f"{Fore.LIGHTBLACK_EX}»› {Style.BRIGHT}{Fore.MAGENTA}Ready Information")
        print(border)
        print(f"{Fore.LIGHTBLACK_EX}»› {Fore.WHITE}Logged in as: {Fore.MAGENTA}{bot_user.name}")
        print(f"{Fore.LIGHTBLACK_EX}»› {Fore.WHITE}Developed with {Fore.RED}♥ {Fore.WHITE}by {Fore.MAGENTA}Foxx")
        print(f"{Fore.LIGHTBLACK_EX}»› {Fore.WHITE}For inquiries, please contact: {Fore.MAGENTA}info@aurelhoxha.de")
        print(f"{Fore.LIGHTBLACK_EX}»› {Fore.WHITE}Check out my GitHub: {Fore.MAGENTA}https://github.com/TeamFoxx")
        print(f"{Fore.LIGHTBLACK_EX}»› {Fore.WHITE}Join my Discord server: {Fore.MAGENTA}https://discord.gg/nQEwwyJ")
        print(border)

    @commands.Cog.listener()
    async def on_ready(self):
        """Event handler for when the bot is ready."""
        # Set the bot's activity to "Watching www.reelab.studio"
        activity = discord.Activity(name="www.reelab.studio", type=discord.ActivityType.watching)
        await self.change_presence(activity=activity)

        # Display startup information in the console
        self.display_startup_info(self.user)

        # Load all cogs (extensions) for the bot
        self.load_cogs()


# ⏤ { settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

if __name__ == '__main__':

    # Instantiate the bot
    reelab = Reelab()

    # Check OS
    system = platform.system()

    print(f"Running on {system}. Performing actions for {system}")
    if system == 'Windows':
        reelab.run(token.WINDOWS, log_handler=None)
    else:
        reelab.run(token.LINUX, log_handler=None)
