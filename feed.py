import requests
from bs4 import BeautifulSoup


async def get_patch_note(discord, message):
    info = patch_note_info()

    embed = discord.Embed(
        title=info['name'],
        url=info['link']
    )

    embed.set_image(
        url=info['img']
    )

    embed.set_author(
        name="League of Legends",
        icon_url="https://preview.redd.it/itq8rpld8va51.png?width=256&format=png&auto=webp&s=9701ba6228c29bf2d7e3dfffd45b9a3562507289"
    )

    await message.channel.send(embed=embed)


def patch_note_info():
    info = {}

    url = "https://www.leagueoflegends.com/fr-fr/news/tags/patch-notes/"

    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser")

    patch_url = "https://www.leagueoflegends.com" + soup.find("a", class_="jyxTUP")['href']
    info['name'] = soup.find("h2", class_="fEywOQ").text
    info['link'] = patch_url

    req = requests.get(patch_url)
    soup = BeautifulSoup(req.content, features="html.parser")

    info['img'] = soup.find("a", class_="cboxElement").find("img")['src']

    return info
