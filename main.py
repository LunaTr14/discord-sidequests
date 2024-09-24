import discord

COMMAND_PREFIX = "/"
intents = discord.Intents.default()

def get_token() -> str:
    token_file = open("token.txt",mode="r")
    token = token_file.readline()
    token_file.close()
    return token


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')



client = MyClient(intents=intents)
client.run(get_token())