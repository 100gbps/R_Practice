library("e1071")

raw_data <- read.csv("buy_computer_spaces.csv",sep = " ",header = TRUE)

naive <- naiveBayes(BUYS_COMPUTER ~ AGE+INCOME+STUDENT+CREDIT_RATING , data = raw_data)

print (naive)