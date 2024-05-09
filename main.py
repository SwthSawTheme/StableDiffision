import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"sk-x5JCH3P99U4FO0tKBxmXgqd4ipHv3HDcSYXpBqizOqeTdtcD",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "an extremely detailed and extremely diabolical vampire lord in front of a French Renaissance medieval castle, on a dark night with a red moon, ultra realistic, in high definition, ultra colorin",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./batman.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))