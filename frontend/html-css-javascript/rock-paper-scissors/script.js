// Rock Paper Scissors
// Tyler Dinn

const totalScore = { playerScore: 0 };

// randomly select computer choice and return a string
// getComputerChoice() -> rock
// getComputerChoice() -> paper
const getComputerChoice = () => {
  const gameChoices = ["Rock", "Paper", "Scissors"];
  const choice = Math.floor(Math.random() * 3);
  return gameChoices[choice];
};

// getresult compares player and computer choices
const getResult = (playerChoice, computerChoice) => {
  // return the result of score based on win lose or draw.
  let score;
  let computScore;
  // if player draws score is 0
  if (playerChoice === computerChoice) {
    score = 0;

    // if player wins score is 1
  } else if (
    (playerChoice === "Rock" && computerChoice === "Scissors") ||
    (playerChoice === "Paper" && computerChoice === "Rock") ||
    (playerChoice === "Scissors" && computerChoice === "Paper")
  ) {
    score = 1;

    // if none of the above then you lose and score is -1
  } else {
    score = -1;
  }
  return score;
};

// update DOM with player choice, computer choice and win lose or draw based on score
const showResult = (score, playerChoice, computerChoice) => {
  const playerScore = document.getElementById("player-score");
  const hands = document.getElementById("hands");
  const result = document.getElementById("result");

  if (score == 0) {
    result.innerText = "It's a Tie!";
    // console.log("It's a Tie!");
  } else if (score == -1) {
    result.innerText = "You Lose!";
    // console.log("You Lose!");
  } else {
    result.innerText = "You Win!";
    // console.log("You Win!");
  }

  hands.innerText = `👱‍♂️ ${playerChoice} vs 🤖 ${computerChoice}`;

  playerScore.innerText = `Player Score: ${totalScore["playerScore"]}`;
};

// playerChoice = btnClick.value from playgame()
// show on screen
onClickGameChoice = (playerChoice) => {
  console.log({ playerChoice });
  // get computerChoice by calling getComputerChoice()
  const computerChoice = getComputerChoice();

  // get result of game by calling getResult(playerChoice, computerChoice)
  const score = getResult(playerChoice, computerChoice);

  // add score to totalScore object
  totalScore["playerScore"] += score;

  // show
  showResult(score, playerChoice, computerChoice);
};

// Listen for a click and do somthing
const playGame = () => {
  // select all buttons
  const btnClick = document.querySelectorAll(".play-option");

  // loop through btns and add onclick event listener to each btn
  // call onClickGameChoice(current selected btn) every click
  btnClick.forEach((btnClick) => {
    btnClick.onclick = () => onClickGameChoice(btnClick.value);
  });
};

const endBtn = document.getElementById("stop");
endBtn.onclick = () => endGame(totalScore);

const endGame = (totalScore) => {
  totalScore["playerScore"] = 0;
  totalScore["computerScore"] = 0;

  let playerScore = document.getElementById("player-score");
  let hands = document.getElementById("hands");
  let result = document.getElementById("result");

  hands.innerText = "";
  playerScore.innerText = "";
  result.innerText = "";
};

playGame();
