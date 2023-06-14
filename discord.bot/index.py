import discord
import sqlite3

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Ready')
	cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, reallyname TEXT, age INT, rulesaccept TEXT)""")

@bot.command()
async def ping(ctx):
	await ctx.respond("Ponk!")

@bot.command()
async def rules(ctx):
	await ctx.respond("""
    ```ansi
[2;45m [2;37mRules[0m[2;45m [0m
``` \n
	\n```ansi
[2;41m [2;37mНа[0m[2;41m [2;37mсервере[0m[2;41m [2;37mзапрещено[0m[2;41m [0m
```
    \n
	\n`0/1` обман
	\n`0/2` капс
	\n`0/3` пиар
	\n`0/4` угрозы
	\n`0/6` пропаганда
	\n`0/7` споры
	\n`0/10` игнор администрации
	\n`0/11` флуд
	\n`0/12` злоупотребление матом
	\n`0/13` троллинг
	\n`0/15` nsfw: шок-контент, порнографию.
	\n
	\n`0/17` администратор вправе требовать изменение ника и картинки, если считает, чᴛо они оскорбляют ᴋоᴦо-либо.
	\n`0/18` не допускается применение террористической символики и/иᴧи символики запрещенных организаций, призыв ᴋ насилию и экстремизму.
	\n
	\n**ʙᴄᴇ чᴛо нᴀходиᴛᴄя зᴀ ᴦᴩᴀнью ᴄᴇᴩʙᴇᴩᴀ, нᴇ яʙᴧяᴇᴛᴄя оᴛʙᴇᴛᴄᴛʙᴇнноᴄᴛью ᴄᴇᴩʙᴇᴩᴀ.**
	\n**нᴇзнᴀниᴇ ᴨᴩᴀʙиᴧ нᴇ оᴄʙобождᴀᴇᴛ оᴛ оᴛʙᴇᴛᴄᴛʙᴇнноᴄᴛи. ᴨᴩᴀʙиᴧᴀ ᴩᴀᴄᴨᴩоᴄᴛᴩᴀняюᴛᴄя нᴀ ʙᴄᴇ ᴋᴀнᴀᴧы.**
	\n**ᴀдʍиниᴄᴛᴩᴀᴛоᴩ ʍожᴇᴛ нᴀзнᴀчиᴛь ᴧюбой ᴄᴩоᴋ нᴀᴋᴀзᴀния, ʙ ᴩᴀʍᴋᴀх ᴩᴀзуʍноᴦо.**
    """)
    
@bot.command()
async def request(ctx,имя,возраст,правила):
	if cursor.execute(f"SELECT id FROM users WHERE id = {ctx.author.id}").fetchone() == None:
		cursor.execute(f"INSERT INTO users VALUES({ctx.author.id},'{ctx.author.name}', '{имя}', '{возраст}', '{правила}')")
		connection.commit()
		await ctx.respond("""Спасибо за вашу заявку!""")
	else:
		await ctx.respond("""Вы уже оставили заявку и/или вы не можете оставить заявку!""")

connection = sqlite3.connect('dissto5opka.sql',check_same_thread=False)
cursor = connection.cursor()

bot.run("MTExODQ1NDA2MDI0NTM0MDIyMQ.G_pu5v.kXR6SFXCATRHakLEiaq5nHvluGwC8KIGubf5N8")