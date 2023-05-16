FROM node:20.1.0 as build

WORKDIR /workspace/kishimen/frontend

COPY package*.json ./
RUN npm ci --unsafe-perm
COPY . .
