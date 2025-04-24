const express = require('express');
const bcrypt = require('bcrypt');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

const usersFilePath = path.join(__dirname, 'users.json');

const readUsers = () => {
  try {
    const data = fs.readFileSync(usersFilePath, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    return [];
  }
};

const writeUsers = (users) => {
  try {
    fs.writeFileSync(usersFilePath, JSON.stringify(users, null, 2));
  } catch (err) {
    console.error('Erreur d\'écriture dans le fichier :', err);
  }
};

app.post('/register', async (req, res) => {
  const { name, 'last-name': lastName, email, username, password } = req.body;
  const users = readUsers();

  const usernameExists = users.some(user => user.username === username);
  if (usernameExists) {
    return res.json({ message: 'Erreur : Le nom d\'utilisateur existe déjà.' });
  }

  const hashedPassword = await bcrypt.hash(password, 10);

  const newUser = { name, lastName, email, username, password: hashedPassword };
  users.push(newUser);
  writeUsers(users);

  res.json({ message: 'Utilisateur enregistré avec succès !' });
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const users = readUsers();

  const user = users.find(user => user.username === username);
  if (!user) {
    return res.json({ message: 'Erreur : Utilisateur non trouvé.' });
  }

  const passwordMatch = bcrypt.compareSync(password, user.password);
  if (!passwordMatch) {
    return res.json({ message: 'Erreur : Mot de passe incorrect.' });
  }

  res.json({ message: 'Connexion réussie !' });
});

app.listen(port, () => {
  console.log(`Serveur en cours d'exécution sur http://localhost:${port}`);
});
