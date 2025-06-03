import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

RPC_USER = os.getenv("RPC_USER")
RPC_PASSWORD = os.getenv("RPC_PASSWORD")
RPC_PORT = os.getenv("RPC_PORT", 8332)
RPC_HOST = os.getenv("RPC_HOST", "127.0.0.1")

def call_rpc(method, params=[]):
    url = f"http://{RPC_HOST}:{RPC_PORT}/"
    headers = {"content-type": "application/json"}
    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(url, json=payload, headers=headers, auth=(RPC_USER, RPC_PASSWORD))
    return response.json()

def claim_reward(meditation_score, mantra_text):
    # ใช้เกณฑ์คะแนนสร้างค่าตอบแทน เช่น 0.01 BTC
    amount = round(0.0001 * meditation_score, 8)

    # สร้าง metadata สำหรับแนบคำภาวนา
    metadata = {
        "score": meditation_score,
        "mantra": mantra_text,
        "source": "kramtrangthai"
    }

    # ฝัง metadata โดยใส่ใน OP_RETURN
    hexdata = json.dumps(metadata).encode().hex()
    raw_tx = call_rpc("createrawtransaction", [[], {"data": hexdata}])["result"]

    # ใส่ค่าทิปเล็กน้อย
    funded_tx = call_rpc("fundrawtransaction", [raw_tx])["result"]["hex"]
    signed_tx = call_rpc("signrawtransactionwithwallet", [funded_tx])["result"]["hex"]
    txid = call_rpc("sendrawtransaction", [signed_tx])["result"]

    print(f"✅ ส่งเหรียญพร้อม metadata แล้ว: {txid}")

# ตัวอย่างทดสอบ
if __name__ == "__main__":
    claim_reward(meditation_score=85, mantra_text="พุทธโธ พุทธัง สรณังคัจฉามิ")