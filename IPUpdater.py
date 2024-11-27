import os
import discord
from requests import get

#Creates the variables to be used in the function#
class IPs():
    oldIP = ""
    newIP = ""
    message = ""

async def main():
    #Reads the contents of the saved IP address and saves it to the IPs.oldIP variable then it to the console#
    f = open("ip.txt", "r")
    IPs.oldIP = f.read()
    print(IPs.oldIP)
    print(type(IPs.oldIP))
    
    #Gets the new IP address using ipify and saves it to the IPs.newIP varaiable then prints it to the console#
    IPs.newIP = get('https://api.ipify.org').content.decode('utf8')
    print(type(IPs.newIP))
    print(IPs.newIP)
    
    #Checks if the length of the new IP to ensure no error messages get sent into Discord#
    if len(IPs.newIP) >= 16 or len(IPs.newIP) <= 6:
        print('Error! IP address is too long, or too short!')
        
    #Checks to see if the new IP matches the old one. If not, it will write the new one to ip.txt and send message.txt to Discord#
    else:
        if IPs.oldIP != IPs.newIP:
            f = open("ip.txt", "w")
            f.write(IPs.newIP)
            f.close()
            f = open("message.txt", "r")
            IPs.message = f.read()
            f.close()
            
            #Replaces every instance of '[IP]' in message.txt with IPs.newIP before sending a Discord message#
            print(IPs.message.replace("[IP]", IPs.newIP))
            print(f'The server IP address has changed. The new IP address is: {IPs.newIP}:25567')
            channel = client.get_channel([INSERT CHANNEL ID HERE])
            await channel.send(IPs.message.replace("[IP]", IPs.newIP))
    quit()

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await main()
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('[INSERT BOT TOKEN HERE]')
