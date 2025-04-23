const bcrypt = require('bcrypt');
const User = require('../models/user.model');

exports.register = async (req, res) => {
  const { username, password, email, first_name, last_name } = req.body;

  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    await User.createUser({ username, email, first_name, last_name }, hashedPassword);
    res.status(201).json({ message: 'User registered successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.login = async (req, res) => {
  const { username, password } = req.body;

  try {
    const record = await User.getHashedPassword(username);
    if (!record) return res.status(400).json({ error: 'User not found' });

    const match = await bcrypt.compare(password, record.password);
    res.json({ message: match ? 'Login successful' : 'Invalid credentials' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.getAllUsers = async (_, res) => {
  const users = await User.getAllUsers();
  res.json(users);
};

exports.getUserById = async (req, res) => {
  const user = await User.getUserById(req.params.id);
  user ? res.json(user) : res.status(404).json({ error: 'User not found' });
};

exports.updateUser = async (req, res) => {
  try {
    await User.updateUser(req.params.id, req.body);
    res.json({ message: 'User updated' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
