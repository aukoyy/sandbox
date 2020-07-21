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
   	plugins: [require('tailwindcss'), require('autoprefixer')],
   };
   ```

4. Replace the content of App.css with the following

   ```css
   @tailwind base;

   @tailwind components;

   @tailwind utilities;
   ```

5. Add a build command to scripts in package.json

   `"build:css": "postcss src/App.css -o src/tailwind.css",`

6. Run `npm run build:css`
7. Add import statement to index.tsx

   `import './tailwind.css';`

8. Purge css:
   replace the code in postcss.config.js with the following:

```javascript
// The following is copied

// postcss.config.js
const purgecss = require('@fullhuman/postcss-purgecss')({
	// Specify the paths to all of the template files in your project
	content: ['./src/**/*.html', './src/**/*.tsx', './public/index.html'],

	// Include any special characters you're using in this regular expression
	defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
});

module.exports = {
	plugins: [
		require('tailwindcss'),
		require('autoprefixer'),
		...(process.env.NODE_ENV === 'production' ? [purgecss] : []),
	],
};
```

9. Add Tailwind to gitignore:
   `/src/tailwind-styles.css /src/tailwind.css`
