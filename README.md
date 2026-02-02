# 🎬 CineFlix Bot - Telegram Content Distribution System

A professional, production-ready Telegram bot for content distribution with force join, duplicate prevention, and Mini App integration.

## 🌟 Key Features

- **Smart Content Delivery**: Automatic video and link distribution
- **Force Join System**: Multi-channel membership verification
- **Duplicate Prevention**: Ensures users receive only latest requests
- **Admin Panel**: Comprehensive management dashboard
- **Mini App Integration**: Seamless user experience
- **MongoDB Storage**: Persistent, reliable data storage
- **Protected Content**: Videos can't be forwarded
- **Production Ready**: Zero hardcoded credentials - completely secure!

---

## 🔒 Security First

**⚠️ CRITICAL: This bot has NO hardcoded credentials!**

All sensitive information must be provided through:
- `.env` file for local development
- Environment variables for production deployment

**NEVER commit `.env` file to Git or share it publicly!**

---

## 🚀 Quick Start

### Installation

```bash
# 1. Clone repository
git clone <your-repo-url>
cd telegram-bot-project-final

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env and fill in YOUR credentials

# 4. Run bot
python main.py
```

---

## 📋 Required Configuration

Create `.env` file with these variables:

```bash
BOT_TOKEN=              # From @BotFather
API_ID=                 # From https://my.telegram.org/apps
API_HASH=               # From https://my.telegram.org/apps
ADMIN_ID=               # From @userinfobot
CONTENT_CHANNEL_ID=     # Your content channel (negative number)
FORCE_JOIN_CHANNEL_ID=  # Your force join channel (negative number)
CHANNEL_USERNAME=       # Format: @YourChannel
MONGODB_URI=            # From https://cloud.mongodb.com
```

See `.env.example` for detailed instructions.

---

## 🚀 Deployment

### Railway (Recommended)

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git push

# 2. Deploy on Railway
- Connect GitHub repo
- Add environment variables
- Deploy automatically!
```

### Environment Variables Setup
Add ALL variables from `.env` to Railway/Render dashboard.

**See `DEPLOYMENT_GUIDE.md` for complete instructions!**

---

## 📖 Bot Commands

**Admin Commands:**
```
/start    - Welcome message
/admin    - Admin panel
/stats    - Statistics
/test     - Test system
```

---

## 🔐 Security Features

✅ **Zero Hardcoded Credentials**  
✅ **Environment Variable Validation**  
✅ **Protected Content (No Forwarding)**  
✅ **Secure Admin Access**  
✅ **Git-Safe (.env in .gitignore)**  

---

## 📚 Documentation

- `DEPLOYMENT_GUIDE.md` - Detailed deployment steps
- `SETUP.md` - Setup guide (Bangla)
- `.env.example` - Configuration template

---

## 🐛 Troubleshooting

**Bot not starting?**
- Check all environment variables are set
- Verify bot token is valid
- Check MongoDB connection

**Force join not working?**
- Bot must be admin in channels
- Channel IDs must be negative
- Bot needs "Invite Users" permission

See `DEPLOYMENT_GUIDE.md` for more solutions.

---

## ✅ Pre-Deployment Checklist

- [ ] All environment variables configured
- [ ] `.env` in `.gitignore`
- [ ] No credentials in code
- [ ] Bot tested locally
- [ ] Channels setup properly
- [ ] MongoDB connected

---

**Version:** 1.0.0 (Secure - No Hardcoded Credentials)  
**Status:** ✅ Production Ready  
**Security:** 🔒 100% Environment Variables

**Deploy safely! 🚀**
