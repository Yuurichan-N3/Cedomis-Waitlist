import requests
import json
import os
from web3 import Web3
from eth_account import Account
from colorama import init, Fore, Style

# Inisialisasi colorama untuk warna di terminal
init(autoreset=True)

# Konfigurasi endpoint
BASE_URL = "https://qlphwtruuvetikksidtj.supabase.co/rest/v1/waitlist_entries"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFscGh3dHJ1dXZldGlra3NpZHRqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU0OTEyNzEsImV4cCI6MjA2MTA2NzI3MX0.gbrF5tQL6GPdjyncCL2dyDdLQO6WWQyVeXdKsm3OWb4"
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": f"Bearer {API_KEY}",
    "apikey": API_KEY,
    "content-type": "application/json",
    "origin": "https://beta.cedomis.xyz",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-client-info": "supabase-js-web/2.49.4"
}

# File untuk menyimpan wallets
WALLETS_FILE = "wallets.json"

# Inisialisasi Web3
w3 = Web3()

# Banner
BANNER = f"""
{Fore.CYAN + Style.BRIGHT}╔══════════════════════════════════════════════╗
║    🌟 CEDOMIS BOT - Waitlist Automation      ║
║   Automate generation and waitlist entry!    ║
║  Developed by: https://t.me/sentineldiscus   ║
╚══════════════════════════════════════════════╝{Style.RESET_ALL}
"""

def generate_wallet():
    """Generate wallet address dan private key baru."""
    account = Account.create()
    return {
        "address": account.address,
        "private_key": account._private_key.hex()
    }

def load_wallets():
    """Load wallets dari file wallets.json."""
    if os.path.exists(WALLETS_FILE):
        with open(WALLETS_FILE, "r") as f:
            return json.load(f)
    return []

def save_wallet(wallet_data):
    """Simpan wallet ke wallets.json."""
    wallets = load_wallets()
    wallets.append(wallet_data)
    with open(WALLETS_FILE, "w") as f:
        json.dump(wallets, f, indent=4)
    return True

def send_to_endpoint(wallet_address):
    """Kirim data ke endpoint."""
    payload = [{
        "wallet_address": wallet_address,
        "followed": True,
        "retweeted": True,
        "commented": True
    }]
    
    params = {
        "columns": '"wallet_address","followed","retweeted","commented"'
    }
    
    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload, params=params)
        if response.status_code == 201:
            print(f"{Fore.GREEN}Berhasil join waitlist untuk address: {wallet_address}{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Gagal join waitlist untuk address: {wallet_address}, Status: {response.status_code}, Response: {response.text}{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}Error saat mengirim untuk address: {wallet_address}, Error: {str(e)}{Style.RESET_ALL}")
        return False

def main():
    """Fungsi utama untuk menjalankan script."""
    print(BANNER)
    
    try:
        num_wallets = int(input(f"{Fore.YELLOW}Masukkan jumlah wallet yang ingin digenerate: {Style.RESET_ALL}"))
        if num_wallets <= 0:
            print(f"{Fore.RED}Jumlah harus lebih dari 0.{Style.RESET_ALL}")
            return
    except ValueError:
        print(f"{Fore.RED}Masukkan angka yang valid.{Style.RESET_ALL}")
        return

    for i in range(num_wallets):
        print(f"\n{Fore.CYAN}Memproses wallet {i+1}/{num_wallets}...{Style.RESET_ALL}")
        
        # Generate wallet baru
        wallet = generate_wallet()
        wallet_data = {
            "address": wallet["address"],
            "private_key": wallet["private_key"]
        }
        
        # Kirim ke endpoint
        if send_to_endpoint(wallet["address"]):
            # Simpan wallet jika berhasil
            if save_wallet(wallet_data):
                print(f"{Fore.GREEN}Wallet disimpan: {wallet['address']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Gagal menyimpan wallet: {wallet['address']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Wallet tidak disimpan karena gagal: {wallet['address']}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
