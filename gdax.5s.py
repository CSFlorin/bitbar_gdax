#!/Users/f/Documents/BitBar/gdax/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>GDAX Trade Prices</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Florin Langer</bitbar.author>
# <bitbar.author.github>CSFlorin</bitbar.author.github>
# <bitbar.desc>Get latest trade prices (in USD) for BTC, LTC, ETH, and BCH on the GDAX exchange. Just change the first line in gdax.5s.py to match your BitBar plugins folder (e.g., #!/Users/<your username>/Documents/BitBar/gdax/bin/python).</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>Python 3 (gdax)</bitbar.dependencies>
# <bitbar.abouturl>http://csflorin.github.io/</bitbar.abouturl>

try:
    import gdax
except ImportError:
    import pip
    if __name__ == "__main__":
        pip.main(["install", "gdax"])

import json, os, sys

if __name__ == "__main__":
    btc_img = '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'
    ltc_img = 'iVBORw0KGgoAAAANSUhEUgAAAEMAAABDCAYAAADHyrhzAAAACXBIWXMAABcRAAAXEQHKJvM/AAAEK0lEQVR42t2cMU7jQBSGfyynMBIkCkUaJEhJRSQOgNNOQ/YE5AjmBtkTkL2B9wQbmmljJA4QcgKQTEEBSty4oGCLvLBe4yTjZGY89pMiFDQ45sv//jfzbM/e5+cndATn/BTAKQAXQANAZ8XQGYDJ8idjLICm2FMFg3PeANCjf94FcLLD4R4BBABGKuFIh8E57wHoA7hSdM5zAD6AIWPsyUgYnPM+gMGOCsgbdwQlMAIGKWGoGUIWFG9XpWwNgwxxqDAdtomfjLGBVhikBh9AHebFI4DeNiqxtgDhA/hjKAgAOAcwoS9MjTKoVI4AXKI8ccMYG0qFQSACol62+M0Y60tJk5KDAIBrSm0pnlFmEEkg3k4wiGjZQSzjdpOpWmtAeACuUa3wOeedXDDoD25RvajT/CiXMnxUN8455wOh0krpcYvqRzs9S7UzyuhA5RnUajUcHh5uHBdFET4+PlSeypD6LdkwAHiqp9nNZhMXFxcbxz08PKiGccU5d5PLfyulCk+1No+OjoTGRVGkI1W8VQaqXBUAhFLk/f1dl29cUSviG4y+jk9vNpsbx7y9vek0Uu8/GJxzFxo6VYalyDJ6aWX0TFFFATBOSAx6YYgoI45jxHGse87RAwCLDERLM1d0flFAfCnD1QXCtm1TYZwvYXRMSRHNZTW9DHG1wTg4ODDRPJPRsbC4GGyEMqIogm3baLfb6Ha7wmqSFA1bh3k6jgPHcYR8pdvtFjX56lg6PkWkihiQLg3LlBQxwUi1wBCdeRZtpLYOv8iTJmEY4uXlRbdfqIXRarVwfHyMVqslNP719RXT6VR1Q0c/DMdxhLpZaY8oEoQyzyhJ9UjHxAJwb0L1KMIjUjGzADwVrQwDVAEAgYXFPZfSYYRhiDAMywTjSQmM8XiM6XSK/f19o1eqiXhmjD3ZjLGAcz6HxM74siqIpkutVtvKZyReaAqSpTWA5Lv2RJs5AHB2drbVZ0i80BQkS+vIhIqSJ+I4luk1ozSMucyTFW3mbBsSS/EdY2z2BYPejMqkDImm62fNQIeyji7azDFAGc+MsdE3GIyxiazZqA6/kHRtZbBuoTYAMDZMxipV4Sd/kXXnjo/q3diWFT+SKbJq1erJriwGxn0aRCYMqiyDCoOYY8XtF5n9DLr5/K6iMPqrHr9Y19zpY/HsRpXiV1Z6rDTQlJl2aN5er4hPuOsGrG370dzDrYChPkLgHpSNPdAKAHkE4C7XHzvBKDkQYRAbPWOFh/gox2MXwk8g5VJGhkJML7s3eUHkVkZKJR5NzuqGpUWfvjRog0FAGrT0L3otMwcwyPOkonQYCSguqeSyAAhDLJ6Hn+16MKm7JJDBelTTVabPM/7tlDCTdVAl+2ck9s5Y7p9RlwRgBIV7aOzp2FmF0qhDr1OBdHrG4rLnhF6B7L0ysuIvj1TMyRRB0HMAAAAASUVORK5CYII='
    eth_img = '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'
    bch_img = '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'

    public_client = gdax.PublicClient()

    # Print price with 2 decimal places
    path = os.path.dirname(sys.argv[0])
    product = json.load(open(path + '/gdax/gdax_settings.json'))['product']
    price = None
    try:
        price = float(public_client.get_product_ticker(product)["price"])
        print("$" + str(int(price)) + str(round(price - int(price), 2))[1:].ljust(3, "0") + " | image=" + eval(product[0:3].lower() + '_img'))
    except KeyError:
        print("N/A | image=" + eval(product[0:3].lower() + '_img'))

    print("---")

    if price:
        # Print 24-hour percent increase/decrease
        open_price = float(public_client.get_product_24hr_stats(product)["open"])
        percent_dec = round(((open_price-price)/open_price)*100, 2)
        if (percent_dec > 0):
            print("-" + str(percent_dec) + "% | color=red")
        else:
            print("+" + str(-percent_dec) + "% | color=green")

    print("Change Coin | bash=\"" + path + "/gdax/Change Coin.sh\" terminal=false refresh=true")

    print("Open GDAX | href='https://gdax.com'")