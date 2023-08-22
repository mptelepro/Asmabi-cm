if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MuraliNew/Murali-Tamil-Pro.git /Murali-Tamil-Pro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Murali-Tamil-Pro
fi
cd /Murali-Tamil-Pro
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
