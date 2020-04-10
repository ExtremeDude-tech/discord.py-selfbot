#<--------------Colors Start-------------->
purple_dark= 0x6a006a
purple_medium= 0xa958a5
purple_light= 0xc481fb
orange= 0xffa500
gold= 0xdaa520
red_dark= 8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
pink= 0xff9dbb
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9
#<--------------Colors End-------------->

#<--------------Imports Start-------------->
import discord
from discord.ext import commands
from datetime import *
from colorama import *
import json
import threading
from tkinter import messagebox
import tkinter
root = tkinter.Tk()
root.withdraw()
from discord.ext import tasks
import psutil
import asyncio
import time
import os
import sys
from pyfiglet import Figlet
import time
import requests
import random
from discord.ext.commands import CommandNotFound
#<--------------Imports End-------------->

#<--------------Prefix Start-------------->
async def get_pre(bot, message):
    with open("config.json") as f:
        pprefix = json.load(f)
        prefix = pprefix["prefix"]
    return prefix
#<--------------Prefix Stop-------------->
last = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
bot = commands.Bot(command_prefix=get_pre, self_bot=True)
bot.remove_command('help')
init()

@bot.event
async def on_command(ctx): 
    with open("config.json") as f:
        da = json.load(f)
        if da['delete_after_execute'] == "yes":
            await ctx.message.delete()
        elif da['delete_after_execute'] == "no":
            pass
        else:
            input("Please enter a value to 'delete_after_execute' in config.json! (value muse be yes or no)")
            os._exit(0)
"""@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return"""
def show_on():
    os.system("cls")
    print('SelfBot Made by 0x72')
    with open("config.json") as m:
        get_prefix = json.load(m)["prefix"]
    print()
    os.system(f'title Connected as {bot.user.name} / made by 0x72')
    print('>> SelfBot')
    print(f">> Name: {bot.user.name}")
    print(f">> ID: {bot.user.id}")
    print(f">> Prefix: {get_prefix}")
    print(f">> Last login: {last}")
    print()
@bot.event
async def on_ready():
    show_on()
    
afk_stat = 0

@bot.event
async def on_message(message):
    global afk_stat
    await bot.process_commands(message)
    if afk_stat == 1:
        with open("config.json") as m:
            mesaje = json.load(m)["afk_message"]
            if mesaje == "":
                mesaje = "This is an autoresponse message! User is now AFK.."
                
        if message.guild is None:
            if message.author == bot.user:
                return
            await message.channel.send(mesaje)
        


@bot.command()
async def btc(ctx, suma: int=None):
    if suma is None:
        await ctx.send(f"Usage: {ctx.prefix}btc <amount>");return
    else: pass
    with open("config.json") as m:
        adresa = json.load(m)["btc"]
        if adresa == "": input("Please enter a value to 'btc' in config.json!"); await ctx.send("Please check console log!")
        else:
            embed= discord.Embed(color= orange, title="Send money to",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.add_field(name="Address", value=f"{adresa}", inline=False)
            embed.add_field(name="Amount", value=f"${suma}", inline=False)
            embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
            embed.set_footer(text=" made by 0x72")
            try:
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"My BTC address is: **{adresa}**") 

@bot.command()
async def paypal(ctx, suma: int=None):
    if suma is None:
        await ctx.send(f"Usage: {ctx.prefix}paypal <amount>");return
    else: pass
    with open("config.json") as m:
        adresa = json.load(m)["paypalmail"]
        if adresa == "": input("Please enter a value to 'paypalmail' in config.json!"); await ctx.send("Please check console log!");return
        else: pass
        embed= discord.Embed(color= aqua, title="Send money to",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="Address", value=f"{adresa}", inline=False)
        embed.add_field(name="Amount", value=f"${suma}", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/d4Wg3BW.png")
        embed.set_footer(text=" made by 0x72")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"My BTC address is: **{adresa}**")

