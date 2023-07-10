const N = 11; // number of cards to sort
const visibleNumbers = [];
let selectedCard = null;
let cycleTracker = {};
const $switch = document.querySelector('#switch')

// Create click and drag
const handleClick = (e) => {
  // get the right DOM element
  let $card = e.target;

  // Did they just want to see the card?
  let showCard = $card.innerHTML === "👀" ? true : false;

  // Regardless, get parent most div
  while (!$card.classList.contains("card")) {
    $card = $card.parentElement;
  }

  //Show the number value only show 3 cards at a time
  if (showCard && !visibleNumbers.includes($card)) {
    visibleNumbers.push($card);
    if (visibleNumbers.length > 3) {
      $hider = visibleNumbers.shift();
      $hider.classList.remove("is-visible");
    }
    $card.classList.add("is-visible");

    /** update observations and cycles */
    const cardValue = Number($card.children[1].innerHTML);
    $obs = document.querySelector("#obs");
    $obs.innerHTML = Number($obs.innerHTML) + 1;
    $cyc = document.querySelector("#cyc");
    cycleTracker[cardValue] += 1;
    if (cycleTracker[cardValue] > $cyc.innerHTML) {
      $cyc.innerHTML = cycleTracker[cardValue];
    }
  } else {
    if (!$card.classList.contains("is-empty")) {
      if (selectedCard) {
        selectedCard.classList.remove("is-selected");
      }
      selectedCard = $card;
      $card.classList.add("is-selected");
    } else if (selectedCard) {
      //move the card
      let $clone = $card.cloneNode(true);
      $clone.addEventListener("click", handleClick);
      selectedCard.before($clone);
      $card.parentNode.replaceChild(selectedCard, $card);
      // update moves
      $mvs = document.querySelector("#mvs");
      $mvs.innerHTML = Number($mvs.innerHTML) + 1;
      //check end game
    }
  }
};

// New blank box
const newEmpty = () => {
  const $node = document.createElement("div");
  $node.classList.add("card", "is-empty");
  $node.addEventListener("click", handleClick);
  $node.innerHTML = `<div class="card-content hold"></div>`;

  return $node;
};

// Create starting random numbers
const resetGame = (numOfCards = N, rangeOfValues = 1000) => {
  document.querySelector("#check-final").disabled = false;
  const $mainGrid = document.querySelector(".mainGrid");
  const $holdBoxes = document.querySelector("#hold-boxes");
  $mainGrid.innerHTML = "";
  $holdBoxes.innerHTML = "";
  cycleTracker = {};
  const bucketsCount = document.querySelector("#add-bucks").checked ? 11 : 1;

  for (let i = 0; i < numOfCards; i++) {
    let num = 0;
    while (!num || cycleTracker.hasOwnProperty(num)) {
      num = Math.floor(Math.random() * rangeOfValues);
    }

    const $node = document.createElement("div");
    $node.classList.add("card");
    $node.addEventListener("click", handleClick);
    $node.innerHTML = `<div id="icon">👀</div><div class="card-content">${num}</div>`;

    $mainGrid.appendChild($node);
    cycleTracker[num] = 0;
  }

  document.querySelectorAll("span").forEach((sp) => {
    sp.innerHTML = "0";
  });
  document.querySelector("#bku").innerHTML = bucketsCount;

  for (let i = 0; i < bucketsCount; i++) {
    $holdBoxes.appendChild(newEmpty());
  }
};

resetGame();

// restart button
document.querySelector("#reset").addEventListener("click", () => resetGame());

// large bucket check box
document
  .querySelector("#add-bucks")
  .addEventListener("change", () => {
    resetGame()
    $switch.classList.toggle('hide')
  });

const getGrade = (id) => {
  const $grade = document.querySelector(id);
  return Number($grade.innerHTML);
};

// When the array is sorted, end game!
document.querySelector("#check-final").addEventListener("click", (e) => {
  e.target.disabled = true;
  //check if list is sorted
  const $cards = document.querySelector(".mainGrid").children;
  const cardsOutOfOrder = [];
  let maxValue = -1;
  let finalScore = "∞";

  for (let i = 0; i < $cards.length; i++) {
    if ($cards[i].classList.contains("is-empty")) {
      cardsOutOfOrder.push($cards[i]);
    } else {
      const value = Number($cards[i].lastChild.innerHTML);
      if (value >= maxValue) {
        maxValue = value;
      } else {
        cardsOutOfOrder.push($cards[i]);
      }
    }
  }
  if (cardsOutOfOrder.length) {
    //highlight wrong cards
    cardsOutOfOrder.forEach(($card) => {
      $card.style.color = "red";
    });
    if(cardsOutOfOrder.length === N) {
      e.target.disabled = false;
      finalScore = 0
      alert("Be sure to swap your cards to the top row for final scoring. If they are, make sure they are sorted in ASCENDING order.")
    }
  } else {
    finalScore =
      2 * getGrade("#obs") +
      8 * getGrade("#cyc") +
      1 * getGrade("#mvs") +
      (getGrade("#bku") === 11? 1:0);
  }
  document.querySelector("#fin").innerHTML = finalScore;
});

$switch.addEventListener('click', (e)=>{
  $mainGrid = document.querySelector('.mainGrid')
  $holdBoxes = document.querySelector('#hold-boxes')
  mainClone = Array.from($mainGrid.children)
  holdClone = Array.from($holdBoxes.children)
  $mainGrid.innerHTML=''
  $holdBoxes.innerHTML=''
  holdClone.forEach(child=>{
    child.addEventListener('click', handleClick)
    $mainGrid.appendChild(child)
  })
  mainClone.forEach(child=>{
    child.addEventListener('click', handleClick)
    $holdBoxes.append(child)
  })
})