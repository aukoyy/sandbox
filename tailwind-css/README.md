## How to implement tailwind
See official instructions: [Tailwind Installation Docs](https://tailwindcss.com/docs/installation)


## Steps to implement tailwind in a React project
1. Install Tailwind with NPM

    `npm install tailwindcss`
    
2. Copy the preflight code into app.css file:
    ```
        @tailwind base;
        
        @tailwind components;
        
        @tailwind utilities;
    ```
3. Add a build command to scripts in package.json

    `"build:css": "tailwind build src/app.css -o src/tailwind-styles.css",`
    
4. Run `npm run build:css`
5. Add import statement to index.tsx 

    `import './tailwind-styles.css';`
6. Create a config file (Optional)
    
    `npx tailwind init`