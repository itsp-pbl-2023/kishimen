FROM node:20.0.0 as build

WORKDIR /workspace/kishimen/frontend

COPY package*.json ./
RUN npm ci --unsafe-perm
COPY . .

ENTRYPOINT [ "npm", "run", "dev" ]
