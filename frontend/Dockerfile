FROM node:20.1.0 as build

WORKDIR /workspace/kishimen/frontend

COPY . .
RUN npm ci --unsafe-perm

ENTRYPOINT [ "npm", "run", "dev" ]
