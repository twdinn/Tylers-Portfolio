// Tip Calculator
// By Tyler Dinn

// Get all the inputs (Global Access)

const billInput = document.getElementById("billTotalInput");
const tipInput = document.getElementById("tipInput");
const numPeople = document.getElementById("numberOfPeople");
const perPersonTotal = document.getElementById("perPersonTotal");

// Get number of people from numPeople input and convert to a number
let numberOfPeople = Number(numPeople.innerText);

// Calculate the total bill per person
const calculateBill = () => {
  // Get bill from billInput and convert to a number
  const bill = Number(billInput.value);

  // Get tip from tipInput and convert to number than percentage
  const tipPercent = Number(tipInput.value) / 100;

  // Add tip amount to bill
  const tipAmt = bill * tipPercent;
  const total = bill + tipAmt;

  // Divde by numberOfPeople to get totalPerPerson
  const totalPerPerson = total / numberOfPeople;

  // Update perPersonTotal in DOM

  perPersonTotal.innerText = `$${totalPerPerson.toFixed(2)}`;
};

// Increase number of people when clicked
const increasePeople = () => {
  // Increment numberOfPeople
  numberOfPeople += 1;

  // Update DOM
  numPeople.innerText = numberOfPeople;

  // Call calculateBill()
  calculateBill();
};

const decreasePeople = () => {
  // decrement numberOfPeople
  // Min number of people is 1

  if (numberOfPeople <= 1) {
    return;
  } else {
    numberOfPeople -= 1;

    // Update DOM
    numPeople.innerText = numberOfPeople;

    // Call calculateBill()
    calculateBill();
  }
};
