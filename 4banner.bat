cd /d %curpath% 
set num=0
:start 
wget https://s.4cdn.org/image/title/%num%.gif --no-check-certificate
wget https://s.4cdn.org/image/title/%num%.jpg --no-check-certificate
wget https://s.4cdn.org/image/title/%num%.png --no-check-certificate
set /a num+=1
goto start                                                       