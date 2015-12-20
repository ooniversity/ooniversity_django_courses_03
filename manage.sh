#!/bin/bash
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon pybursa

usage()
{
        echo "$0 (start|stop|restart)"
}

start()
{
	if [ -f /home/san/python/bursa/tmp/project-master.pid ];
	    then
	    echo "Already running"
	    exit 0
	else
	    cd /home/san/python/bursa/2/pybursa/
	    uwsgi --ini uwsgi.ini
	    echo "Started"
	fi
}

stop()
{
if [ -f /home/san/python/bursa/tmp/project-master.pid ];
then
    cd /home/san/python/bursa/tmp/
    uwsgi --stop project-master.pid
    rm project-master.pid
    rm project-master.sock
    cd ..
    echo "Stopped"
else
    echo "Not running"
    exit 0 
fi
}

case $1 in
	"start")	start;;
	"stop")		stop;;
	"restart")	stop; sleep 2; start;;
	*)		usage;;
esac
deactivate
exit
