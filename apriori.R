library('arules')

raw_data <- read.csv('groceries.csv')

txns <- read.transactions('groceries.csv',format = 'basket', sep = ",", rm.duplicates = TRUE, cols = 1)

txns@itemInfo$labels = gsub("\"","",txns@itemInfo$labels)

rules = apriori(txns,parameter = list(target = "rules"))

inspect(rules)

itemFrequencyPlot(txns,topN = 5)