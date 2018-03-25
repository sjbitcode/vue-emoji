FROM busybox:1.28

LABEL maintainer sjbitcode@gmail.com

ENV WEB_PATH="/usr/src/web"

# Make directories
RUN mkdir -p $WEB_PATH
WORKDIR $WEB_PATH 

COPY ./dist/ "$WEB_PATH/"

CMD echo Web container
