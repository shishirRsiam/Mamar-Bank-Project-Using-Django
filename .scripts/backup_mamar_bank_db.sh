#!/bin/bash

# Colors
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
GREEN='\033[1;32m'
MAGENTA='\033[1;35m'
RESET='\033[0m'

# ╔════════════════════════════════════════════════════════════════════════╗
# ║ 🌟 Saving mamar_bank_db treasure with a little pg_dump magic! ✨         ║
# ╚════════════════════════════════════════════════════════════════════════╝

echo -e "${CYAN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ 🌟 ${YELLOW}Saving our mamar_bank_db treasure with a little pg_dump magic!${CYAN} ✨     ║"
echo -e "║    ${MAGENTA}Backing up like a pro, one byte at a time. 🐢💖                     ${CYAN}║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"
echo ""


mkdir -p logs
mkdir -p .database



let count_file=$(find .database -maxdepth 1 -type f | wc -l)
file_name="$((count_file + 1)). $(date +"%d %B %Y")"


echo "✅ Backing up 'mamar_bank_db' Database at: $(date +"%d %B %Y - %I:%M:%S %p")" >> logs/logs.txt
docker exec -i postgres pg_dump -U postgres mamar_bank_db > ./.database/$file_name.sql


echo -e "${GREEN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ 🎉 Backup complete! ${YELLOW}It’s backup o’clock! ⏰                            ${GREEN}║"
echo -e "║    ${CYAN}Saving mamar_bank_db with love and care. 💕📦                         ${GREEN}║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"

