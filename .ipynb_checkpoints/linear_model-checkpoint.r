library(ggplot2)

dataset <- read.csv("regression_data.csv")

#data
df <- data.frame(
  x = dataset$YearsExperience,
  y = dataset$Salary)

#fit model
model <- lm(y ~ x, data = df)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(df$x, df$y)
pred <- predict(model)
mse <- mean((df$y - pred)^2)

#plot
ggplot(df, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 1.5, y = max(df$y) - 0.5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit of Salary vs Experience",
       x = "Years of Experience", y = "Salary") +
  theme_minimal()

ggsave("regression_plot_r.png")
