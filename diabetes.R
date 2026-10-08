# The R equivalent of diabetes.py. Run it with:
#     Rscript diabetes.R

# Load Dataset (the same Efron et al. data that sklearn's load_diabetes uses)
url <- "https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt"
df <- read.delim(url)
X <- df[, setdiff(names(df), "Y")]
y <- df$Y

# Train/Test Split
test_idx <- sample(nrow(df), size = round(0.2 * nrow(df)))
X_train <- X[-test_idx, ]
X_test <- X[test_idx, ]
y_train <- y[-test_idx]
y_test <- y[test_idx]

# Scale the Data (using the training mean and sd for both sets)
X_train_scaled <- scale(X_train)
X_test_scaled <- scale(X_test,
                       center = attr(X_train_scaled, "scaled:center"),
                       scale = attr(X_train_scaled, "scaled:scale"))

# Train the Linear Regression Model
model <- lm(y_train ~ ., data = as.data.frame(X_train_scaled))

# Test the Model
y_pred <- predict(model, newdata = as.data.frame(X_test_scaled))
rmse <- sqrt(mean((y_pred - y_test)^2))

cat("rmse =", rmse, "\n")
