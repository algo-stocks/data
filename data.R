if (!require(reticulate, quietly=TRUE)) install.packages("reticulate", quiet=TRUE)
library(reticulate)
library(dplyr)

if (!file.exists('data.py')) download.file('https://raw.githubusercontent.com/algo-stocks/data/master/data.py', 'data.py')

data = import('data')

loadPrice <- function(...) {
  if (is.null(data$data)) {
    data$load_data()
  }
  data$data %>% filter(ticker %in% c(...))
}
