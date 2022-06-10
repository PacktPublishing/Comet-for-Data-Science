library(cometr)
library(caret)
library(Metrics)


df <- read.csv('source/mushrooms.csv')

for(i in 2:ncol(df)) {       
  df[ , i] <-  as.numeric(factor(df[ , i], levels = unique(df[ , i]), exclude = NULL))
}

df$class <- as.factor(df$class)
experiment <- create_experiment()
set.seed(10)
n <- dim(df)[1]
burst <- 1000
for (i in seq(200, n+burst, by=burst)) {
  if(i > n)
    i = n
  dft <- df[c(1:i),]
  index <- createDataPartition(y = dft$class, times = 1, p = 0.7, list = FALSE)
  training <- dft[index,]
  test <- dft[-index,]
  
  model <- train(class ~ ., method='knn', data = training, metric='Accuracy')
  test$pred <- predict(model, test)
  
  acc <- accuracy(test$class, test$pred)
  test$factor_pred <- as.factor(test$pred)
  test$factor_truth <- as.factor(test$class)
  
  precision <- posPredValue(test$factor_truth, test$factor_pred)
  recall <- sensitivity(test$factor_truth, test$factor_pred)
  
  F1 <- (2 * precision * recall) / (precision + recall)
  experiment$log_metric("accuracy", acc, step=i)
  experiment$log_metric("precision", precision, step=i)
  experiment$log_metric("recall", recall, step=i)
  experiment$log_metric("F1", F1, step=i)
  
}

experiment$stop()
