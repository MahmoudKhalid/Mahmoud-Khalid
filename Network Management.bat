@echo off

echo Must Copy the script to C:\Windows\System32\ (Recommended)
echo Must run as administrator (Recommended)
goto :options

:options
::Options introduction
echo Welcome to Network Management 
echo [+] Choose a number from...
echo       -------------------
echo [+] 1- Display IPv4 Addreass  [+]
echo [+] 2- Display MAC Addreass   [+]
echo [+] 3- Restart Network        [+]
echo [+] 4- Stop session lease     [+]
echo [+] 5- Renew Connection lease [+]
echo [+] 6- Set IPv4 static        [+]
echo [+] 7- Remove IPv4 static     [+]
echo [+] 8- Set DNS static         [+]
echo [+] 9- Remove DNS static      [+]
echo [+]10- Display Netstat        [+]
echo [+]11- Display DNS Cashe      [+]
echo [+]12- Clear DNS Cashe        [+]
echo [+]13- Display Options HELP   [+]
echo       -------------------
echo.

:input
::Input
set /p Order=What is your choice: 
if [%Order%] == [] (
	goto :input)
if %Order% == 1 (
	ipconfig /all 
	echo.
	echo.
	goto :input)
if %Order% == 2 (
	getmac /v
	echo.
	echo.
	goto :input)
if %Order% == 3 (
	ipconfig /release
	ipconfig /renew 
	echo.
	echo.
	goto :input)
if %Order% == 4 (
	ipconfig /release
	echo       -------------------
	echo       -------------------
	echo WARNING : When run this option will to disconnect internet and get IP from APIPA 169.254.X.X, for reconnect you must choose option number 5
	echo.
	echo.
	goto :input)
if %Order% == 5 (
	ipconfig /renew
	echo.
	echo.
	goto :input)
if %Order% == 6 (
	echo Must copy Script location in C:\Windows\System32\ and Run as administrator
	echo You must put some information [name ethernet, IP Addreass, Mask, Gateway]
	netsh interface ipv4 show interface
	set /P eth=Ethernet Name: 
	set /P ip=IP Addreass: 
	set /P mask=IP Mask: 
	set /P gateway=IP Gateway : 
	CALL echo Configure Ethernet "%eth%" ...
	CALL netsh interface ipv4 set address name="%%eth%%" source=static address=%%ip%% mask=%%mask%% gateway=%%gateway%%
	CALL echo Successfully Configure IP Address Static %%ip%%
	echo if you want configure DNS put number 8
	echo.
	echo.
	goto :input)
if %Order% == 7 (
	echo Must copy Script location in C:\Windows\System32\ and Run as administrator
	echo You must put some information [name ethernet]
	netsh interface ipv4 show interface
	set /p ether=Ethernet Name: 
	CALL netsh interface ipv4 set address name="%%ether%%" source=dhcp
	echo Successfully remove IP address and Configure from DHCP
	echo.
	echo.
	goto :input)
if %Order% == 8 (
	echo Must copy Script location in C:\Windows\System32\ and Run as administrator
	echo You must put some information [name ethernet, DNS]
	netsh interface ipv4 show interface
	set /p ethern=Ethernet Name: 
	set /p dns=Enter DNS: 
	CALL netsh interface ipv4 add dnsserver name="%%ethern%%" address=%%dns%% index=1
	CALL echo Successfully Configure DNS %%dns%% 
	echo.
	echo.
	goto :input)
if %Order% == 9 (
	echo Must copy Script location in C:\Windows\System32\ and Run as administrator
	echo You must put some information [name ethernet]
	netsh interface ipv4 show interface
	set /p ethernet=Ethernet Name: 
	CALL netsh interface ipv4 delete dnsserver "%%ethernet%%" all
	echo Successfully remove DNS and Configure DNS from DHCP 
	echo.
	echo.
	goto :input)
if %Order% == 10 (
	netstat -a
	echo.
	echo.
	goto :input)
if %Order% == 11 (
	ipconfig /displaydns
	echo.
	echo.
	goto :input)
if %Order% == 12 (
	ipconfig /flushdns
	echo.
	echo.
	goto :input)
if %Order% == 13 (
	goto :options
	echo.
	echo.
	goto :input)

pause