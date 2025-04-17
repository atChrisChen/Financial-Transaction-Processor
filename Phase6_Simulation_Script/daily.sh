#!/bin/bash

# Simpulates a single day's banking backend processing

SESSIONS_DIR="./sessions"
MERGED_FILE="../MergedBankAccountTransaction.txt"
BACKEND_INPUT="../OldMasterBankAccounts.txt"
BACKEND_OUTPUT="../CurrentBankAccounts.txt"

echo "Merging session files from: $SESSIONS_DIR"

? "$MERGED_FILE"

for session_file in "$SESSIONS_DIR"/*.txt; do 
    echo "Adding $session_file to merged file"
    cat "$session_file" >> "$MERGED_FILE"
done

echo " All session files merged into $MERGED_FILE"

echo "Running backend with merged transactions..." 
python3 main.py "$BACKEND_INPUT" "$MERGED_FILE" "$BACKEND_OUTPUT"

echo "Backend processing complete."
echo "New CurrentBankAccounts file: $BACKEND_OUTPUT"