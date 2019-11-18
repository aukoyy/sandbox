const express = require('express');
const path = require('path');
const exphbs = require('express-handlebars');

const logger = require('./middleware/logger');
const members = require('./Members')

const app = express();
const PORT = process.env.PORT || 5000;


// INITIALIZE MIDDLEWARE
// app.use(logger);

// Body Parser Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));


// HANDLEBARS MIDDLEWARE
app.engine('handlebars', exphbs({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

// HANDLEBARS HOMEPAGE ROUTE
app.get('/', (req, res) => res.render('index', {
    title: 'Member App',
    members
}));


// HELLO WORLD
// app.get('/', (req, res) => res.send('<h1>Hello World</h1>'));

// SERVE A STATIC FILE
app.get('/file', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'))
});

// SERVE CURRENT FOLDER (QUICK SETUP)
app.use('/', express.static(__dirname));

// SET STATIC FOLDER - all files in this folder is accessable
// app.use(express.static(path.join(__dirname, 'public')));

// MEMBERS API ROUTES
app.use('/api/members', require('./routes/api/members'));

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));