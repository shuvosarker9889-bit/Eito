# 🚀 Deployment Guide - CineFlix Bot

## 📋 Overview

এই guide আপনাকে দেখাবে কিভাবে আপনার bot deploy করবেন **কোনো credential public না করে**।

---

## ⚠️ IMPORTANT SECURITY RULES

### ✅ DO:
- সব credentials `.env` file এ রাখুন
- `.env` file কখনো Git এ commit করবেন না
- Deployment platform এ environment variables manually add করুন
- Strong passwords use করুন

### ❌ DON'T:
- কোনো file এ hardcoded credentials রাখবেন না
- `.env` file public share করবেন না
- Bot token কারো সাথে share করবেন না
- Same password multiple জায়গায় use করবেন না

---

## 🔧 Step 1: Get Your Credentials

### 1. Bot Token
```
1. Telegram এ @BotFather open করুন
2. Send: /newbot
3. Bot এর name ও username দিন
4. Token copy করুন (Format: 123456789:ABCdefGHI...)
```

### 2. API ID & API Hash
```
1. https://my.telegram.org/apps এ যান
2. Login করুন
3. Create new application
4. API ID (numeric) এবং API Hash copy করুন
```

### 3. Admin ID
```
1. Telegram এ @userinfobot open করুন
2. /start send করুন
3. আপনার User ID copy করুন (numeric)
```

### 4. Channel IDs
```
1. আপনার channels create করুন (Content ও Force Join)
2. Bot কে উভয় channel এ Admin বানান
3. @username_to_id_bot use করে channel IDs পান
4. Format: -1001234567890 (must be negative)
```

### 5. MongoDB URI
```
1. https://cloud.mongodb.com এ যান
2. Free cluster create করুন
3. Database user create করুন
4. Connection string copy করুন
5. Format: mongodb+srv://username:password@cluster.mongodb.net/
```

---

## 🏠 Step 2: Local Setup (Testing)

### Install Dependencies
```bash
# Clone/Download project
cd telegram-bot-project-final

# Install Python packages
pip install -r requirements.txt
```

### Configure Environment
```bash
# Copy template
cp .env.example .env

# Edit .env file
nano .env  # or use any text editor
```

### Fill in .env file:
```bash
BOT_TOKEN=your_bot_token_from_botfather
API_ID=your_api_id_from_my_telegram_org
API_HASH=your_api_hash_from_my_telegram_org
ADMIN_ID=your_user_id_from_userinfobot
CONTENT_CHANNEL_ID=-1001234567890
FORCE_JOIN_CHANNEL_ID=-1001234567890
CHANNEL_USERNAME=@YourChannelName
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/
DATABASE_NAME=cineflix_bot
ENABLE_NOTIFICATIONS=Yes
LOG_LEVEL=INFO
```

### Test Locally
```bash
python main.py
```

যদি সব ঠিক থাকে, আপনি দেখবেন:
```
✅ Configuration Loaded Successfully
🤖 Bot Configuration:
   ✓ Bot Token: ********************...
   ✓ Admin ID: 123456789
   ...
Ready to start! 🚀
```

---

## ☁️ Step 3: Deploy to Railway

### Method 1: GitHub (Recommended)

#### 1. Push to GitHub
```bash
# Initialize git (if not already)
git init

# Add files
git add .

# Check that .env is NOT staged
git status
# You should see: .env (untracked) - this is CORRECT!

# Commit
git commit -m "Initial commit - Bot ready for deployment"

# Add remote and push
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

#### 2. Deploy on Railway
```
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will detect Python and use Procfile automatically
```

#### 3. Add Environment Variables
```
1. In Railway dashboard, go to your project
2. Click on "Variables" tab
3. Add ALL these variables ONE BY ONE:

   BOT_TOKEN          → your_bot_token
   API_ID             → your_api_id
   API_HASH           → your_api_hash
   ADMIN_ID           → your_user_id
   CONTENT_CHANNEL_ID → -1001234567890
   FORCE_JOIN_CHANNEL_ID → -1001234567890
   CHANNEL_USERNAME   → @YourChannel
   MONGODB_URI        → mongodb+srv://...
   DATABASE_NAME      → cineflix_bot
   ENABLE_NOTIFICATIONS → Yes
   LOG_LEVEL          → INFO
```

#### 4. Deploy
```
Railway will automatically deploy after you add variables
Check logs to verify bot started successfully
```

### Method 2: Direct Upload

```
1. Zip the project (make sure .env is NOT included!)
2. Go to Railway → New Project → Empty Project
3. Add environment variables (same as above)
4. Upload your zip file
5. Deploy!
```

---

## 🎨 Step 4: Deploy to Render

### 1. Create Web Service
```
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repo OR upload code
```

### 2. Configure Service
```
Name: cineflix-bot
Environment: Python
Build Command: pip install -r requirements.txt
Start Command: bash start.sh
```

### 3. Add Environment Variables
```
Go to "Environment" tab and add ALL variables:

