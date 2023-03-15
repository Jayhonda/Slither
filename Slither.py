"""
    Slither Discord bot

    The skeleton of this project

    Base code developed and commented by Jhon Tabio (@Jayhonda)
"""
import discord

class Slither(discord.Client):
    def __init__(self, prefix, current_game, *args, **kwargs):
        super().__init__(intents=discord.Intents.all(), *args, **kwargs)

        self.current_game = current_game
        self.prefix = prefix

    # Fires when the discord client is initialized and ready to accept commands
    async def on_ready(self):
        print(f"Logged in as {self.user}!")

        await self.change_presence(status=discord.Status.dnd, activity=self.current_game)
    
    # Fires when the discord client is uninitialized
    async def close(self):
        print(f"Logging off from {self.user}!")
        print("All done!")
    
    # Fires when a member in a guild has a status update event
    async def on_member_update(self, before, after):
        if str(after.status) != "offline" and str(before.status) == "offline":
            print(f"{after.name} has gone from {before.status} to {after.status}")
        
        elif str(after.status) == "offline" and str(before.status) != "offline":
            print(f"{after.name} has gone from {before.status} to {after.status}")

# Ensure that we instatiate our client only if we call upon this file directly
if __name__ == "__main__":
    # Set our client to respond to commands with the prefix of 'u!' and a status of 'Playing for self development'
    client = Slither("u!", discord.Game(name="for self development"))

    client_secret = None

    # Revealing the client secret token is dangerous,
    # not only in groups, but uploading it to the internet.
    # We will not upload it on the internet, merely access it
    # directly on file so it is in one location. (Better method as project grows)
    with open("Project_Fluff\client_secret.txt") as secret:
        client_secret = secret.read()

    client.run(client_secret)