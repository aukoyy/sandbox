## How to implement tailwind

See official instructions: [Tailwind Installation Docs](https://tailwindcss.com/docs/installation)

## Steps to implement tailwind in a React project

Tailwind is a postcss plugin. Vue CLI, Webpack, Next.JS already sports postcss.

0. First make sure you are in a npm folder. If not, run `npm init`.
1. Install Tailwind with NPM

   `npm install tailwindcss postcss-cli autoprefixer --save`

2. Create a config file (optional)

   `npx tailwind init`

3. Create a postcss.config.js file in the root of the project (optional). Add the following:

   ```javascript
   module.exports = {
     plugins: [require("tailwindcss"), require("autoprefixer")]
   };
   ```

4. Create a css/tailwind.css file in the root client folder

5. Copy the preflight code into the tailwind.css file:
   ```css
   @tailwind base;

   @tailwind components;

   @tailwind utilities;
   ```
6. Add a build command to scripts in package.json

   `"build:css": "postcss css/tailwind.css -o public/build/tailwind.css",`

7. Run `npm run build:css`
8. Add import statement to index.tsx

   `import './public/build/tailwind.css';`
