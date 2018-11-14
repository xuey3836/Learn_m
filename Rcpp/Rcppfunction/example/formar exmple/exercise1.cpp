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
double f1(NumericVector x) {
  int n = x.size();
  double y = 0;
  
  for(int i = 0; i < n; ++i) {
    y += x[i] / n;
  }
  return y;
}
// mean()

// [[Rcpp::export]]

NumericVector f2(NumericVector x) {
  int n = x.size();
  NumericVector out(n);
  
  out[0] = x[0];
  for(int i = 1; i < n; ++i) {
    out[i] = out[i - 1] + x[i];
  }
  return out;
}
//cumsum

//[[Rcpp::export]]
// cumprod
NumericVector cumprodc(NumericVector x){
  int n = x.size();
  NumericVector out(n);
  out[0] = x[0];
  for (int i=1; i<n; ++i){
    out[i] = out[i-1] *x[i];
  }
  return out;
}

//[[Rcpp::export]]
// cummin
NumericVector cummaxc(NumericVector x){
  int n = x.size();
  NumericVector out(n);
  out[0] = x[0];
  for (int i=1; i<n; ++i){
    out[i] = std::max(out[i-1],x[i]);
  }
  return out;
}



// [[Rcpp::export]]
bool f3(LogicalVector x) {
  int n = x.size();
  
  for(int i = 0; i < n; ++i) {
    if (x[i]) return true;
  }
  return false;
}
// ||

// [[Rcpp::export]]
bool allc(LogicalVector x){
  int n = x.size();
  for (int i=0;i<n;++i){
    if (!x[i]) return false;
  }
  return true;
}

// [[Rcpp::export]]

int f4(Function pred, List x) {
  int n = x.size();
  
  for(int i = 0; i < n; ++i) {
    LogicalVector res = pred(x[i]);
    if (res[0]) return i + 1;
  }
  return 0;
}
// [[Rcpp::export]]

NumericVector f5(NumericVector x, NumericVector y) {
  int n = std::max(x.size(), y.size());
  NumericVector x1 = rep_len(x, n);
  NumericVector y1 = rep_len(y, n);
  
  NumericVector out(n);
  
  for (int i = 0; i < n; ++i) {
    out[i] = std::min(x1[i], y1[i]);
  }
  
  return out;
}

// [[Rcpp::export]]
// fast than R
NumericVector diffc(NumericVector x, int lag=1){
  int n = x.size() - lag;
  NumericVector out(n);
  
  for(int i=0; i<n; ++i){
    out[i] =  x[i+lag] -x[i]; 
  }
  return out;
}

// [[Rcpp::export]]
// fast than R
double varc(NumericVector x){
  int n = x.size();
  double mean = 0;
  for (int i=0;i<n; ++i){
    mean += x[i] /n;
  }
  double var = 0;
  for (int i= 0; i < n; ++i){
    var += pow((x[i]-mean),2)/(n-1); 
   }
   return var;
}