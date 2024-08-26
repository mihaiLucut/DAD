// static/js/todo.js

document.addEventListener('DOMContentLoaded', function () {
    const completeButtons = document.querySelectorAll('.mark-complete-btn');
    const timerButtons = document.querySelectorAll('.start-timer-btn');

    completeButtons.forEach(button => {
        button.addEventListener('click', function () {
            this.parentElement.style.textDecoration = 'line-through';
            this.parentElement.style.color = '#aaa';
            this.innerHTML = 'Completed';
            this.disabled = true;

            // Play a cheerful sound
            let audio = new Audio('/static/audio/cheerful-tune.mp3');
            audio.play();
        });
    });

    timerButtons.forEach(button => {
        button.addEventListener