FROM node:22-alpine

USER root
RUN npm install -g docsify-cli

WORKDIR /docs

EXPOSE 3000

CMD ["docsify", "serve", ".", "--port", "3000"]
