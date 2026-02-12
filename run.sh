#!/bin/bash
cat << "EOF"
                          (\_______/)
                          (  ^   ^  )
                         (    >‿<    )
                           \_______/
                         🦫 BoberFun
EOF
echo ""
echo "Setting up environment now"
echo ""
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
if ! python -c "import pygame" &> /dev/null; then
    pip install pygame
fi
echo ""
echo "Launching fireworks, enjoy!"
echo ""
./venv/bin/python firework.py

deactivate
echo ""
echo "Clickable Firework Demo closed. Virtual environment deactivated."
echo ""

