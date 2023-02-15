
function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
};
function refresh() {
    location.reload();
}
function win(){
    var element = getElementById("gameContainer");
    element.classList.remove("gameContainer");
    element.classList.add("win");
}


let wordlist = ['word','hour','work','play','game','love','life','time','home','book','face','name','data','code','text',]

let gameState = {
    gameGrid: Array(4)
        .fill()
        .map(() => Array(4).fill('')),
    currentRow: 0,
    currentCol: 0,
    hiddenWord: wordlist[Math.floor(Math.random() * wordlist.length)]
}

function init() {
    const gameContainer = document.getElementById("gameContainer");
    makeGameGrid(gameContainer);
    console.log(gameState.hiddenWord);
    keyboardpresses();
}
function makeGameGrid(gameContainer) {
    const gameGrid = document.createElement("div");
    gameGrid.className = 'gameGrid';
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            makeBox(gameGrid, i, j);
        }
    }
    gameContainer.appendChild(gameGrid);

}
function makeBox(gameGrid, i, j, letter = '') {
    const charBox = document.createElement("div");
    charBox.className = "charBox";
    charBox.id = 'charBox.' + i + '' + j;
    charBox.textContent = letter;
    gameGrid.appendChild(charBox);
    return charBox;
}
function keyboardpresses() {
    document.body.onkeydown = (e) =>{
        let key = e.key;
        displaykey(key);
        if (key === "Enter") {
            while (gameState.currentCol < 4) {
                alert("Please enter a word of 4 letters")
                return;
            }
            let word = getEnteredWord();
            checkletters();
            checkTurn(word);
            gameState.currentRow++;
            gameState.currentCol = 0;
        }
        if (key === "Backspace") {
            deleteletter();
        }
        if (isAlpha(key)) {
            addLetter(key);

        }
        updateGameGrid();
    }
} 
function displaykey(key) {
    
}
function checkTurn(word) {
    let won = gameState.hiddenWord === word
    let gameOver = gameState.currentRow === 3;
    if (won) {
        alert("You win!");
    } else if (gameOver) {
        alert("You lose! the word was " + gameState.hiddenWord + ".");
    }
}
function isvalid(word) {
    return wordlist.includes(word);
}
function checkletters(){
    for (let i = 0; i < 4; i++) {
        let charBox = document.getElementById('charBox.' + gameState.currentRow + '' + i);
        let letter = charBox.textContent;
        if (letter == gameState.hiddenWord[i]) {
            charBox.classList.add('correct');
        } else if(gameState.hiddenWord.includes(letter)){
            charBox.classList.add('contains');
        }else{
            charBox.classList.add('empty');
        }
    }
}
function getEnteredWord() {
    return gameState.gameGrid[gameState.currentRow].reduce((previous,current) => previous + current);
}
function updateGameGrid() {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            let charBox = document.getElementById('charBox.' + i + '' + j);
            charBox.textContent = gameState.gameGrid[i][j];
        }
    }

}
function isAlpha(key) {
    return key.length === 1 && key.match(/[a-z]/i);
}
function deleteletter(){
    if (gameState.currentCol === 0) return;
    gameState.gameGrid[gameState.currentRow][gameState.currentCol-1] = "";
    gameState.currentCol--;
}

function addLetter(key){
    if (gameState.currentCol === 4) return;
    gameState.gameGrid[gameState.currentRow][gameState.currentCol] = key;
    gameState.currentCol++;
}

init();