import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"sk-x5JCH3P99U4FO0tKBxmXgqd4ipHv3HDcSYXpBqizOqeTdtcD",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Sekiro Shadow Die Twice dressed as Batman, ultra realistic, ultra detailed amid intense red rain, red details on the clothes and on the cover. Demonic and vampiric look, ultra coloring and RGB, ultra particles, lots and lots of particles on the screen, in high definition, ultra reality, fire particles, smoke effects, ultra cinematics, rising particle effects, ancient, ultra detailed particles, mesh ultra detailed",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./batman.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))