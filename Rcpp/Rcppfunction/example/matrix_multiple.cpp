#include <Rcpp.h>
using namespace Rcpp;

// This is a simple example of exporting a C++ function to R. You can
// source this function into an R session using the Rcpp::sourceCpp 
// function (or via the Source button on the editor toolbar). Learn
// more about Rcpp at:
//
//   http://www.rcpp.org/
//   http://adv-r.had.co.nz/Rcpp.html
//   http://gallery.rcpp.org/
//

// [[Rcpp::export]]
NumericVector matrixfun(NumericMatrix x, NumericMatrix y){
  int n = x.nrow();
  int p = x.ncol();
  int m = y.ncol();
  NumericMatrix z(n,m);
  
  for(int i=0; i < n; i++){
    for(int j=0;j < p;j++){
      for (int l=0;l<m;l++){
        z(i,l)= z(i,l) +x(i,j)*y(j,l);
      }
    }
  }
  return z;
}


