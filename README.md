# 𝗔𝗟𝗣𝗛𝗔 𝗦𝗣𝗔𝗠

<h1 align="center">🚩🚩 जय बजरंग बली 🚩🚩</h1>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://readme-typing-svg.herokuapp.com?color=FF0085&width=620&lines=🍁+🚩+𝗣𝗢𝗪𝗘𝗥𝗘𝗗+𝗕𝗬+𝗥𝗔𝗨𝗦𝗛𝗔𝗡+𝗞𝗜𝗡𝗚+𝗔𝗥𝗔+🚩+🍁">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<h1 align="center"><b>𝐓ᴇᴀᴍ 𝐏ᴜʀᴠɪ 𝐁ᴏᴛs</b></h1>
<p align="center"><a href="https://t.me/ll_ALPHA_BABY_lll"><img src="https://files.catbox.moe/ikxjd1.jpg" width="500"></a></p>

---

## 🚀 **Deploy Guide / Deploy Kaise Kare (VPS, Heroku, Docker)**

Bot ko error-free deploy karne ke liye niche me diye gaye steps follow karein.

---

### 1️⃣ **VPS Deployment Guide (Ubuntu / Debian / Linux)**

VPS par deploy karne ke liye niche diye gaye commands run karein:

```bash
# System packages update aur required tools install karein
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git -y

# Repository clone karein
git clone https://github.com/TEAMPURVI/ALPHA_SPAM.git
cd ALPHA_SPAM

# Virtual Environment (venv) create aur activate karein
python3 -m venv venv
source venv/bin/activate

# Dependencies install karein
pip install -r requirements.txt
```

#### **Environment Variables Set Karein (VPS par):**
Aap terminal me export kar sakte hain ya environment set kar sakte hain:

```bash
export API_ID="your_api_id"
export API_HASH="your_api_hash"
export BOT_TOKEN="your_bot_token"
export OWNER_ID="your_telegram_id"
export SUDO_USERS="your_sudo_user_ids"
export CMD_HNDLR="."
```

#### **Bot Run Karein:**

Direct run karne ke liye:
```bash
python3 main.py
```

Background me 24/7 run karne ke liye:
```bash
tmux new -s alpha_bot
python3 main.py
# Press Ctrl+B then D to detach
```

---

### 2️⃣ **Heroku Deployment**

Heroku par deploy karne ke liye niche Button par click karein:

<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https://github.com/TEAMPURVI/ALPHA_SPAM">
    <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-green?style=for-the-badge&logo=heroku" width="220" height="38.45"/>
  </a>
</p>

#### **Heroku Environment Variables (Config Vars):**
- `API_ID`: Aapka Telegram API ID
- `API_HASH`: Aapka Telegram API HASH
- `BOT_TOKEN`: Bot 1 Token (Master Bot)
- `BOT_TOKEN2` to `BOT_TOKEN10`: (Optional) Extra bot tokens
- `OWNER_ID`: Aapka Telegram User ID
- `SUDO_USERS`: Space-separated Telegram user IDs
- `CMD_HNDLR`: Command Handler Symbol (e.g. `.`)

---

### 3️⃣ **Docker Deployment**

Docker se deploy karne ke liye:

```bash
docker build -t alpha-spam .
docker run -d --name alpha_spam   -e API_ID="your_api_id"   -e API_HASH="your_api_hash"   -e BOT_TOKEN="your_bot_token"   -e OWNER_ID="your_owner_id"   alpha-spam
```

---

## 🛠️ **Troubleshooting & Fixes**

- **Error: `sqlite3.OperationalError: database is locked`**
  - **Reason:** Telethon by default SQLite `.session` files use karta hai, multiple instances execution ya concurrent locks se db locked error aata tha.
  - **Solution:** Ab codebase updated hai aur `MemorySession()` use kar raha hai jisse SQLite database locking ki koi problem nahi aayegi.

---

<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
  <a href="https://t.me/PURVI_SUPPORT"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
  <a href="https://t.me/PURVI_UPDATES"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

- <b>Special Thanks to [THE PURVI MUSIC™](https://github.com/TEAMPURVI) for [THE PURVI MUSIC™](https://github.com/TEAMPURVI/PURVI_MUSIC)</b>
