# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.177.0/containers/javascript-node/.devcontainer/base.Dockerfile

# [Choice] Node.js version: 16, 14, 12
FROM node:16

LABEL description="This is the base docker image for crowded space app."

RUN npm -g install eslint
RUN npm -g install eslint-config-airbnb
RUN npm install  -g eslint-plugin-import
RUN npm install  -g eslint-plugin-jsx-a11y
RUN npm install  -g eslint-plugin-react 

RUN npm install -g prettier 

RUN npm install -g --save-dev jest 
RUN npm install -g --save-dev @testing-library/react 