library("Rcpp")
evalCpp("2 + 2")
# R function
isOddR <- function(num = 10L) {
  result <- (num %% 2L == 1L)
  return(result)
}
#Rcpp function
cppFunction("
bool isOddCpp(int num = 10) {
            bool result = (num % 2 == 1);
            return result;
            }")
isOddCpp(42L)


sourceCpp("Rcpp/convolve.cpp")

##time comparison
library("microbenchmark")
results <- microbenchmark(isOddR = isOddR(12L),
                          isOddCpp = isOddCpp(12L))
print(summary(results)[, c(1:7)],digits=1)


##
set.seed(123)
evalCpp("R::rnorm(0, 1)")

set.seed(123)
# Implicit mean of 0, sd of 1
rnorm(1)
#Rcpp function
set.seed(123)
evalCpp("Rcpp::rnorm(3)")


##boostrap example
# Function declaration
bootstrap_r <- function(ds, B = 1000) {
  # Preallocate storage for statistics
  boot_stat <- matrix(NA, nrow = B, ncol = 2)
  # Number of observations
  n <- length(ds)
  # Perform bootstrap
  for(i in seq_len(B)) {
    # Sample initial data
    gen_data <- ds[ sample(n, n, replace=TRUE) ]
    # Calculate sample data mean and SD
    boot_stat[i,] <- c(mean(gen_data),
                       sd(gen_data))
  }
  # Return bootstrap result
  return(boot_stat)
}
# Set seed to generate data
set.seed(512)
# Generate data
initdata <- rnorm(1000, mean = 21, sd = 10)
# Set a new _different_ seed for bootstrapping
set.seed(883)
# Perform bootstrap
result_r <- bootstrap_r(initdata)

sourceCpp("Rcpp/bootstrap.cpp")
# Use the same seed use in R and C++
set.seed(883)
# Perform bootstrap with C++ function
result_cpp <- bootstrap_cpp(initdata)
# Compare output
all.equal(result_r, result_cpp)
library(rbenchmark)
benchmark(r = bootstrap_r(initdata),
          cpp = bootstrap_cpp(initdata))[, 1:4]