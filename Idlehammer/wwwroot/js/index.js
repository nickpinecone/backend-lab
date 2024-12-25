const threshold = 1;
let seconds = 0;
let clicks = 0;
let fromAbilities = 0;
const currentScoreElement = document.getElementById("current_score");
const recordScoreElement = document.getElementById("record_score");
const profitPerClickElement = document.getElementById("profit_per_click");
const profitPerSecondElement = document.getElementById("profit_per_second");
let currentScore = Number(currentScoreElement.innerText);
let recordScore = Number(recordScoreElement.innerText);
let profitPerSecond = Number(profitPerSecondElement.innerText);
let profitPerClick = Number(profitPerClickElement.innerText);


$(document).ready(function() {
    const clickitem = document.getElementById("clickitem");

    clickitem.onclick = click;
    setInterval(addSecond, 1000)

    const boostButtons = document.getElementsByClassName("boost-button");

    for (let i = 0; i < boostButtons.length; i++) {
        const boostButton = boostButtons[i];

        boostButton.onclick = () => boostButtonClick(boostButton);
    }

    const abilities = document.getElementsByClassName("ability");

    for (let i = 0; i < abilities.length; i++) {
        const ability = abilities[i];

        ability.onclick = () => {
            let charge = ability.querySelector(".boost-charge");
            let maxCharge = ability.querySelector(".max-charge");
            var id = ability.getAttribute("data-id");
            var quantity = Number(ability.parentNode.querySelector(".boost-quantity").innerText)
            var profit = Number(ability.getAttribute("data-profit")) * quantity * 10;

            if (id != "" && Number(charge.innerText) >= Number(maxCharge.innerText)) {
                currentScoreElement.innerText = Number(currentScoreElement.innerText) + profit;
                recordScoreElement.innerText = Number(recordScoreElement.innerText) + profit;
                fromAbilities += profit;
                charge.innerText = 0;
            }
        }
    }

    toggleBoostsAvailability();
})

function boostButtonClick(boostButton) {
    buyBoost(boostButton);
}

function buyBoost(boostButton) {
    const boostIdElement = boostButton.getElementsByClassName("boost-id")[0];
    const boostId = boostIdElement.innerText;

    $.ajax({
        url: '/boost/buy',
        method: 'post',
        dataType: 'json',
        data: { boostId: boostId },
        success: (response) => onBuyBoostSuccess(response, boostButton),
    });
}

function onBuyBoostSuccess(response, boostButton) {
    const score = response["score"];

    const boostPriceElement = boostButton.getElementsByClassName("boost-price")[0];
    const boostQuantityElement = boostButton.getElementsByClassName("boost-quantity")[0];

    const boostPrice = Number(response["price"]);
    const boostQuantity = Number(response["quantity"]);

    boostPriceElement.innerText = boostPrice;
    boostQuantityElement.innerText = boostQuantity;

    const ability = boostButton.parentNode.querySelector(".ability");
    ability.setAttribute("data-id", response["id"]);

    updateScoreFromApi(score);
}

function addSecond() {
    seconds++;

    const abilities = document.getElementsByClassName("ability");

    for (let i = 0; i < abilities.length; i++) {
        const ability = abilities[i];
        let charge = ability.querySelector(".boost-charge");
        let maxCharge = ability.querySelector(".max-charge");
        let id = ability.getAttribute("data-id")

        if (id != "" && Number(charge.innerText) < Number(maxCharge.innerText)) {
            charge.innerText = Number(charge.innerText) + 1;
        }
    }

    if (seconds >= threshold) {
        addPointsToScore();
    }

    if (seconds > 0) {
        addPointsFromSecond();
    }
}

function click() {
    clicks++;

    if (clicks >= threshold) {
        addPointsToScore();
    }

    if (clicks > 0) {
        addPointsFromClick();
    }
}

function updateScoreFromApi(scoreData) {
    currentScore = Number(scoreData["currentScore"]);
    recordScore = Number(scoreData["recordScore"]);
    profitPerClick = Number(scoreData["profitPerClick"]);
    profitPerSecond = Number(scoreData["profitPerSecond"]);

    updateUiScore();
}

function updateUiScore() {
    currentScoreElement.innerText = currentScore;
    recordScoreElement.innerText = recordScore;
    profitPerClickElement.innerText = profitPerClick;
    profitPerSecondElement.innerText = profitPerSecond;

    toggleBoostsAvailability();
}

function addPointsFromClick() {
    currentScore += profitPerClick;
    recordScore += profitPerClick;

    updateUiScore();
}

function addPointsFromSecond() {
    currentScore += profitPerSecond;
    recordScore += profitPerSecond;

    updateUiScore();
}

function addPointsToScore() {
    $.ajax({
        url: '/score',
        method: 'post',
        dataType: 'json',
        data: { clicks: clicks, seconds: seconds, fromAbilities: fromAbilities },
        success: (response) => onAddPointsSuccess(response),
    });
}

function onAddPointsSuccess(response) {
    seconds = 0;
    clicks = 0;

    updateScoreFromApi(response);
}

function toggleBoostsAvailability() {
    const boostButtons = document.getElementsByClassName("boost-button");

    for (let i = 0; i < boostButtons.length; i++) {
        const boostButton = boostButtons[i];

        const boostPriceElement = boostButton.getElementsByClassName("boost-price")[0];
        const boostPrice = Number(boostPriceElement.innerText);

        if (boostPrice > currentScore) {
            boostButton.disabled = true;
            continue;
        }

        boostButton.disabled = false;
    }
}
