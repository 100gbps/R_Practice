fact_recur <- function(num){
	fact = 1
	for (value in c(2:num)){
		fact <- fact*value
	}
	fact <- fact
}
#return value is the last expression evaluated
print (fact_recur(15))