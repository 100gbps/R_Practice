iris_data = datasets::iris

irisCluster <- kmeans(iris_data[,1:4], 3, nstart=20)

plot(iris_data, col = irisCluster$cluster)