import finnhub
import time
import json
import re

companies = ["AAPL", "AMZN", "TSLA", "NVDA", "COF", "GME", "FB", "GM", "GOOG", "AMD"]
finnhub_client = finnhub.Client(api_key="c688e9aad3iagio37smg")

# Calculating time difference between now and 14 days
weekBeforeSeconds = int(round(time.time())) - 604800
currentSeconds = int(round(time.time()))
jsonString = '{'

for company in companies:
    data = finnhub_client.stock_candles(company, 'D', weekBeforeSeconds, currentSeconds)
    #print(data)

    closeData = json.dumps(data['c'])
    closeData = re.sub(r'\[', '', closeData)
    closeData = re.sub(r'\]', '', closeData)
    closeData = closeData.split(', ')

    openPriceData = json.dumps(data['o'])
    openPriceData = re.sub(r'\[', '', openPriceData)
    openPriceData = re.sub(r'\]', '', openPriceData)
    openPriceData = openPriceData.split(', ')

    volumeData = json.dumps(data['v'])
    volumeData = re.sub(r'\[', '', volumeData)
    volumeData = re.sub(r'\]', '', volumeData)
    volumeData = volumeData.split(', ')
    averageVolumeFloat = 0.0

    for i in volumeData:
        averageVolumeFloat = float(i) + averageVolumeFloat

    averageVolumeFloat = averageVolumeFloat / len(volumeData)

    difference = float(closeData[len(closeData) - 1]) - float(openPriceData[1])
    volumeDiff = float(volumeData[len(volumeData) - 1])

    # print("Last Week Open Price " + openPriceData[1])
    # print("Today Close Price " + closeData[len(closeData) - 1])
    # print("Difference: " + str(difference))
    # print(averageVolumeFloat)
    # print(volumeDiff)
    status = ""

    if volumeDiff > averageVolumeFloat and difference < 0:
        status = "Sell"
        print("Sell!")

    elif volumeDiff > averageVolumeFloat and difference > 0:
        status = "Buy"
        print("Buy!")

    else:
        status = "Stable"
        print("Stable!")

    jsonString = jsonString + '"name": ' + company + ', "openPrice": ' + str(openPriceData[1]) + ', "closePrice: "' + str(closeData[len(closeData) - 1]) + ', "avgVolume": ' + str(averageVolumeFloat) + ', "volDiff": ' + str(volumeDiff) + ', "status": ' + status