from webserver import keep_alive
import requests

channelID = 1067078440412520521
headers = {
    "authorization":
    MTE3NjkxNTMyODIwMzIzOTUxMA.GrS69C.PEjYLUFVaALl8n9Smc8u_Z7z2u643XkxxurHcA
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
