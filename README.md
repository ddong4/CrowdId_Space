# Crowded_Space

Part of [Johnson Space Center Hackathon (JSC Hack) Jan 28-30 2022](https://jsc-hack.github.io/)

## Team Members (in alphabetical order of last name)

- David Dong
- Angela Fan
- Taylor Hou
- Chantal Nyiramwiza
- Abdurrahman Padela
## Project Description

TODO

## Start Development Container

This project provides a containerized dev environment via VS Code.

Follow these steps to open this sample in a container using the VS Code Remote - Containers extension:

1. If this is your first time using a development container, please ensure your system meets the pre-reqs (i.e. have Docker installed) in the [getting started steps](https://aka.ms/vscode-remote/containers/getting-started).

   - Make sure to set up the WSL 2 environment if you are on Windows.

2. To use this repository, open a locally cloned copy of the code:
   - Clone this repository to your local filesystem (MacOS, Linux), or the WSL 2 environment (Windows)
   - Press <kbd>F1</kbd> and select the **Remote-Containers: Open Folder in Container...** command.
   - Select the cloned copy of this folder, wait for the container to start, and try things out!

## Client Directory Structure

- `client/public` : static files that serve as the scaffold for the React app, including `index.html`
- `client/src` : JS and CSS files that form the actual React App, including `index.js` and `App.js`
  - `client/src/styles` : CSS styling files
  - `client/src/components`: Reactjs components that get loaded and manipulated
  - `client/src/pages`: Each page to be rendered

## Server Directory Structure

- `server/models` : table models that sequelize interacts with
- `server/routes` : routing for query requests

## Running npm commands

After you have launched the development container, in the project directory:

First `cd server` and then `npm start`. Repeat for client `cd ..` ; `cd client` and also `npm start`

Then run in separate terminals for client and server:

## For Client

Server runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.
