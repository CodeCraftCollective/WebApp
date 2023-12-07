let incorrectGuesses = 0;
const maxGuesses = 6;
const words = ["Good morning", "Hello world", "Programming", "Javascript", "Django", "Hangman"]; // List of words
let currentWord = '';

document.addEventListener("DOMContentLoaded", () => {
    const resetButton = document.getElementById('resetButton');
    resetButton.addEventListener('click', resetGame);
    initializeGame();
});

function initializeGame() {
    currentWord = getRandomWord().toUpperCase();
    incorrectGuesses = 0;
    updateDisplayedWord();
    createOrUpdateButtons();
    updateImage(incorrectGuesses);
}

function getRandomWord() {
    return words[Math.floor(Math.random() * words.length)];
}

function resetGame() {
    document.querySelectorAll('#letterRow1 button, #letterRow2 button, #numberRow button').forEach(btn => btn.disabled = false);
    initializeGame();
}

function updateDisplayedWord() {
    const wordDisplay = document.getElementById('wordDisplay');
    let displayedWord = Array.from(currentWord).map(char => char === ' ' ? ' ' : '_').join(' ');
    wordDisplay.innerText = displayedWord;
}

function createOrUpdateButtons() {
    const letterRow1 = document.getElementById('letterRow1');
    const letterRow2 = document.getElementById('letterRow2');
    const numberRow = document.getElementById('numberRow');

    letterRow1.innerHTML = '';
    letterRow2.innerHTML = '';
    numberRow.innerHTML = '';

    createButtons('A'.charCodeAt(0), 'M'.charCodeAt(0), letterRow1);
    createButtons('N'.charCodeAt(0), 'Z'.charCodeAt(0), letterRow2);
    createButtons('0'.charCodeAt(0), '9'.charCodeAt(0), numberRow);
}

function createButtons(startCode, endCode, container) {
    for (let charCode = startCode; charCode <= endCode; charCode++) {
        let btn = document.createElement('button');
        let character = String.fromCharCode(charCode);
        btn.innerText = character;

        btn.addEventListener('click', () => handleLetterClick(btn, character));

        container.appendChild(btn);
    }
}

function handleLetterClick(button, character) {
    button.disabled = true; // Disable the button instead of hiding

    let guessIsCorrect = false;
    const wordDisplay = document.getElementById('wordDisplay');
    let updatedWordArray = wordDisplay.innerText.split(' ');

    for (let i = 0; i < currentWord.length; i++) {
        if (currentWord[i] === character) {
            updatedWordArray[i] = character;
            guessIsCorrect = true;
        }
    }

    wordDisplay.innerText = updatedWordArray.join(' ');

    if (!guessIsCorrect) {
        incorrectGuesses++;
        updateImage(incorrectGuesses); // Update the image on incorrect guess

        if (incorrectGuesses >= maxGuesses) {
            alert('Game Over! You have exceeded the maximum number of guesses.');
            disableAllButtonsExceptReset();
        }
    } else if (allCharactersGuessed(updatedWordArray, currentWord)) {
        alert('Congratulations! You guessed the word!');
        disableAllButtonsExceptReset();
    }
}

function allCharactersGuessed(displayArray, originalWord) {
    return displayArray.every((char, index) => char === originalWord[index] || originalWord[index] === ' ');
}

function updateImage(guesses) {
    const imageName = (maxGuesses - guesses) + '.png'; // Calculate image name based on guesses
    const imagePath = '/static/hangman/' + imageName; // Update path as per Django's static file structure
    document.getElementById('hangmanImage').src = imagePath;
}

function disableAllButtonsExceptReset() {
    document.querySelectorAll('#letterRow1 button, #letterRow2 button, #numberRow button').forEach(btn => btn.disabled = true);
}