#!/bin/bash
# Deploy script for cybersec-psychology website
# Follows two-stage deployment process

set -e

echo "🚀 Начинаем публикацию изменений..."
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Git commit and push
echo -e "${YELLOW}ЭТАП 1: Публикация на GitHub Pages...${NC}"
echo "───────────────────────────────────────"

git add -A

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo -e "${GREEN}✓ Нет изменений для коммита${NC}"
else
    read -p "Введите описание изменений: " message
    git commit -m "$message"
    GIT_SSH_COMMAND="ssh -i /root/.ssh/id_ed25519_pozitiv -o IdentitiesOnly=yes" git push origin main
    echo -e "${GREEN}✓ Изменения отправлены в GitHub${NC}"
fi

echo ""
echo "⏳ Ждём обновления GitHub Pages (10 секунд)..."
sleep 10

echo ""
echo -e "${GREEN}✓ ГОТОВО!${NC}"
echo ""
echo "───────────────────────────────────────"
echo "🔗 Тестовый URL: https://zolotova-kamila.github.io/cybersec-psychology"
echo ""
echo "⚠️  ДАЛЬШЕ ДЕЙСТВУЕТ ПОЛЬЗОВАТЕЛЬ:"
echo "   1. Проверьте изменения на тестовом URL"
echo "   2. Если всё ок — скажите мне 'публикуй на основной сайт'"
echo "   3. Только после этого я загружу на pozitiv-psychology.ru"
echo ""
echo "───────────────────────────────────────"