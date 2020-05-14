library(ggplot2)
library(reshape2)
library(pheatmap)
library(devtools)
library(grid)
library(rgl)
library(ggbiplot)
theme_complete_bw <- function(base_size = 24, base_family = "") 
{
  theme_grey(base_size = base_size, base_family = base_family) %+replace% 
    theme(
      axis.line =         element_blank(),
      axis.text.x =       element_text(size = base_size * 0.8 , lineheight = 0.9, colour = "black", vjust = 1),
      axis.text.y =       element_text(size = base_size * 0.8, lineheight = 0.9, colour = "black", hjust = 1),
      axis.ticks =        element_line(colour = "black"),
      axis.title.x =      element_text(size = base_size, vjust = 0.5),
      axis.title.y =      element_text(size = base_size, angle = 90, vjust = 0.5),
      axis.ticks.length = unit(0.15, "cm"),
      axis.ticks.margin = unit(0.1, "cm"),
      
      legend.background = element_rect(colour=NA), 
      legend.key =        element_rect(fill =NA, colour = "black", size = 0.25),
      legend.key.size =   unit(1.5, "lines"),
      legend.text =       element_text(size = base_size * 0.7),
      legend.title =      element_text(size = base_size * 0.8),
      legend.position =   "top",
      
      panel.background = element_rect(fill = "white", colour = NA), 
      panel.border =     element_rect(fill = NA, colour = "black", size=2), 
      panel.grid.major = element_line(colour = NA, size = 0.2), #"grey"
      panel.grid.minor = element_line(colour = NA, size = 0.5), #"grey"
      panel.margin =     unit(0.25, "lines"),
      
      strip.background = element_rect(fill = NA, colour = NA), 
      strip.text.x =     element_text(colour = "black", size = base_size * 0.8),
      strip.text.y =     element_text(colour = "black", size = base_size * 0.8, angle = +90),
      
      plot.background =  element_rect(colour = NA, fill = "white"),
      plot.title =       element_text(size = base_size*.8),
      plot.margin =      unit(c(1, 1, .5, .5), "lines"))
}

setwd("/Users/alireza/Desktop/University/97-98\ Spring/Neuroscience/Project/Final_Paper")

my_data <- read.csv("data.csv")
mean_data <- as.data.frame(read.csv("neuro_data.csv"))
data <-as.data.frame(my_data)
first_data <- as.data.frame(read.csv("data_neuro.csv"))



#Regression
ggplot(mean_data, aes(mean_data$mean.pain, mean_data$num.of.True)) + geom_point() + geom_smooth(method = lm)+labs(x = 'mean pain', y = 'correctness')+theme_complete_bw()

#Correlation
cor.test(mean_data$num.of.True, mean_data$mean.pain)
cor.test(data$correctness, data$Pain.Rate)
pheatmap(cor(data))
pheatmap(cor(mean_data))

#PCA
datapca <- prcomp(data[, c(1:14)], center = TRUE, scale. = TRUE)
plot(datapca)
pcx <- data.frame(datapca$x)
ggplot(pcx, aes(PC1, PC2)) + geom_point(size=2) + theme_complete_bw()
plot(data[,7:8])
plot3d(pcx[,1:3])
pcr <- data.frame(datapca$rotation)
pcr$feature <- rownames(pcr)
ggplot(pcr, aes(PC1, PC2, label=feature))+geom_text() + theme_complete_bw()
ggbiplot(datapca)

#ttest
t.test(data$correctness, mu= 0.5)

#fisher test
correct <- as.integer((first_data$Response == first_data$Stimulus))
cold_index <- correct[first_data$Stimulus == "cold"]
a <- sum(cold_index)
c <- length(cold_index) - a
warm_index <- correct[first_data$Stimulus == "warm"]
b <- sum(warm_index)
d <- length(warm_index) - b
table <- rbind(c(a,d),c(c,b))
fisher.test(table, alternative = 'g')
