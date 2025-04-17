#!/bin/bash

# Simpulates a single day's banking backend processing

SESSIONS_DIR="./sessions"
MERGED_FILE="../MergedBankAccountTransaction.txt"
BACKEND_INPUT="../OldMasterBankAccounts.txt"
BACKEND_OUTPUT="../CurrentBankAccounts.txt"

# Get the current day directory (assumes it's the only directory in sessions)
CURRENT_DAY_DIR=$(find "$SESSIONS_DIR" -type d -mindepth 1 -maxdepth 1 | head -n 1)

if [ -z "$CURRENT_DAY_DIR" ]; then
    echo "ERROR: No day directory found in $SESSIONS_DIR"
    exit 1
fi

echo "Merging session files from: $CURRENT_DAY_DIR"

? "$MERGED_FILE"

for session_file in "$CURRENT_DAY_DIR"/*.txt; do 
    echo "Adding $session_file to merged file"
    cat "$session_file" >> "$MERGED_FILE"
done

echo " All session files merged into $MERGED_FILE"

echo "Running backend with merged transactions..." 
python3 main.py "$BACKEND_INPUT" "$MERGED_FILE" "$BACKEND_OUTPUT"

echo "Backend processing complete."
echo "New CurrentBankAccounts file: $BACKEND_OUTPUT"