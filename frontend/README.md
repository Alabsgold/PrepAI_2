# PrepAI Frontend

This is the SvelteKit frontend for the PrepAI application.

## GitHub Pages Deployment

To deploy this application to GitHub Pages, you need to update the `base` path in the `svelte.config.js` file.

1.  Open `frontend/svelte.config.js`.
2.  Find the `paths` configuration.
3.  Replace `'your-repo-name'` with the name of your GitHub repository.

```javascript
// svelte.config.js
paths: {
    base: process.env.NODE_ENV === 'production' ? '/your-repo-name' : '',
}
```

## Deploying to GitHub Pages

1.  **Build the application:**
    ```bash
    cd frontend
    npm run build
    ```
2.  **Deploy the `build` directory to GitHub Pages.**
    You can use the `gh-pages` package to simplify this process.
    - Install `gh-pages`: `npm install -D gh-pages`
    - Add a `deploy` script to your `package.json`:
      ```json
      "scripts": {
        "deploy": "gh-pages -d build -t true"
      }
      ```
    - Run the deploy script: `npm run deploy`
