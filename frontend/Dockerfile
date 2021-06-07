FROM node:lts-alpine

COPY . /usr/src/app/frontend
WORKDIR /usr/src/app/frontend

# install project dependencies
RUN npm install
RUN npm run

EXPOSE 8080

ENTRYPOINT ["npm", "run", "--silent"]

CMD ["serve"]