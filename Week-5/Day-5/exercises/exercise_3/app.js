const express = require('express');
const { fetchPosts } = require('./data/dataService');

const app = express();
const PORT = 5000;

app.get('/api/posts', async (req, res) => {
  try {
    const posts = await fetchPosts();
    console.log('Data fetched and sent');
    res.json(posts);
  } catch (err) {
    console.error('Error fetching data:', err);
    res.status(500).send('Server Error');
  }
});

app.listen(PORT, () => {
  console.log(`🔌 CRUD API using Axios running on http://localhost:${PORT}`);
});
