iris_data = datasets::iris

irisCluster <- kmeans(iris_data[,3:4], 3, nstart=20)

plot(irisCluster, col = irisCluster$cluster)