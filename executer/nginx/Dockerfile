FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx
