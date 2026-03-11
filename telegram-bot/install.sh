#!/bin/bash

# Installation script for Telegram Bot
# Run as root

echo "=== Installing Telegram Bot ==="

# Install pip if not installed
apt-get update
apt-get install -y python3-pip

# Install requirements
cd /root/.openclaw/workspace/cybersec-psychology/telegram-bot
pip3 install -r requirements.txt

# Create log directory
mkdir -p /var/log
touch /var/log/telegram_bot.log
chmod 666 /var/log/telegram_bot.log

# Copy systemd service
cp telegram-bot.service /etc/systemd/system/

# Reload systemd
systemctl daemon-reload

# Enable and start service
systemctl enable telegram-bot
systemctl start telegram-bot

echo "=== Bot installed and started! ==="
echo "Check status: systemctl status telegram-bot"
echo "View logs: tail -f /var/log/telegram_bot.log"
echo ""
echo "Bot is running at: @ShchitOtMoshennikov_bot"