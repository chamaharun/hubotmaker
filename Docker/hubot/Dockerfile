FROM alpine
MAINTAINER nasa9084
RUN apk --no-cache add nodejs &&\
    npm install -g npm &&\
    npm install -g yo generator-hubot hubot coffee-script &&\
    adduser -h bot -D bot
USER bot
WORKDIR /bot
RUN yes | yo hubot --owner="user" --description="No Description" --name="Hubot" --adapter=slack &&\
    sed -i -e '/"hubot-heroku-keepalive",/d' external-scripts.json &&\
    sed -i -e '/"hubot-google-images",/d' external-scripts.json &&\
    sed -i -e '/"hubot-google-translate",/d' external-scripts.json &&\
    rm bin/hubot
ADD scripts/name.coffee scripts/
ADD hubot bin/hubot
ADD scripts_for_hubot/scripts/*.coffee node_modules/hubot-scripts/src/scripts/

CMD ["/bot/bin/hubot", "--adapter", "slack"]
