# Vue.js용 Dockerfile
FROM node:lts as build-stage

WORKDIR /usr/src/front_app

COPY . /usr/src/front_app/

RUN npm install
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /usr/src/front_app/dist /usr/share/nginx/html

# 권한 변경
RUN chown -R nginx:nginx /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]