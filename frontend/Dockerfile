# Stage 1: Build the application
FROM node:18-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

# Stage 2: Create the production image
FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app/build ./build
COPY package.json ./
COPY . .
# SvelteKit uses a standalone server, so we don't need a separate web server like Nginx
# We need to install the production dependencies
RUN npm install --omit=dev

EXPOSE 3000

CMD ["node", "build"]
