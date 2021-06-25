# https://discord.com/api/oauth2/authorize?client_id=815400066264858635&permissions=8&scope=bot
import asyncio
import discord
import requests
import json

client = discord.Client()

def soruCek(kategori=""):
    gelen = requests.get("http://127.0.0.1:8000/api/rastgele/?kategori="+kategori)
    json_data = json.loads(gelen.text)
    
    soru     = "\nSoru : {}\nCevaplar:\n".format(json_data[0]['baslik'])
    cevaplar = json_data[0]['cevap']
    sayac=1
    dogru_cevap=0

    for cevap in cevaplar:
        soru = soru + "{}) {}\n".format(sayac,cevap['cevap'])

        if(cevap['dogruMu']):
            dogru_cevap=sayac

        sayac = sayac+1
    
    return(soru,dogru_cevap)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gelenMesaj = message.content.split("_")
    if(("sorugetir" in gelenMesaj) or ("!sorugetir" in gelenMesaj)):
        if(len(gelenMesaj)>1):
            sorum = soruCek(gelenMesaj[0][1:])
            await message.channel.send(sorum[0])
        else:
            sorum = soruCek()
            await message.channel.send(sorum[0])
        
        def kontrol(m):
            return m.author == message.author and m.content.isdigit()
        
        try:
            alinan_cevap = await client.wait_for('message', check=kontrol, timeout=3)
        except asyncio.TimeoutError:
            return await message.channel.send('Üzgünüm, cevap vermen çok uzun sürdü!')

        if(int(alinan_cevap.content) == sorum[1]):
            await message.channel.send("Cevabın doğru!")
        else:
            await message.channel.send("Yanlış cevap :(")

client.run('ODE1NDAwMDY2MjY0ODU4NjM1.YDr2fQ.13pVrsVWlXrTNCQqhD3SI8HFkYQ')