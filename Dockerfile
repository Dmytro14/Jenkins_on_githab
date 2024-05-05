FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/index.html
COPY ./puthatka_house-main/. /usr/share/nginx/html/
#COPY ./puzatka_house-main/. /usr/share/nginx/html/
# sample
