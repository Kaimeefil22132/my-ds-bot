import discord
from discord.ext import commands
import get_model

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    res = ""
    img_format = ["png", "jpg", "jpeg"]
    if ctx.message.attachments != []:
        print(ctx.message.attachments)
        for attachment in ctx.message.attachments:
            file_name = attachment.filename 
            await attachment.save(file_name) 
            format = file_name.split(".")[1]
            if format not in img_format:
                await ctx.send["aqsdewsfaredg"]
                return
            await ctx.send("Файл сохранён Сэр!!!!")
            res = get_model.class_image(file_name)
            if res == "":
                await ctx.send("C vjltkm. xnjnnj ")
            else:
                await ctx.send("edfrgtdhfydcgtjuhy")
                
bot.run("MTE1MjYwMDA3Mjc1Mjc0MjQ4MQ.G1tErv.10kItzGH4J3Z_0JNIqm1x4C6JeU9LslHxTIBgk")