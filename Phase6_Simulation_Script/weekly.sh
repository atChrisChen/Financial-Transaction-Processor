SESSIONS_DIR="./sessions"
DAYS_DIR="./days"
ROOT_DIR="../"
DAILY_SCRIPT="./daily.sh"

# Start with original old master account file
CURRENT_MASTER="$ROOT_DIR/OldMasterBankAccounts.txt"

# Check if daily.sh is executable
if [ ! -x "$DAILY_SCRIPT" ]; then
    echo "ERROR: $DAILY_SCRIPT is not executable. Run: chmod +x $DAILY_SCRIPT"
    exit 1
fi


echo "Starting weekly simulation..."

# Loop over 7 days
for day in {1..7}; do
    echo -e "\n Running Day $day..."

    DAY_SESSIONS_DIR="$DAYS_DIR/day$day"

    if [ ! -d "$DAY_SESSIONS_DIR" ]; then
        echo "ERROR: $DAY_SESSIONS_DIR does not exist. Skipping day $day."
        continue
    fi

    # Clear out and copy the day's session files
    echo "Preparing session files for Day $day"
    rm -f "$SESSIONS_DIR"/*.txt
    cp "$DAY_SESSIONS_DIR"/*.txt "$SESSIONS_DIR/"

    # Replace OldMasterBankAccounts.txt with current version
    cp "$CURRENT_MASTER" "$ROOT_DIR/OldMasterBankAccounts.txt"

    # Run the daily script
    echo "Running daily.sh for Day $day"
    bash "$DAILY_SCRIPT"

    # After running backend, CurrentBankAccounts.txt becomes next day's master
    CURRENT_MASTER="$ROOT_DIR/CurrentBankAccounts.txt"

    # Optionally archive outputs
    ARCHIVE_DIR="$ROOT_DIR/day${day}_output"
    mkdir -p "$ARCHIVE_DIR"
    cp "$ROOT_DIR/MergedBankAccountTransaction.txt" "$ARCHIVE_DIR/"
    cp "$ROOT_DIR/CurrentBankAccounts.txt" "$ARCHIVE_DIR/"
    echo "Day $day output archived in: $ARCHIVE_DIR"

    echo "Day $day complete. Master updated and outputs archived."
done

echo -e "\nWeekly simulation completed!"
