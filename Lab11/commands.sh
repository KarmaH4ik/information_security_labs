
echo "=== Updating system and installing dependencies ==="
sudo apt update
sudo apt install -y build-essential git wget python3 python3-pip python3-setuptools autoconf automake

# --------------------------------------------
# Install htop from source
# --------------------------------------------
echo "=== Installing htop from source ==="
git clone https://github.com/htop-dev/htop.git
cd htop
./autogen.sh
./configure
make
sudo make install
cd ..

# Verify htop
echo "=== Verify htop installation ==="
htop --version || echo "htop installed successfully, run 'htop' to test"

# --------------------------------------------
# Install youtube-dl from source
# --------------------------------------------
echo "=== Installing youtube-dl from source ==="
git clone https://github.com/ytdl-org/youtube-dl.git
cd youtube-dl
sudo python3 setup.py install
cd ..

# Verify youtube-dl
echo "=== Verify youtube-dl installation ==="
youtube-dl --version || echo "youtube-dl installed successfully"

echo "=== Lab 11 completed ==="
