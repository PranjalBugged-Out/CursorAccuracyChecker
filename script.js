let startTime, endTime;
let clicks = 0;

function startTest() {
    clicks = 0;
    startTime = new Date().getTime();
    document.getElementById("accuracyResult").innerText = "Click inside the box as quickly as possible!";
}

function registerClick() {
    if (!startTime) return;
    
    clicks++;
    if (clicks >= 10) {
        endTime = new Date().getTime();
        let timeTaken = (endTime - startTime) / 1000;
        let accuracy = (10 / timeTaken).toFixed(2);
        document.getElementById("accuracyResult").innerText = `Accuracy Score: ${accuracy} clicks per second`;
        startTime = null;
    }
}
