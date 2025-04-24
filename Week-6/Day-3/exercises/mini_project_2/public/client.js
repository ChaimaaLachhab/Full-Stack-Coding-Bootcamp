const socket = io();
const params = new URLSearchParams(window.location.search);
const username = params.get('username');
const room = params.get('room');

socket.emit('joinRoom', { username, room });

socket.on('message', (data) => {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message');
  msgDiv.innerHTML = `<strong>${data.user}:</strong> ${data.text}`;
  document.getElementById('messages').appendChild(msgDiv);
});

socket.on('roomUsers', (users) => {
  const userList = document.getElementById('users');
  userList.innerHTML = '';
  users.forEach(u => {
    const li = document.createElement('li');
    li.textContent = u;
    userList.appendChild(li);
  });
});

document.getElementById('chat-form').addEventListener('submit', function (e) {
  e.preventDefault();
  const msg = document.getElementById('msg').value;
  socket.emit('chatMessage', msg);
  document.getElementById('msg').value = '';
});
