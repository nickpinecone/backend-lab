FROM node

ADD . /opt/client
WORKDIR /opt/client
RUN npm install

EXPOSE 5005

CMD ["npm", "run", "dev"]
