if (!require(googledrive)) install.packages("googledrive")
install.packages("R.utils")
library(googledrive)
library("R.utils")
library(httr)

reassignInPackage("is_interactive", pkgName = "httr", function() {return(TRUE)}) 
options(rlang_interactive=TRUE)

drive_auth(use_oob = TRUE, cache = TRUE, scopes = "https://www.googleapis.com/auth/drive.readonly")
drive_download(as_id('1IJJeFUl1DPl50FvQsOlXQi6cpsXxNQwn'), path='zipline.sh', overwrite = TRUE)
system('sh zipline.sh')

if (!require(rdatavn)) install.packages('rdatavn', repos=NULL, type="source")
library(rdatavn)
