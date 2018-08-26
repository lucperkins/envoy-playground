# Envoy vs nginx

To start up the example:

```shell
docker-compose up --build
```

Access the HTTP service via envoy:

```shell
curl -i http://localhost:8000/hello
HTTP/1.1 200 OK
content-type: text/plain; charset=utf-8
content-length: 12
server: envoy
date: Sun, 26 Aug 2018 21:08:31 GMT
x-envoy-upstream-service-time: 2

Hello world!
```

Access the HTTP service via nginx:

```shell
curl -i http://localhost:9000/hello
HTTP/1.1 200 OK
Server: nginx/1.15.2
Date: Sun, 26 Aug 2018 21:09:03 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 12
Connection: keep-alive

Hello world!
```