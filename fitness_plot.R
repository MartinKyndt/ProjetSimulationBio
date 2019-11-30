rm(list=ls())

data <- read.table("all_fitness_abc.txt", sep = ':')

plot(data$V2)
