const express = require('express');
const axios = require('axios');
const router = express.Router();

// Define Employee Service URL (Flask API)
const EMPLOYEE_SERVICE_URL = 'http://localhost:5000';

// Fetch All Employees
router.get('/', async (req, res) => {
    try {
        const response = await axios.get(`${EMPLOYEE_SERVICE_URL}/employees`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch employees', details: error.message });
    }
});

// Add Employee
router.post('/', async (req, res) => {
    try {
        const response = await axios.post(`${EMPLOYEE_SERVICE_URL}/employee`, req.body);
        res.status(response.status).json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to add employee', details: error.message });
    }
});

// Delete Employee
router.delete('/:email', async (req, res) => {
    try {
        const response = await axios.delete(`${EMPLOYEE_SERVICE_URL}/employee/${req.params.email}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to delete employee', details: error.message });
    }
});

module.exports = router;
