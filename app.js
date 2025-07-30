const express = require('express');
const axios = require('axios');
const moment = require('moment');
const _ = require('lodash');

const app = express();
const port = 3000;

app.use(express.json());

// Vulnerable code examples (for testing purposes only)
app.get('/', (req, res) => {
    res.send('Vulnerable Test Application');
});

app.get('/api/data', async (req, res) => {
    try {
        // Using vulnerable packages
        const response = await axios.get('https://api.example.com/data');
        const data = _.merge({}, response.data);
        const timestamp = moment().format('YYYY-MM-DD HH:mm:ss');
        
        res.json({
            data: data,
            timestamp: timestamp,
            message: 'Data retrieved successfully'
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Vulnerable test app listening at http://localhost:${port}`);
}); 