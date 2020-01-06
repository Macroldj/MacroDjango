# boot application

function build(){
    echo -e "\033[32m[ <<<< build project >>>> ]\033[0m"
    echo "build project"
    docker-compose down
    docker-compose build
    docker-compose up
}

function start(){
    echo -e "\033[32m[ <<<< start service >>>> ]\033[0m"
    docker-compose build
    docker-compose up -d
}

function stop(){
    echo -e "\033[31m[ <<<< stop service >>>> ] \033[0m"
    docker-compose down
}

function update_git(){
    echo -e "\033[34m[ <<<< update github code >>>> ] \033[0m"
    git fetch --all
    git reset --hard origin/master
    git pull
}

function debug(){
    echo -e "\033[33m[ <<<< debug code >>>> ] \033[0m"
    docker-compose build
    docker-compose up
}

case ${1} in
   start|stop|update|build|debug)
   case ${1} in
       start)
       start
       ;;
       stop)
       stop
       ;;
       build)
       build
       ;;
       update)
       update_git
       ;;
       debug)
       debug
       ;;
   esac
   ;;
   help)
    echo " start        - Starts service"
    echo " update       - update code from gitlab"
    echo " stop         - stop all app service."
    echo " build        - build and init project."
    echo " help         - Displays the help"
   ;;
esac
