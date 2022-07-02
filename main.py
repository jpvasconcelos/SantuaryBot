import datetime
import discord
from discord.ext import commands, tasks
import batatinha

bot = commands.Bot('!')
TOKEN = batatinha.my_token()
SantuaryCD = 3
santuaryFloor = "4F"
santuaryMap = None
# santuaryConfirm = f"Tem certeza que quer registrar santuário no {santuaryMap} - {SantuaryFloor}?"


#checar se o bot iniciou
@bot.event
async def on_ready():
    print(f"to na area, sou o {bot.user}")

# @bot.event #pegar os emotes do disc no terminal
# async def on_reaction_add(reaction, user):
#     print(reaction.emoji,user)

#cria a embed com as opções do santuário
@bot.command(name='santuario')
async def santuary_check(ctx):
    
    embed = discord.Embed(
        title = "Onde você quer colocar seu santuário?",
        description="obs: confira se não tem outro clã no local",
        color=0xFA8072
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="1️⃣ - Haven's Way Labyrint", value='--', inline=False)
    embed.add_field(name="2️⃣ - Redmoon Labyrint", value='--', inline=False)
    embed.add_field(name="3️⃣ - Redmoon Valley", value='--', inline=False)
    embed.add_field(name="4️⃣ - Snake Pit Lab(4F only)", value='--', inline=False)
    embed.add_field(name="5️⃣ - Abandoned Mine Lab(4F only)", value='--', inline=False)

    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction("1️⃣")
    await botmsg.add_reaction("2️⃣")
    await botmsg.add_reaction("3️⃣")
    await botmsg.add_reaction("4️⃣")
    await botmsg.add_reaction("5️⃣")

    
    # seleciona o mapa do santuario e cria embed para escolher o andar (caso só haja 1 andar possivel, registra o santuário no mapa)
    @bot.event
    async def on_reaction_add(reaction, user):
        now = datetime.datetime.now()
        now = now.strftime('%d/%m/%Y às %H:%M')

        msg = reaction.message
        santuaryMap = None

        if msg.id == botmsg.id:

            if user == bot.user:
                return

            if reaction.emoji == "1️⃣":
                santuaryMap = "Haven's Way Labyrint"
                await botmsg.delete()

            if reaction.emoji == "2️⃣":
                santuaryMap = "Redmoon Labyrint"
                await botmsg.delete()

            if reaction.emoji == "3️⃣":
                santuaryMap = "Redmoon Valley"
                await botmsg.delete()

            if reaction.emoji == "4️⃣":
                santuaryMap = "Snake Pit Lab - 4F"
                await botmsg.delete()
                await botmsg.channel.send(f"{user.name} registrou o santuário em {santuaryMap}: " + now)
                await botmsg.channel.send(f"O Santuário termina em {SantuaryCD} dias!")
                
                return

            if reaction.emoji == "5️⃣":
                santuaryMap = "Abandoned Mine Lab - 4F"
                await botmsg.delete()
                # await botmsg.channel.send(santuaryConfirm)
                await botmsg.channel.send(f"{user.name} registrou o santuário em {santuaryMap}: " + now)
                await botmsg.channel.send(f"O Santuário termina em {SantuaryCD} dias!")

                return

            elif reaction.emoji != "5️⃣" and reaction.emoji != "4️⃣" and reaction.emoji != "3️⃣" and reaction.emoji != "2️⃣" and reaction.emoji != "1️⃣":
                await reaction.remove(user)
                return
                

            embed2 = discord.Embed(
                title = f"O mapa escolhido foi {santuaryMap}",
                description="escolha o andar:",
                color=0xFA8072
            )
            embed2.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
            embed2.add_field(name="1️⃣ - 1F", value='--', inline=False)
            embed2.add_field(name="2️⃣ - 2F", value='--', inline=False)
            embed2.add_field(name="3️⃣ - 3F", value='--', inline=False)
            embed2.add_field(name="4️⃣ - 4F", value='--', inline=False)
            embed2.add_field(name="❌ - CANCELAR", value='--', inline=False)

            botmsg2 = await ctx.send(embed=embed2)
            await botmsg2.add_reaction("1️⃣")
            await botmsg2.add_reaction("2️⃣")
            await botmsg2.add_reaction("3️⃣")
            await botmsg2.add_reaction("4️⃣")
            await botmsg2.add_reaction("❌")

            @bot.event # seleciona o andar e entrega o registro do santuario no mapa/andar escolhidos
            async def on_reaction_add(reaction, user):
                
                msg2 = reaction.message
                santuaryFloor = None

                if msg2.id == botmsg2.id:

                    if user == bot.user:
                        return

                    if reaction.emoji == "1️⃣":
                        santuaryFloor = "1F"
                        await botmsg2.delete()

                    if reaction.emoji == "2️⃣":
                        santuaryFloor = "2F"
                        await botmsg2.delete()

                    if reaction.emoji == "3️⃣":
                        santuaryFloor = "3F"
                        await botmsg2.delete()

                    if reaction.emoji == "4️⃣":
                        santuaryFloor = "4F"
                        await botmsg2.delete()

                    if reaction.emoji == "❌":
                        await botmsg2.delete()

                    elif reaction.emoji != "❌" and reaction.emoji != "4️⃣" and reaction.emoji != "3️⃣" and reaction.emoji != "2️⃣" and reaction.emoji != "1️⃣":
                        await reaction.remove(user)
                        return

                    await botmsg2.channel.send(f"{user.name} registrou o santuário em {santuaryMap} - {santuaryFloor}: " + now)
                    await botmsg2.channel.send(f"O Santuário termina em {SantuaryCD} dias!")


        else:
            return

bot.run(TOKEN)

#  ✅