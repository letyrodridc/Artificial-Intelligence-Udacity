data <- read.csv(filename, header = TRUE)
colnames(v) <- cbind(colnames(data[1]),colnames(data[6]))

data[data$Case == 'heuristic',]

p1 <- data[data$Problem == 'problem1',]
tmp <- p1
v <- data.frame(tmp[,1],tmp[,6])
colnames(v) <- cbind(colnames(data[1]),colnames(data[6]))