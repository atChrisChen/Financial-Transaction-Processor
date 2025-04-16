for DAY in 1 2 3 4 5 6 7
do
    #read based off how daily.sh is handling directories
    #export

    echo "Day: $DAY"
    ./daily.sh

    cp ../OldMasterBankAccounts.txt "../OldMasterBankAccounts${DAY}.txt"
    cp ../CurrentBankAccounts.txt "../CurrentBankAccounts${DAY}.txt"
done
echo "Finished weekly simulation."