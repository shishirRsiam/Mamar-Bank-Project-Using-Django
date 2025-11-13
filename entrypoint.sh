#!/bin/bash

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color


echo -e "${YELLOW}⚙️  Running makemigrations...${NC}"
python manage.py makemigrations

echo -e "${YELLOW}📦 Applying database migrations...${NC}"
python manage.py migrate

echo -e "${GREEN}🚀 Starting Django development server at http://0.0.0.0:8000 ...${NC}"
python manage.py runserver 0.0.0.0:8000

echo -e "${GREEN}🚀 Django development server started at http://0.0.0.0:8000 ...${NC}"

