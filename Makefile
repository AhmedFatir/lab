all: build run

build:
	@clear
	@cp /Users/afatir/.zsh_history zsh_history
	@docker-compose build 

run:
	@docker-compose up -d

clean:
	@docker stop clab || true
	@docker rm clab || true
	@docker rmi -f ilab || true
	@docker volume rm vlab || true
	@docker network rm nlab || true

re: clean all

lab:
	@docker exec -it clab /bin/zsh

.PHONY: all build run clean re lab