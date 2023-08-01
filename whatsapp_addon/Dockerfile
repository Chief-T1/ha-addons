FROM ghcr.io/home-assistant/aarch64-base

RUN apk add --no-cache git npm

COPY . /
RUN chmod a+x /run.sh
RUN chmod a+x /finish.sh

RUN cd /Baileys && npm i -f && cd .. && npm install -f

EXPOSE 3000
CMD [ "/run.sh" ]
