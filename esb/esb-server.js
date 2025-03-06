require('dotenv').config();

const express = require('express');

// Initialize the app
const app = express();

// Request mapper
const mapper = '/api/v1';

// Middleware
app.use(express.json());
app.use((req, res, next) => {
    console.log(req.path, req.method);
    next();
});

// Services
const productServices = require('./routes/inventory-route');
const posServices = require('./routes/pos-routes');
const authService = require('./routes/auth-routes');
const employeeService = require('./routes/employee-route'); // Ensure this file exists

// Register routes
app.use(`${mapper}/employees`, employeeService);
app.use(`${mapper}/inventory`, productServices);
app.use(`${mapper}/pos`, posServices);
app.use(`${mapper}/auth`, authService);

// Start server
app.listen(process.env.PORT, () => {
    console.log(`Listening to port ${process.env.PORT}`);
});

// Handle invalid routes
app.use((req, res) => {
    res.status(404).json({ error: 'No such endpoint exists' });
});
