import requests
from discord import SyncWebhook
import time

webhookUrl = ""


while True:
    time.sleep(10)
    x = requests.get('https://www.apple.com/ca/shop/fulfillment-messages?pl=true&mts.0=regular&mts.1=compact&parts.0=MQ013VC/A&location=j9h%203v7')

    x = x.json()

    for store in x["body"]["content"]["pickupMessage"]["stores"]:
        if store["partsAvailability"]["MQ013VC/A"]["pickupDisplay"] != "unavailable":
            webhook = SyncWebhook.from_url(webhookUrl)
            webhook.send(store["storeName"] + " SILVER")
