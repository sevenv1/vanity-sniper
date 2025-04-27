try:
    import requests
    import time
    import random
    from pystyle import *
except ImportError:
    import os
    os.system("pip install requests pystyle")

"""
Configuration Variables:
    GUILD_ID (str): The Discord server/guild ID where you want to set the vanity URL
    TARGET_VANITY (str): The desired vanity URL you want to claim (e.g., 'discord' for discord.gg/discord)
    TOKEN (str): Your Discord authentication token (ur account token, not a bot token)
    MAX_ATTEMPTS (int): Maximum number of attempts to claim the vanity URL (0 for unlimited)
    DELAY (float): Base delay in seconds between each attempt
"""
GUILD_ID = ""
TARGET_VANITY = "discord"
TOKEN = ""
MAX_ATTEMPTS = 0
DELAY = 1

def loadProxies():
    try:
        with open("proxies.txt", "r") as f:
            return [p.strip() for p in f.readlines() if p.strip()]
    except FileNotFoundError:
        print("proxies.txt not found. Running without proxies...")
        return []

def snipeVanity():
    url = f"https://discord.com/api/v9/guilds/{GUILD_ID}/vanity-url"
    proxies = loadProxies()
    
    headers = {
        "authority": "discord.com",
        "method": "PATCH",
        "path": f"/api/v9/guilds/{GUILD_ID}/vanity-url",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US",
        "authorization": TOKEN,
        "content-type": "application/json",
        "origin": "https://discord.com",
        "priority": "u=1, i",
        "referer": f"https://discord.com/channels/{GUILD_ID}",
        "sec-ch-ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.191 Safari/537.36",
        "x-discord-locale": "en-US"
    }
    
    System.Clear()
    System.Title("Vanity Sniper made by sevenv1")
    attemptCount = 0
    
    print(f"Starting sniper for vanity: {TARGET_VANITY}")
    print(f"Loaded {len(proxies)} proxies" if proxies else "Running without proxies")
    print("-" * 50)
    
    while MAX_ATTEMPTS == 0 or attemptCount < MAX_ATTEMPTS:
        try:
            timestamp = time.strftime("%H:%M:%S", time.localtime())
            data = {"code": TARGET_VANITY}
            currentProxy = random.choice(proxies) if proxies else None
            proxyDict = {"http": f"http://{currentProxy}", "https": f"http://{currentProxy}"} if currentProxy else None
            
            response = requests.patch(url, headers=headers, json=data, proxies=proxyDict, timeout=5)
            attemptCount += 1
            
            if response.status_code == 200:
                print(f"\n[{timestamp}] ✅ SUCCESS! Claimed vanity: {TARGET_VANITY}")
                return True
            
            proxyInfo = f" - Proxy: {currentProxy}" if currentProxy else ""
            print(f"\r[{timestamp}] Attempt #{attemptCount} - Status: {response.status_code} - Target: {TARGET_VANITY}{proxyInfo}", end="")
            
            jitter = random.uniform(0.3, 1)
            time.sleep(DELAY + jitter)
            
        except KeyboardInterrupt:
            print("\n\ncancelled by user.")
            return False
        except (requests.exceptions.ProxyError, requests.exceptions.ConnectTimeout):
            print(f"\n[{timestamp}] Proxy error, retrying with different proxy...")
            continue
        except Exception as e:
            print(f"\n[{timestamp}] Error occurred: {str(e)}")
            time.sleep(DELAY)
    
    print("\n\nmaximum attempts reached. sniper stopped.")
    return False

if __name__ == "__main__":
    snipeVanity()