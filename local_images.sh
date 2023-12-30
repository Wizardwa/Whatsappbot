#!/bin/bash
latest_image=$(find ~/Projects/Whatsappbot/images -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -printf "%T+ %p\n" 2>/dev/null | sort -r | head -n 1 | cut -d' ' -f2-)
#print name
latest_image=$(find ~/Projects/Whatsappbot/images -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -printf "%T+ %p\n" 2>/dev/null | sort -r | head -n 1 | cut -d' ' -f2-)
echo "$(basename "$latest_image")"
