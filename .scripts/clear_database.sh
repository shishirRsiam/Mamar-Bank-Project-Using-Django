#!/bin/bash

# Colors
RED='\033[1;31m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
GREEN='\033[1;32m'
RESET='\033[0m'

# Warning box
echo -e "${RED}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ ⚠️  WARNING: This will flush the database in the server container.      ║"
echo -e "║     ${YELLOW}ALL EXISTING DATA WILL BE LOST. Proceeding with flush...${RED}           ║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"
echo ""

# Ask for confirmation
read -p "$(echo -e "${YELLOW}Are you sure you want to flush the database? Type 'yes' to continue: ${RESET}")" CONFIRM

if [[ "$CONFIRM" != "yes" ]]; then
    echo -e "${RED}❌ Operation cancelled. Database not flushed.${RESET}"
    exit 1
fi

# Flush the database
docker exec -it server python manage.py flush --no-input
docker exec -it postgres psql -U postgres -d mamar_bank_db -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# Completion message
echo -e "${GREEN}╔════════════════════════════════════════════════════════════════════════╗"
echo -e "║ ✅  Flush complete! ${CYAN}Your Django DB is now clean and fresh. 🧼✨       ${GREEN}║"
echo -e "╚════════════════════════════════════════════════════════════════════════╝${RESET}"