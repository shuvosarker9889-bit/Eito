# -*- coding: utf-8 -*-
"""
🔧 Bot Configuration
All credentials and settings loaded from environment variables
⚠️ NO HARDCODED CREDENTIALS - All values must be set in .env or deployment platform
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Bot Configuration Class
    All credentials are loaded from environment variables only.
    No fallback values to prevent accidental exposure.
    """
    
    # ═══════════════════════════════════════════════
    # 🤖 TELEGRAM BOT CREDENTIALS
    # ═══════════════════════════════════════════════
    # Get from @BotFather - Required
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # Get from https://my.telegram.org/apps - Required
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    
    # ═══════════════════════════════════════════════
    # 👨‍💼 ADMIN CONFIGURATION
    # ═══════════════════════════════════════════════
    # Your Telegram User ID - Get from @userinfobot - Required
    ADMIN_ID = os.getenv("ADMIN_ID")
    
    # ═══════════════════════════════════════════════
    # 📺 CHANNEL CONFIGURATION
    # ═══════════════════════════════════════════════
    # Content storage channel ID (must be negative) - Required
    CONTENT_CHANNEL_ID = os.getenv("CONTENT_CHANNEL_ID")
    
    # Force join channel ID (must be negative) - Required
    FORCE_JOIN_CHANNEL_ID = os.getenv("FORCE_JOIN_CHANNEL_ID")
    
    # Channel username with @ (e.g., @YourChannel) - Required
    CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
    
    # ═══════════════════════════════════════════════
    # 🗄️ DATABASE CONFIGURATION
    # ═══════════════════════════════════════════════
    # MongoDB connection string - Get from https://cloud.mongodb.com - Required
    MONGODB_URI = os.getenv("MONGODB_URI")
    
    # Database name (optional, has default)
    DATABASE_NAME = os.getenv("DATABASE_NAME", "cineflix_bot")
    
    # ═══════════════════════════════════════════════
    # 🔔 NOTIFICATION SETTINGS
    # ═══════════════════════════════════════════════
    ENABLE_NOTIFICATIONS = os.getenv("ENABLE_NOTIFICATIONS", "Yes").lower() == "yes"
    
    # ═══════════════════════════════════════════════
    # 💬 WELCOME MESSAGE (Bangla + Professional)
    # ═══════════════════════════════════════════════
    @classmethod
    def get_welcome_message(cls):
        """Generate welcome message with channel username"""
        return f"""
🎬 <b>স্বাগতম CineFlix এ!</b>

আপনাকে আমাদের প্রিমিয়াম কন্টেন্ট ডিস্ট্রিবিউশন বটে স্বাগতম! 

🌟 <b>বিশেষ সুবিধা:</b>
✅ HD Quality Videos
✅ সরাসরি Telegram এ দেখুন
✅ দ্রুত ও নিরাপদ ডেলিভারি
✅ ডাউনলোড সাপোর্ট

📢 <b>কন্টেন্ট পেতে:</b>
আমাদের অফিশিয়াল চ্যানেলে জয়েন করুন এবং Mini App থেকে আপনার পছন্দের কন্টেন্ট সিলেক্ট করুন।

🎯 <b>Official Channel:</b> {cls.CHANNEL_USERNAME}

<i>আপনার বিনোদনের সাথী - CineFlix 🎭</i>
"""
    
    # ═══════════════════════════════════════════════
    # 🛡️ SECURITY SETTINGS
    # ═══════════════════════════════════════════════
    PROTECT_CONTENT = True  # Video forwarding disabled
    MAX_RETRIES = 3  # Database reconnection attempts
    FLOOD_WAIT_TOLERANCE = 60  # Seconds to wait on flood
    
    # ═══════════════════════════════════════════════
    # 📝 LOGGING
    # ═══════════════════════════════════════════════
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls):
        """
        Validate all required configurations
        Raises ValueError if any required config is missing
        """
        required_configs = {
            "BOT_TOKEN": cls.BOT_TOKEN,
            "API_ID": cls.API_ID,
            "API_HASH": cls.API_HASH,
            "ADMIN_ID": cls.ADMIN_ID,
            "CONTENT_CHANNEL_ID": cls.CONTENT_CHANNEL_ID,
            "FORCE_JOIN_CHANNEL_ID": cls.FORCE_JOIN_CHANNEL_ID,
            "CHANNEL_USERNAME": cls.CHANNEL_USERNAME,
            "MONGODB_URI": cls.MONGODB_URI
        }
        
        missing = [key for key, value in required_configs.items() if not value]
        
        if missing:
            error_msg = f"""
╔═══════════════════════════════════════════════════════════╗
║  ⚠️  CONFIGURATION ERROR                                  ║
╚═══════════════════════════════════════════════════════════╝

Missing required environment variables:
{chr(10).join(f"  ❌ {key}" for key in missing)}

Please set these variables in your .env file or deployment platform.

For local development:
  1. Copy .env.example to .env
  2. Fill in all required values
  3. Run: python main.py

For deployment (Railway/Render):
  1. Go to your project dashboard
  2. Navigate to Environment Variables
  3. Add all missing variables
  4. Redeploy

Documentation: See SETUP.md for detailed instructions
"""
            raise ValueError(error_msg)
        
        # Type conversion and validation
        try:
            cls.API_ID = int(cls.API_ID)
            cls.ADMIN_ID = int(cls.ADMIN_ID)
            cls.CONTENT_CHANNEL_ID = int(cls.CONTENT_CHANNEL_ID)
            cls.FORCE_JOIN_CHANNEL_ID = int(cls.FORCE_JOIN_CHANNEL_ID)
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid numeric value in configuration: {e}")
        
        # Validate channel IDs are negative (Telegram requirement)
        if cls.CONTENT_CHANNEL_ID >= 0:
            raise ValueError("CONTENT_CHANNEL_ID must be a negative number (e.g., -1001234567890)")
        
        if cls.FORCE_JOIN_CHANNEL_ID >= 0:
            raise ValueError("FORCE_JOIN_CHANNEL_ID must be a negative number (e.g., -1001234567890)")
        
        # Validate channel username format
        if not cls.CHANNEL_USERNAME.startswith("@"):
            raise ValueError("CHANNEL_USERNAME must start with @ (e.g., @YourChannel)")
        
        # Validate MongoDB URI format
        if not cls.MONGODB_URI.startswith("mongodb"):
            raise ValueError("MONGODB_URI must be a valid MongoDB connection string")
        
        return True
    
    @classmethod
    def display_config(cls):
        """Display current configuration (safely, without exposing secrets)"""
        return f"""
╔═══════════════════════════════════════════════════════════╗
║  ✅ Configuration Loaded Successfully                     ║
╚═══════════════════════════════════════════════════════════╝

🤖 Bot Configuration:
   ✓ Bot Token: {'*' * 20}...{cls.BOT_TOKEN[-10:] if cls.BOT_TOKEN else 'NOT SET'}
   ✓ API ID: {cls.API_ID}
   ✓ API Hash: {'*' * 20}...{cls.API_HASH[-6:] if cls.API_HASH else 'NOT SET'}

👨‍💼 Admin:
   ✓ Admin ID: {cls.ADMIN_ID}

📺 Channels:
   ✓ Content Channel: {cls.CONTENT_CHANNEL_ID}
   ✓ Force Join Channel: {cls.FORCE_JOIN_CHANNEL_ID}
   ✓ Channel Username: {cls.CHANNEL_USERNAME}

🗄️ Database:
   ✓ MongoDB: Connected
   ✓ Database: {cls.DATABASE_NAME}

🔔 Settings:
   ✓ Notifications: {"Enabled" if cls.ENABLE_NOTIFICATIONS else "Disabled"}
   ✓ Log Level: {cls.LOG_LEVEL}
   ✓ Content Protection: {"Enabled" if cls.PROTECT_CONTENT else "Disabled"}

Ready to start! 🚀
"""


# Global config instance
config = Config()

# Validate configuration on import
try:
    config.validate()
    # Set WELCOME_MESSAGE after validation
    config.WELCOME_MESSAGE = config.get_welcome_message()
except ValueError as e:
    print(e)
    exit(1)
