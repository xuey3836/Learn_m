#include <RcppArmadillo.h>
// [[Rcpp::depends(RcppArmadillo)]]
// [[Rcpp::export]]


arma::mat mul(arma::mat M, arma::mat N) {
  return M*N;
}