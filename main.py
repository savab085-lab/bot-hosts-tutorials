intents.guilds = True
intents.members = True
intents.message_content = True

# No prefix commands
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}!")

# Example command without prefix
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# -----------
# Web server for uptime
# -----------

async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', WEB_PORT)
    await site.start()
    print(f"Web server running on port {WEB_PORT}")

# ... (restul codului pentru rulare)
