IPUpdater is a simple Discord bot that checks the machine's public IP and sends it into a Discord server. It is intended to be used by those who are self-hosting a Minecraft server with an ISP that does not provide a static IP. THIS IS NOT AN OFFICIAL MINECRAFT OR DISCORD PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG, MICROSOFT OR DISCORD. I am not liable for any issues this program may cause.

Instructions:
 - Ensure you have Python installed. It can be found at https://www.python.org/downloads/
 - Ensure you have Discord.py installed. Instructions can be found at https://discordpy.readthedocs.io/en/stable/intro.html
 - If your Python version does not have audioop, a long term support version can be found at https://github.com/AbstractUmbra/audioop
 - Ensure you have the Requests library installed. It can be found at http://docs.python-requests.org/en/latest/
 - Download the code of this repository.
 - Replace the contents of channel.txt with the Discord channel ID you want the bot to send messages to. Next, replace the contents of token.txt with your Discord bot's token and save your changes. Instructions on creating a Discord bot and adding it to your server can be found somewhere. You're on your own for this one since I can't find any good tutorials out there and I don't want to make my own.
 - In message.txt, write the message you would like the bot to send to your server when the IP changes. IP in brackets ([IP]) will be replaced by the new IP address. An example might be: "The Minecraft server IP has changed. The new IP address is: [IP]:25565." This will be sent as "The Minecraft server IP has changed. The new IP address is: [Your current IP]:25565." If you are not using Minecraft's default port (25565) you must specifiy the port number or users will not be able to join your server. **If message.txt is blank, the program will crash!**
 - Schedule the the script to run every 15 minutes or your desired time. This can be done with Task Scheduler on Windows or Cron on Linux. If you're hosting a Minecraft server on a Mac, your tactics confuse and scare me so you're on your own for figuring this step out.
