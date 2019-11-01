const express = require('express');
const app = express();
const port = 5000;

app.get('/', (req, res) => res.send('Hello World!'));
// app.get('/tail', express.static(path.join(__dirname, 'dist/index.html')));
app.use(express.static('dist'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`));