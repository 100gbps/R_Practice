stu_data <- data.frame(
	gender = c("male","male","male"),
	roll_no = c("91","92","93"),
	marks = c(18,18,20),
	name = c('a','b','c')
)

print (stu_data)

city <- c("Tampa","Seattle","Hartford","Denver")
state <- c("FL","WA","CT","CO")
zipcode <- c(33602,98104,06161,80294)

location_data <- cbind(city,state,zipcode)

print (location_data)
