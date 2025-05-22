import requests
import json
import subprocess
import re

# 設定
url = "https://xxx/api/detect/"
api_key = "xxx"

def get_mac_addresses():
    try:
        # arpコマンドの出力を取得
        output = subprocess.check_output(['arp', '-n'], encoding='utf-8')
        
        # 正規表現でMACアドレスを抽出（xx:xx:xx:xx:xx:xx）
        mac_addresses = re.findall(r'..:..:..:..:..:..', output)
        
        # 重複除去してソート（必要なら）
        mac_addresses = sorted(set(mac_addresses))
        
        return mac_addresses

    except subprocess.CalledProcessError as e:
        print("ARPコマンドの実行に失敗しました:", e)
        return []

mac_addresses = get_mac_addresses()

# ヘッダー
headers = {
    "X-API-Key": api_key,
    "Content-Type": "application/json"
}

# 本文
payload = {
    "mac_addresses": mac_addresses
}

# リクエスト送信
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 結果表示
print(f"Status Code: {response.status_code}")
print("Response Body:", response.text)
