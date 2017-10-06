[ "$(whoami)" != "root" ] && { echo "Execute como root"; exit; } 
local="/etc/ircbot"
chmod +x drawA.sh
chmod +x drawB.sh
if [ -e "$local" ]  
then
	echo "O PROGRAMA JA ESTA INSTALADO"
	exit
fi 
./drawA.sh
sleep 3
echo "$(whoami)"
chmod +x Init.py
mkdir $local
cp * $local
ln -sd $local"/Init.py" "/bin/ircbot"
./drawB.sh
