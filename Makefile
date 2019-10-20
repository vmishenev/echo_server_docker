
build:
	docker build -t socksrv:1 .
start:
	docker run -d --rm -p 9090:9091 socksrv:1 > container_id
stop:
	cat container_id | xargs docker stop
clean:
	rm container_id
