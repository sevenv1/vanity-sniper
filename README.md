# 🚀 Vanity Sniper
A powerful Discord vanity URL sniper written in Python that allows you to automatically claim custom vanity URLs.

## 📖 About
This tool helps you claim Discord vanity URLs by continuously monitoring and attempting to claim your desired URL when it becomes available. Built with proxy support and rate limiting protection.

## ✨ Features
- 🎯 Target specific vanity URLs
- 🔄 Automatic retries
- 📊 Status monitoring
- 🌐 Proxy support
- ⏱️ Configurable delays
- 📈 Attempt counting
- ⚡ Fast response time

## 🛠️ Installation

1. **Install required packages**
```bash
pip install requests pystyle
```

2. **Configure the script**
Edit `main.py` and set your configuration:
```python
GUILD_ID = ""          # Your guild ID
TARGET_VANITY = ""     # Target vanity URL to snipe
TOKEN = ""             # Your Discord token
MAX_ATTEMPTS = 0       # 0 for unlimited attempts
DELAY = 1             # Delay between attempts in seconds
```

## 📝 Usage

1. Run the script:
```bash
python main.py
```

2. (Optional) Add proxies to `proxies.txt`:
```
ip:port
ip:port
```

## ⚠️ Important Notes
- Requires Discord user token
- Admin permissions needed in target server
- Use responsibly and respect Discord's TOS
- Consider rate limits to avoid account flags

## 🔧 Technical Details
- Written in Python
- Uses Discord API v9
- Proxy support
- Error handling
- Progress tracking

## 🤝 Credits
Made by: sevenv1

## ⚖️ Disclaimer
This tool is for educational purposes only. Use at your own risk and responsibility.
