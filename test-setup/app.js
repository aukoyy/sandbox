const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

const heyy = 'Hello from backend 2000';

const configureAccessControl = (req, res, next) => {
    res.header('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    res.header('Access-Control-Expose-Headers', 'authorization');
    res.header('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE');
    next();
};

app.use(configureAccessControl)

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'))
});

app.get('/hey', (req, res) => {
    res.status(200).send(JSON.stringify({ hey: heyy }));
});

app.listen(PORT, () => console.log(`Server started. Listening on port: ${PORT}`));