redisurl="http://download.redis.io/redis-stable.tar.gz"
curl -s -o redis-stable.tar.gz $redisurl
sudo su root
mkdir -p /usr/local/lib/
chmod a+w /usr/local/lib/
tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
rm redis-stable.tar.gz
cd /usr/local/lib/redis-stable/
make && make install
redis-cli --version
ls -hFG /usr/local/bin/redis-* | sort
sudo su root
mkdir -p /etc/redis/
touch /etc/redis/6379.conf
config = "
port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes"
echo $config > /etc/redis/6379.conf
redis-server /etc/redis/6379.conf