## send message to discord server

import requests


def main():
    data = {
        "content": "Hello, this is a webhook message!",
        "username": "MyWebhookBot",
        "avatar_url": "https://example.com/avatar.png",
        "embeds": [
            {
                "title": "Embed Title",
                "description": "This is an embedded message.",
                "color": 16711680  # RGB color value
            }
        ]
    }
    requests.post(URL, json=data)
    pass


if __name__ == '__main__':
    URL = r'https://discordapp.com/api/webhooks/1086417159044993085/hZXin2pqdpa7DmCKQ6s7nlzQW3y4rCJ9YRzvH5a2BW7KKA1WWZDrMsXHnm_imRAqe3jW'
    main()