@bot.command()
async def price(ctx, curen: str=None):
    if curen is None:
        await ctx.send(f">> Please specify a currency\nAvaliable Currency's: `Ethereum (eth), Bitcoin (btc), Litecoin (ltc), Monero (xmr)`"); await ctx.send("Please check console log!");return
    elif curen.lower() == "btc" or curen.lower() == "bitcoin":
        try:
            with requests.session() as ses:
                resp = ses.get('https://blockchain.info/ticker')
                pret = resp.json()['USD']['last']
                pret1 = resp.json()['EUR']['last']
                pret2 = resp.json()['GBP']['last']
                try:
                    embed= discord.Embed(color= orange, title="Bitcoin Price", description=f"Show's the current Bitcoin Price!",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="Current Price is:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
                    embed.set_footer(text=" made by 0x72")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"Bitcoin Price:\n${pret}\n€{pret1}\n£{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")

    elif curen.lower() == "eth" or curen.lower() == "ethereum":
        try:
            with requests.session() as ses:
                resp = ses.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP')
                pret = resp.json()['USD']
                pret1 = resp.json()['EUR']
                pret2 = resp.json()['GBP']
                try:
                    embed= discord.Embed(color= purple_medium, title="Ethereum Price", description=f"Show's the current Ethereum Price!",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="Current Price is:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/Huyedhz.png")
                    embed.set_footer(text=" made by 0x72")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"Ethereum Price:\n${pret}\n€{pret1}\n£{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")
    elif curen.lower() == "ltc" or curen.lower() == "litecoin":
        try:
            with requests.session() as ses:
                resp = ses.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR,GBP')
                pret = resp.json()['USD']
                pret1 = resp.json()['EUR']
                pret2 = resp.json()['GBP']
                try:
                    embed= discord.Embed(color= blue_dark, title="Litecoin Price", description=f"Show's the current Litecoin Price!",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="Current Price is:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/Hn4zLbc.png")
                    embed.set_footer(text=" made by 0x72")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"Litecoin Price:\n${pret}\n€{pret1}\n£{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")
    elif curen.lower() == "xmr" or curen.lower() == "monero":
        try:
            with requests.session() as ses:
                resp = ses.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR,GBP')
                pret = resp.json()['USD']
                pret1 = resp.json()['EUR']
                pret2 = resp.json()['GBP']
                try:
                    embed= discord.Embed(color= orange, title="Monero Price", description=f"Show's the current Monero Price!",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="Current Price is:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/nIjEKrN.png")
                    embed.set_footer(text=" made by 0x72")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"Monero Price:\n${pret}\n€{pret1}\n£{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")
    else:
        await ctx.send("Invalid currency!")
