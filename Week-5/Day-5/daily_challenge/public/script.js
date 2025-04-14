let score = 0;
const player = prompt("Enter your name") || "Anonymous";

async function loadQuestion() {
  const res = await fetch('/api/question');
  const data = await res.json();

  document.getElementById('emoji').textContent = data.emoji;
  const optionsDiv = document.getElementById('options');
  optionsDiv.innerHTML = '';

  data.options.forEach(opt => {
    const btn = document.createElement('button');
    btn.textContent = opt;
    btn.onclick = () => submitGuess(opt);
    optionsDiv.appendChild(btn);
  });
}

async function submitGuess(guess) {
  const res = await fetch('/api/guess', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ guess, player })
  });

  const data = await res.json();
  document.getElementById('feedback').textContent =
    data.correct ? 'Correct!' : 'Wrong!';
  document.getElementById('score').textContent = data.score;
  updateLeaderboard();
  setTimeout(() => {
    document.getElementById('feedback').textContent = '';
    loadQuestion();
  }, 1000);
}

async function updateLeaderboard() {
  const res = await fetch('/api/leaderboard');
  const leaders = await res.json();

  const ul = document.getElementById('leaderboard');
  ul.innerHTML = '';
  leaders.forEach(l => {
    const li = document.createElement('li');
    li.textContent = `${l.name}: ${l.score}`;
    ul.appendChild(li);
  });
}

loadQuestion();
updateLeaderboard();
