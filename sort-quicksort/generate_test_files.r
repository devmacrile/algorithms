# Generate files for testing and comparing QuickSort comparisons
# Devin Riley

set.seed(42)
options(scipen = 10)
sizes <- seq(10000, 1000000, by=10000)
for(i in sizes){
  arr <- sample(1:i, i, replace=F)
  fname <- paste("data/QuickSort-", i, ".txt", sep="")
  write.table(arr, fname, row.names=FALSE, col.names=FALSE)
}