@bot.command()
async def coinflip(ctx):
    lista = ['head', 'tails']
    coin = random.choice(lista)
    try:
        if coin == 'head':
            embed= discord.Embed(color= orange, title="Head",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(color= orange, title="Tails",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
    except discord.HTTPException:
        if coin == 'head':
            await ctx.send("Coinflip: **Head**")
        else:
            await ctx.send("Coinflip: **Tails**")
@bot.command()
async def ip(ctx, ip: str=None):
    if ip is None: await ctx.send("Please sepcify an IP address");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("Invalid IP address")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color= blue_light, title=f"INFO",timestamp=datetime.utcfromtimestamp(time.time()))
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'City', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Region', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'Country', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinates', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organization', value=f'{j["org"]}', inline=True)
                        embed.set_footer(text=" made by 0x72")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def ping(ctx):
    try:
        embed= discord.Embed(color= green_light, title=f"Pong",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" made by 0x72")
        before = time.monotonic()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        ping = (time.monotonic() - before) * 1000
        embed= discord.Embed(color= green_light, title=f"Ping: {int(ping)}ms",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" made by 0x72")
        await message.edit(embed=embed)

    except discord.HTTPException:
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping: `{int(ping)}ms`")
@bot.command()
async def ascii(ctx, *,text: str=None):
    if text is None:
        await ctx.send("Invalid argument")
    else:
        f = Figlet(font='Slant')
        j = (f.renderText(text))
        try:
            embed= discord.Embed(color= aqua, description=f"```{j}```",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
        except discord.HTTPException:
            try:
                await ctx.send(f"```{j}```")
            except Exception as e:
                await ctx.send(f"Error: {e}")
            
def is_me(m):
    return m.author == bot.user
@bot.command()
async def purge(ctx, amount:int=None):
    try:
        if amount is None:
            await ctx.send("Invalid amount")
        else:
            deleted = await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
            asd = await ctx.send('Deleted {} message(s)'.format(len(deleted)))
            await asyncio.sleep(3)
            await asd.delete()
    except:
        try:
            await asyncio.sleep(1)
            c = 0
            async for message in ctx.message.channel.history(limit=amount):
                if message.author == bot.user:
                    c += 1
                    await message.delete()
                else:
                    pass
            asd = await ctx.send('Deleted {} message(s)'.format((c)))
            await asyncio.sleep(3)
            await asd.delete()
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def playing(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=0, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Playing {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def streaming(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=1, name=f"{status}", url="https://www.twitch.tv/robert832")
            await bot.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Streaming {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def listening(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=2, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Listening {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def watching(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=3, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Watching {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def removestatus(ctx):

    try:
        game = discord.Activity(type=-1)
        await bot.change_presence(activity=game)
        await ctx.send(f"Status removed")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def nickname(ctx, *, name: str=None):
    if name is None:
        await ctx.send(f"Usage: {ctx.prefix}rename <new name>")
    elif len(name) < 1:
        await ctx.send("Name need to have atleast 1 characters")
    else:
        try:
            await ctx.author.edit(nick=name)
            await ctx.send(f"Change nickname into `{name}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def spfp(ctx):
    try:
        embed= discord.Embed(color= aqua, description=f"[Server Icon]({ctx.guild.icon_url})",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=" made by 0x72")
        await ctx.send(embed=embed)
    except discord.HTTPException:    
        await ctx.send(f"{ctx.guild.icon_url}")
    except:
        await ctx.send(f"You must be into a guild! For user avatar use {ctx.prefix}pfp <user>")
@bot.command()
async def pfp(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send(f"Usage: {ctx.prefix}pfp <user>")
    else:
        try:
            embed= discord.Embed(color= purple_dark, description=f"[{user.name}'s Avatar]({user.avatar_url})",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
        except discord.HTTPException:    
            await ctx.send(f"{user.avatar_url}")
        except Exception as e:
            await ctx.send(f"Eror: {e}")
                
@bot.command()
async def invisiblenickname(ctx):
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def junknickname(ctx):

    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is a big mess :)")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def help(ctx):
    try:
        embed= discord.Embed(color= pink, title="  Commands",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="Information", value="help, ip, ping", inline=False)
        embed.add_field(name="Status", value="playing, streaming, watching, listening, removestatus", inline=False)
        embed.add_field(name="Fun", value="coinflip, spam, junk, haxor, dox, nickname, inivisiblenickname, junknickname, spfp, pfp", inline=False)
        embed.add_field(name="Money", value="price, btctousd, usdtobtc, paypal, btc", inline=False)
        embed.add_field(name="Moderation", value="purge, shutdown, ban, kick, unban", inline=False)
        embed.add_field(name="Others", value="ascii, shrug, embed", inline=False)
        embed.set_footer(text=" made by 0x72")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Error: This channel have embed links off, so check console")
        os.system("cls")
        print("""
        Commands

        Information:
        - help
        - ip
        - ping

        Status:
        - playing
        - streaming
        - watching
        - listening
        - removestatus

        Fun:
        - conflip
        - spam
        - junk
        - haxor
        - dox
        - nickname
        - invisiblenickname
        - junknickname
        - spfp
        - pfp

        Money:
        - price
        - usdtobtc
        - btctousd
        - paypal
        - btc

        Moderation:
        - purge
        - shutdown
        - ban
        - kick
        - unban


        Others:
        - ascii
        - shrug
        - embed
        - afk

        Press enter to comeback to main screen..
        """)
        input()
        show_on()
strbtc = 0


@bot.command()
async def usdtobtc(ctx, num:int=None):
    if num is None:
        await ctx.send("Invalid format pal")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num/pret
            try:
                embed= discord.Embed(color= orange, title="USD -> BTC", description=f"USD: {num}\n BTC: {final}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
                embed.set_footer(text=" made by 0x72")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"USD -> BTC:\n\nUSD: {num}\n BTC: {final}")
@bot.command()
async def btctousd(ctx, num:int=None):
    if num is None:
        await ctx.send("Invalid format pal")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num*pret
            try:
                embed= discord.Embed(color= orange, title="BTC -> USD", description=f"BTC: {num}\n USD: {final}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/HHSzzNz.png")
                embed.set_footer(text=" made by 0x72")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"BTC -> USD:\n\nBTC: {num}\n USD: {final}")

@bot.command()
async def afk(ctx):
    global afk_stat
    if afk_stat == 0:
        afk_stat += 1
        await ctx.send("Afk mode `ON`")
            
    elif afk_stat == 1:
        afk_stat -= 1
        await ctx.send("Afk mode `OFF`")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("Who you want unbanned? Please specify his id")
        return
    else:pass
    try:
        user1 = await bot.fetch_user(user)
        await ctx.guild.unban(user1)
        await ctx.send(f"User {user.mention}({user.id}) has been unbanned")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
async def shutdown(ctx):
    def check(m):
            return m.author == ctx.author and m.content == "yes" or m.content == "y"
    await ctx.send("‎‏‏‎You have 10 seconds type `y` or `yes` or command will be avoided")
    try:
        m = await bot.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Command avoided")
            
    else:
        os._exit(0)
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member=None, *, reason: str=None):
    if user is None:
        await ctx.send("Who you want banned? Please mention an user")
        return
    elif user == ctx.author:
        await ctx.send("Nice try but you can't ban yourself")
        return
    else:pass
    try:
        await user.ban(reason=reason)
        await ctx.send(f"User {user.mention}({user.id}) has been banned for reason {reason}")
    except Exception as e:
        await ctx.send(f"{e}")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member=None, *, reason: str=None):
    if user is None:
        await ctx.send("Who you want kicked? Please mention an user")
        return
    elif user == ctx.author:
        await ctx.send("Nice try but you can't kick yourself")
        return
    else:pass
    try:
        await user.ban(reason=reason)
        await ctx.send(f"User {user.mention}({user.id}) has been kicked for reason {reason}")
    except Exception as e:
        await ctx.send(f"{e}")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")
@bot.command()
async def spam(ctx, amount:int=None, *, message: str=None):
    try:
        if amount is None or message is None:
            await ctx.send(f"Usage: {ctx.prefix}spam <amount> <message>")
        else:
            for each in range (0, amount):
                await ctx.send(f"{message}")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def junk(ctx):
    for each in range(0, 11):
        d = "\n"*100
        await ctx.send(f".{d}.")
@bot.command()
async def haxor(ctx, *, message: str=None):
    
    if message is None:
        await ctx.send("Insert message sir")
    else:
        try:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')

            embed= discord.Embed(color= green_dark, title="1337 Haxor", description=f"{leetmsg.upper()}",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/TR2cv3C.jpg")
            embed.set_footer(text=" made by 0x72")
            await ctx.send(embed=embed)
        except discord.HTTPException:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')
            await ctx.send(f"{leetmsg.upper()}")
@bot.command()
async def dox(ctx, user: discord.Member=None):
    emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com"])
    nr = random.choice(range(0,9999))
    ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
    country = random.choice(['Niger', 'Niggeria', "3rd wolrd country", "Africa"])
    if user is None:
        await ctx.send("Please mention a member")
    else:
        try:
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %0",description="Getting his email and address",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" made by 0x72")
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %50",description="Getting ip and stuffs",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" made by 0x72")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Doxing in progress %100",description="Getting mom credit cards",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" made by 0x72")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"Dox of {user.name}",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.add_field(name=f'Email', value=f'{user.name}{nr}@{emaillist}', inline=False)
            embed.add_field(name=f'IP', value=f'{ip}', inline=False)
            embed.add_field(name=f'Country', value=f'{country}', inline=False)
            embed.set_footer(text=" made by 0x72")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send("Doxing in progress %0 - Getting his email and address")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %50 - Getting ip and stuffs")
            await asyncio.sleep(2)
            await a.edit(content="Doxing in progress %100 - Getting mom credit cards")
            await asyncio.sleep(2)
            await a.edit(content=f"Dox of {user.name}:\n\nEmail: {user.name}{nr}@{emaillist}\nIP: {ip}\nCountry: {country}")



@dox.error
async def dox_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
async def embed(ctx,*,text: str=None):
    if text is None:
        await ctx.send("Add some text sir")
    else:
        embed= discord.Embed(color= orange,description=f"{text}",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" made by 0x72")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"Error: This channel have embed links off!")
def start():
    try:
        os.system("title Connecting to discord server")
        print("\n>> Connecting to discord servers...")

        with open("config.json") as f:
            token = json.load(f)
            bot.run(token["token"], bot=False)
    except Exception as e:
        print(f"\n>> Something went wrong, please check the error!\n>> Error: {e}")
        input()
threading.Thread(target=start, args=()).start()