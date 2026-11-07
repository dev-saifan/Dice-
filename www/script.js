const resultEl = document.getElementById('result');
const infoEl = document.getElementById('info');
const rollBtn = document.getElementById('rollBtn');

rollBtn.addEventListener('click', () => {
    rollBtn.disabled = true;
    infoEl.textContent = "Rolling...";
    resultEl.classList.add('shake');

    let steps = 0;
    const maxSteps = 10; // Total shuffle ticks
    const intervalTime = 50; // Speed of shuffle in ms

    const shuffleInterval = setInterval(() => {
        const tempRoll = Math.floor(Math.random() * 6) + 1;
        resultEl.textContent = tempRoll;
        steps++;

        if (steps >= maxSteps) {
            clearInterval(shuffleInterval);
            const finalRoll = Math.floor(Math.random() * 6) + 1;
            resultEl.textContent = finalRoll;
            resultEl.classList.remove('shake');
            infoEl.textContent = `You rolled a ${finalRoll}!`;
            rollBtn.disabled = false;
        }
    }, intervalTime);
});
