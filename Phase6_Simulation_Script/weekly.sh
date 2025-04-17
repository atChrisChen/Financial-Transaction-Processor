cp ../OldMasterBankAccounts.txt ../OldMasterBankAccounts_p6.txt
cp ../CurrentBankAccounts.txt ../CurrentBankAccounts_p6.txt

for DAY in 1 2 3 4 5 6 7
do
    echo "Start of day: $DAY"
    ./daily.sh $DAY
    echo "End of day: $DAY"
done

echo "Finished weekly simulation."
