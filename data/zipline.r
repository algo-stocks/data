library(httr)

token = content(GET('https://auth.aicafe.one/token'),"text")
api = paste('https://auth.aicafe.one/api?token=', token, sep='')
login = paste('https://auth.aicafe.one/login#url=https://sites.google.com/view/aicafe-database&token=', token, sep='')

expire = strtoi(substr(token, 0, gregexpr(pattern="\\.", token)[[1]][1]-1)) + 180

IRdisplay::display_javascript(paste('Date.now()>',expire,'000 || window.open("', login, '")', sep=''))
IRdisplay::display_text('If popup does not open, please click to this link')
IRdisplay::display_text(login)

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
