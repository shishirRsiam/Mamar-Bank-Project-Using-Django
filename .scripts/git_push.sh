#!/bin/bash

echo ""
echo ""
echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
echo ""
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

NOW=$(date +"%d %B %Y - %I:%M:%S %p")
echo -e "${YELLOW}🚀 Starting Git update at: $NOW${NC}"

echo ""
echo -e "${GREEN}⬇️ Pulling latest changes...${NC}"
git pull

# Ensure logs directory exists
mkdir -p logs

# Save commit message to logs/last_update_time.txt
echo "✅ Update completed at: $(date +"%d %B %Y - %I:%M:%S %p")" > logs/last_update_time.txt


echo ""
echo -e "${GREEN}➕ Adding changes...${NC}"
git add .

echo ""
echo -e "${GREEN}💾 Committing changes...${NC}"
git commit -am "Update Database - $NOW"

echo ""
echo -e "${GREEN}📤 Pushing changes...${NC}"
git push

echo ""
echo -e "${YELLOW}✅ Update completed at: $(date +"%d %B %Y - %I:%M:%S %p")${NC}"


