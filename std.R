x <- matrix(rnorm(100000,1,0.5),20000,5)
betae <- runif(5)
y <- 1+ x%*%betae + rnorm(20000)
fit1 <- lm(y~x)
xs = scale(x, center = T,scale = T)
ys <- scale(y,center = T, scale = F)

fit2 <- lm(y~xs)
fit2$coefficients[-1]/attr(xs,"scaled:scale")
fit3 <- lm(ys~x)
fit4 <- lm(ys~xs)


mean(y) - sum( attr(xs, "scaled:center") * fit4$coefficients[-1])

fit5 <- lm(ys~std(x))
fit5$coefficients/attr(std(x),"scale")

fit6 = ncvreg(X=x, y=y,lambda = 0.2)


xx = std(x)
