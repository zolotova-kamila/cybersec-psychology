#!/bin/bash
# Deploy to production hosting (STAGE 2)
# ONLY RUN AFTER USER APPROVAL!

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${RED}⚠️  ВНИМАНИЕ! ЭТО ПУБЛИКАЦИЯ НА ОСНОВНОЙ САЙТ${NC}"
echo ""
echo "Перед запуском убедитесь, что:"
echo "  ✓ Пользователь проверил изменения на GitHub Pages"
echo "  ✓ Получено явное подтверждение на публикацию"
echo ""

read -p "Получено подтверждение от пользователя? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo -e "${YELLOW}❌ Публикация отменена. Сначала получите подтверждение!${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}ЭТАП 2: Публикация на pozitiv-psychology.ru...${NC}"
echo "───────────────────────────────────────"

# FTP credentials
FTP_USER="cu48621"
FTP_PASS="tfCq8P4a"
FTP_HOST="vh278.timeweb.ru"

echo "🔄 Загрузка файлов на хостинг..."

lftp -u "$FTP_USER,$FTP_PASS" "$FTP_HOST" -e "
    set ssl:verify-certificate no
    set ftp:ssl-allow no
    mirror -R . pozitiv-psychology.ru/public_html/
    quit
"

echo ""
echo -e "${GREEN}✓ ГОТОВО!${NC}"
echo ""
echo "───────────────────────────────────────"
echo "🔗 Проверьте: https://pozitiv-psychology.ru/"
echo "───────────────────────────────────────"