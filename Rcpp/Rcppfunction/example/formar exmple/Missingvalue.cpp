#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
List scalar_missings() {
  int int_s = NA_INTEGER;
  String chr_s = NA_STRING;
  bool lgl_s = NA_LOGICAL;
  double num_s = NA_REAL;

  return List::create(int_s, chr_s, lgl_s, num_s);
}

// [[Rcpp::export]]
LogicalVector is_naC(NumericVector x) {
  int n = x.size();
  LogicalVector out(n);

  for (int i = 0; i < n; ++i) {
    out[i] = NumericVector::is_na(x[i]);
  }
  return out;
}

// [[Rcpp::export]]
LogicalVector is_naC2(NumericVector x) {
  return is_na(x);
}


// [[Rcpp::export]]
double meanc(NumericVector x, bool narm = false){
  double m=0;
  int k = 0;
  int n = x.size();
  for(int i = 0; i < n; i++){
    if(NumericVector::is_na(x[i])){
      if(!narm){
        m = NA_REAL;
        break;
      }else{
         k=k+1;
      }  
    }else{
      m += x[i];
    }
  }
   return m/(n-k);
}


// [[Rcpp::export]]

NumericVector cumsumc(NumericVector x){
  int n = x.size();
  NumericVector out(n);
  

  if(NumericVector::is_na(x[0])){
     out[0] = NA_REAL;
  }else{
     out[0] = x[0];
  }

  for(int i = 1; i < n; ++i) {
    if (NumericVector::is_na(x[i])){
         out[i] = NA_REAL; 
    }else{
       out[i] = out[i-1]+x[i];
    }
  }
  return out;
}
