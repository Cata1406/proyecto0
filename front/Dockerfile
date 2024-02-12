FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y curl git

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs
RUN npm install -g yarn

COPY . /front

WORKDIR /front

RUN yarn install

EXPOSE 3000

WORKDIR /front/task-manager

CMD ["sh", "-c", "yarn start --port 3000 --host 0.0.0.0"]
