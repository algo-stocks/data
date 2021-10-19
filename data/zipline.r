library(httr)

token = content(GET('https://auth.aicafe.cf/token'),"text")
api = paste('https://auth.aicafe.cf/api?token=', token, sep='')
login = paste('https://auth.aicafe.cf/login#url=https://sites.google.com/view/aicafe-database&token=', token, sep='')

IRdisplay::display_javascript(paste('window.open("', login, '")', sep=''))
print('If popup does not open, please click to this link')
print(login)

for (i in 0:58) {
  Sys.sleep(3)
  res = GET(api)
  if (status_code(res) == 200) {
    writeLines(content(res, "text"), "zipline.sh")
    system('sh zipline.sh')
    if (!require(rdatavn)) install.packages('rdatavn', repos=NULL, type="source")
    library(rdatavn)
    break
  }
}
