import discord
from requests import get

class IPs(): #Creates the variables to be used in the function
    oldIP = ""
    newIP = ""
    message = ""
    channel = ""

async def main():
    getOldIP()
    getNewIP()
    IPLengthChecker()
    IPChangeChecker()
    saveIP()
    await sendIP()
    quit()

def getOldIP(): #Sets the value of IPs.oldIP to the saved IP address in ip.txt and prints it to the console
    print('Getting saved IP...')
    f = open("ip.txt", "r")
    IPs.oldIP = f.read()
    print(IPs.oldIP)
    f.close()

def getNewIP(): #Sets the value of IPs.newIP to the new IP address obtained from ipify and prints it to the console
    print('Getting new IP...')
    IPs.newIP = get('https://api.ipify.org').content.decode('utf8')
    print(IPs.newIP)

def IPLengthChecker(): #Checks the length of IPs.newIP to ensure a correct IP address was obtained. If an incorrect IP is obtained, it exits the program
    print('Checking IP length...')
    if len(IPs.newIP) > 15 or len(IPs.newIP) < 7:
        print('Error! IP address is too long, or too short! Quitting program...')
        quit()
    else:
        print('IP length OK')

def IPChangeChecker(): #Checks if the IP has changed. If not, it will exit the program
    print('Checking for IP changes...')
    if IPs.oldIP != IPs.newIP:
        print('IP change detected!')
    else:
        print('No IP change detected. Quitting program...')
        quit()

def saveIP (): #Saves the new IP address to ip.txt
    print('Saving new IP...')
    f = open("ip.txt", "w")
    f.write(IPs.newIP)
    f.close()

async def sendIP(): #Sends the new IP address message
    print('Sending message')
    getMessage()
    getChannelID()
    await IPs.channel.send(IPs.message.replace("[IP]", IPs.newIP)) #Replaces every instance of [IP] in the message variable with the value of IPs.newIP and sends the result to Discord

def getToken(): #Sets the token variable to token in token.txt
    global token
    f = open('token.txt', 'r')
    token = f.read()
    f.close

def getChannelID(): #Sets the value of IPs.channel to the channel ID in channel.txt
    f = open('channel.txt', 'r')
    IPs.channel = client.get_channel(int(f.read()))
    f.close()

def getMessage(): #Sets the value of IPs.message to the message in message.txt
    f = open("message.txt", "r")
    IPs.message = f.read()
    f.close()

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await main()
getToken()
intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(token)