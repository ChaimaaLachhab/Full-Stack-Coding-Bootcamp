let current = 0;
let score = 0;
let answered = false; // empêche de répondre plusieurs fois

async function loadQuestion(index) {
  const res = await fetch(`/api/questions/next/${index}`);
  if (!res.ok) {
    document.getElementById('quiz-container').innerHTML = `<h2>🎉 Quiz terminé !<br/>Score final : ${score}</h2>`;
    return;
  }

  const data = await res.json();
  const questionElement = document.getElementById('question');
  const optionsContainer = document.getElementById('options');
  const feedback = document.getElementById('feedback');

  questionElement.textContent = data.question.question;
  optionsContainer.innerHTML = '';
  feedback.textContent = '';
  answered = false;

  data.options.forEach(opt => {
    const btn = document.createElement('button');
    btn.textContent = opt.option;
    btn.disabled = false;
    btn.onclick = async () => {
      if (answered) return;
      answered = true;

      const res = await fetch('/api/questions/answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ questionId: data.question.id, selectedOption: opt.option })
      });

      const result = await res.json();

      if (result.correct) {
        score++;
        feedback.textContent = '✅ Bonne réponse !';
        btn.style.backgroundColor = '#28a745';
      } else {
        feedback.textContent = '❌ Mauvaise réponse.';
        btn.style.backgroundColor = '#dc3545';
      }

      // Désactiver tous les boutons après réponse
      document.querySelectorAll('#options button').forEach(b => b.disabled = true);

      // Afficher le score
      document.getElementById('score').textContent = `Score: ${score}`;
    };
    optionsContainer.appendChild(btn);
  });
}

function nextQuestion() {
  const feedback = document.getElementById('feedback');
  if (!answered) {
    feedback.textContent = 'Veuillez répondre à la question avant de continuer.';
    return;
  }
  current++;
  loadQuestion(current);
}

loadQuestion(current);
