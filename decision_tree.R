library('rpart')
library('rpart.plot')

data <- read.csv('buy_computer.csv',header = TRUE)

tree <- rpart(BUYS_COMPUTER ~ AGE+INCOME+STUDENT+CREDIT_RATING , data = data , method = "class", control = rpart.control(minsplit = 1,minbucket = 1,cp = 0))

png('decision_tree.png')
plot(tree,uniform = TRUE)
text(tree,use.n = TRUE)
dev.off()