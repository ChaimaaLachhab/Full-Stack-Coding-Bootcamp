const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

const PORT = 3000;
app.use(express.static(path.join(__dirname, 'public')));

const users = {};

io.on('connection', (socket) => {
  console.log('New user connected');

  socket.on('joinRoom', ({ username, room }) => {
    users[socket.id] = { username, room };
    socket.join(room);

    socket.emit('message', { user: 'System', text: `Welcome ${username}!` });

    socket.to(room).emit('message', { user: 'System', text: `${username} has joined.` });

    updateUsersInRoom(room);
  });

  socket.on('chatMessage', (msg) => {
    const user = users[socket.id];
    if (user) {
      io.to(user.room).emit('message', { user: user.username, text: msg });
    }
  });

  socket.on('disconnect', () => {
    const user = users[socket.id];
    if (user) {
      const { username, room } = user;
      socket.to(room).emit('message', { user: 'System', text: `${username} left.` });
      delete users[socket.id];
      updateUsersInRoom(room);
    }
  });

  function updateUsersInRoom(room) {
    const roomUsers = Object.values(users).filter(u => u.room === room).map(u => u.username);
    io.to(room).emit('roomUsers', roomUsers);
  }
});

server.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