BOT_TOKEN          → your_bot_token
API_ID             → your_api_id
API_HASH           → your_api_hash
ADMIN_ID           → your_user_id
CONTENT_CHANNEL_ID → -1001234567890
FORCE_JOIN_CHANNEL_ID → -1001234567890
CHANNEL_USERNAME   → @YourChannel
MONGODB_URI        → mongodb+srv://...
DATABASE_NAME      → cineflix_bot
ENABLE_NOTIFICATIONS → Yes
LOG_LEVEL          → INFO
```

### 4. Deploy
```
Click "Create Web Service"
Wait for deployment to complete
Check logs for success message
```

---

## 🔍 Step 5: Verify Deployment

### Test Commands
```
1. Open Telegram and find your bot
2. Send: /start
   - You should see welcome message

3. Send: /admin
   - Admin panel should appear (only for you)

4. Send: /stats
   - Statistics should be displayed
```

### Check Logs
```
Railway: View → Logs
Render: Logs tab

Look for:
✅ Configuration Loaded Successfully
✅ Bot started successfully
✅ MongoDB connected
```

---

## 🐛 Troubleshooting

### Bot Not Starting
**Check:**
- All environment variables are set correctly
- Bot token is valid and not revoked
- MongoDB connection string is correct

**Solution:**
```bash
# View logs
railway logs  # or check Render logs

# Common issues:
- Missing environment variables
- Invalid channel IDs (must be negative)
- MongoDB connection failed
- Bot token revoked
```

### Configuration Error
```
If you see:
"Missing required environment variables"

Action:
1. Check which variables are missing in the error message
2. Add them in Railway/Render dashboard
3. Redeploy
```

### MongoDB Connection Failed
```
If you see:
"Failed to connect to MongoDB"

Action:
1. Check MongoDB Atlas is running
2. Verify connection string is correct
3. Check IP whitelist (allow all: 0.0.0.0/0)
4. Verify database user credentials
```

### Bot Added to Channel But Can't Post
```
Action:
1. Make sure bot is Admin in BOTH channels
2. Bot needs "Post Messages" permission in content channel
3. Bot needs "Invite Users" permission in force join channel
```

---

## 📊 Monitoring

### Daily Checks
```bash
# Check bot status
/stats   # in Telegram

# View logs
Railway: Dashboard → Logs
Render: Logs tab
```

### Weekly Tasks
```
- Review bot statistics
- Check MongoDB storage usage (Free tier: 512MB)
- Monitor Railway credits (Free tier: $5/month)
- Clear old logs if needed
```

---

## 🔄 Updating Bot

### Update Code
```bash
# Make changes locally
# Test locally first!
python main.py

# Push to GitHub
git add .
git commit -m "Update: description of changes"
git push

# Railway/Render will auto-deploy
```

### Update Environment Variables
```
1. Go to platform dashboard
2. Variables/Environment tab
3. Edit or add new variables
4. Service will restart automatically
```

---

## 🔐 Security Best Practices

### Regular Maintenance
```
✅ Rotate bot token every 6 months
✅ Change MongoDB password periodically  
✅ Review bot access logs regularly
✅ Monitor unusual activity
✅ Keep dependencies updated
```

### Backup Strategy
```
✅ Export MongoDB data monthly
✅ Keep copy of .env file securely (offline)
✅ Document your channel IDs
✅ Backup your bot configuration
```

---

## 📞 Getting Help

### Common Issues
Check `TROUBLESHOOTING.md` for solutions

### Logs Location
- **Local:** Terminal output
- **Railway:** Dashboard → Logs
- **Render:** Service → Logs tab

### Documentation
- `README.md` - Project overview
- `SETUP.md` - Detailed setup (Bangla)
- `.env.example` - Configuration template

---

## ✅ Deployment Checklist

Before going live:

- [ ] All environment variables configured
- [ ] Bot token valid and active
- [ ] MongoDB connected successfully
- [ ] Bot is admin in both channels
- [ ] Force join working correctly
- [ ] Content delivery tested
- [ ] Admin commands working
- [ ] Logs showing no errors

---

## 🎉 Success!

যদি সব ঠিক থাকে, আপনার bot এখন live! 🚀

### Next Steps:
1. Configure your Mini App
2. Add content to content channel
3. Share Mini App link with users
4. Monitor bot performance

---

**Remember: NEVER share your .env file or credentials publicly!**

**Deploy Date:** Fill in when deployed
**Bot Status:** ✅ Live / 🔧 Testing / ❌ Down
**Platform:** Railway / Render / Other

---
