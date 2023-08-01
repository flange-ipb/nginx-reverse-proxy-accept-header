# nginx-reverse-proxy-accept-header
Demonstrator for switching NGINX's `proxy_pass` target using the Accept header

## Build and start the application
`docker-compose build && docker-compose up && docker-compose rm -f`

## Run some tests
- `curl -H "Accept: text/html" http://localhost`
- `curl -H "Accept: text/turtle" http://localhost`
- `curl -H "Accept: application/ld+json" http://localhost`
