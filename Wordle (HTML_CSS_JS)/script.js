let words = [];
let secretWord = "";
const secretWordDisplay = document.getElementById("secret-word-display");
const guessedLetters = [];
let incorrectGuesses = 0;

function initializeWords(category) {
    const categories = {
        fruits: ["apple", "banana", "orange", "grape", "strawberry", "kiwi"],
        animals: ["dog", "cat", "elephant", "lion", "giraffe", "monkey"],
        videoGames: ["forza", "minecraft", "fifa", "madden", "fortnite", "lego"],
        toys: ["doll", "robot", "lego", "train", "teddy"],
        cs50: ["python","edX", "sql", "flask", "http", "array"]
    };

    if (categories.hasOwnProperty(category)) {
        words = categories[category];
        secretWord = words[Math.floor(Math.random() * words.length)];
    } else {
        alert("Invalid category selected.");
    }
}

function submitGuess() {
    const categorySelect = document.getElementById("category-select");
    const selectedCategory = categorySelect.value;

    if (!words.length) {
        initializeWords(selectedCategory);
        updateSecretWordDisplay();
    }

    const guessInput = document.getElementById("guess-input");
    const guess = guessInput.value.toLowerCase();

    if (!isValidGuess(guess)) {
        alert("Please enter a single valid letter.");
        return;
    }

    if (secretWord.includes(guess)) {
        handleCorrectGuess(guess);
    } else {
        handleIncorrectGuess();
    }

    guessInput.value = "";
}

function isValidGuess(guess) {
    return guess.length === 1 && guess.match(/[a-z]/);
}

function updateSecretWordDisplay(guess) {
    const secretWordArray = secretWord.split("");
    const updatedDisplay = Array.from(secretWordArray).map(
        (letter) => (guessedLetters.includes(letter) ? letter : "_")
    ).join(" ");

    secretWordDisplay.textContent = updatedDisplay;
}

function handleCorrectGuess(guess) {
    guessedLetters.push(guess);
    updateSecretWordDisplay(guess);

    if (!secretWordDisplay.textContent.includes("_")) {
        alert("Congratulations! You guessed the word!");
        resetGame();
    }
}

function handleIncorrectGuess() {
    incorrectGuesses++;
    displayFeedback(`Incorrect guess! ${5 - incorrectGuesses} attempts remaining.`);
    if (incorrectGuesses === 5) {
        alert(`Sorry, you ran out of attempts. The correct word was "${secretWord}".`);
        resetGame();
    }
}

function displayFeedback(message) {
    const feedbackElement = document.getElementById("feedback");
    feedbackElement.textContent = message;
}

function resetGame() {
    words = [];
    secretWord = "";
    guessedLetters.length = 0;
    incorrectGuesses = 0;
    document.getElementById("guess-input").disabled = false;
    document.querySelector("button").disabled = false;
    document.getElementById("category-select").value = "";
    document.getElementById("feedback").textContent = "";
    document.getElementById("secret-word-display").textContent = "";
}
