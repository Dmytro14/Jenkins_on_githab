FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/index.html
COPY ./puzatka_house-main/. /usr/share/nginx/html/