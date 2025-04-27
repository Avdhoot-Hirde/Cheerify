
let pendingReview = "";

function submitReview() {
    const input = document.getElementById("reviewInput").value;
    if (!input.trim()) return;

    fetch('/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: input, stage: 'initial' })
    })
    .then(res => res.json())
    .then(data => {
        if (data.ask_confirmation) {
            pendingReview = input;
            document.getElementById("popupText").innerText = `We detected a negative tone. Do you want to use this instead?\n\n"${data.transformed}"`;
            document.getElementById("popup").style.display = 'block';
        } else if (data.done) {
            addReviewToList(data.review);
            document.getElementById("reviewInput").value = '';
        }
    });
}

function confirmTransformation(confirm) {
    document.getElementById("popup").style.display = 'none';
    fetch('/review', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: pendingReview, stage: 'confirmation', confirm: confirm })
    })
    .then(res => res.json())
    .then(data => {
        if (data.done) {
            addReviewToList(data.review);
            document.getElementById("reviewInput").value = '';
        }
    });
}

function addReviewToList(review) {
    const list = document.getElementById("reviewList");
    const li = document.createElement("li");
    li.textContent = review + " (just now)";
    list.prepend(li);
}
