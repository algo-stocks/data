if (!require(reticulate, quietly=TRUE)) install.packages("reticulate", quiet=TRUE)
library(reticulate)
library(dplyr)

if (!file.exists('data.py')) download.file('https://raw.githubusercontent.com/algo-stocks/data/master/data.py', 'data.py')

pdata = import('data')

data = {}
rdata = NULL

data$set_source <- function(src) {
  if (src != pdata$source) {
    pdata$set_source(src)
    rdata <<- NULL
  }
}

loadPrice <- function(...) {
  if (is.null(rdata)) {
    rdata <<- pdata$load_data()
    rdata$ticker <- sub("\\^", "", rdata$ticker)
  }
  tickers = toupper(c(...))
  rdata %>% filter(ticker %in% sub("\\^", "", tickers))
}
