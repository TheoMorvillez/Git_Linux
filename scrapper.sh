#!/bin/bash

# Run curl command and extract Dogecoin price
price=$(curl -s https://cryptorank.io/price/dogecoin | grep -A 1 'Dogecoin Price' | grep -m 1 -oP '\$\s*\K\d+\.\d+' | head -n 1)

# Save price to file
echo $price > dogecoin_price.txt
