update:
	@echo -e "\033[32m[ <<<< update service >>>> ]\033[0m"
	git fetch --all
	git reset --hard HEAD~1
	git pull
	docker-compose build
	docker-compose up -d

start:
	@echo -e "\033[32m[ <<<< start service >>>> ]\033[0m"
	docker-compose down
	docker-compose build
	docker-compose up -d

stop:
	@echo -e "\033[31m[ <<<< stop service >>>> ] \033[0m"
	docker-compose down
