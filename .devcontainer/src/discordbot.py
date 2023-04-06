import discord
from discord.ext import commands
import RPi.GPIO as GPIO

import os



TOKEN =  os.environ.get('DISCORD_TOKEN')
POWER_PIN = os.environ.get('POWER_PIN')
POWER_LED_PIN = os.environ.get('POWER_LED_PIN')



bot = commands.Bot(command_prefix='+')

@bot.command()
async def gpio_on(ctx, pin: int):
    if current_state == "OFF":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        await ctx.send(f"GPIO pin {pin} turned on.")
    current_state = "ON"

@bot.command()
async def gpio_off(ctx, pin: int):
    if current_state == "ON":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        await ctx.send(f"GPIO pin {pin} turned off.")
    current_state = "OFF"



bot.run(TOKEN)
