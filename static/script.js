document.addEventListener("DOMContentLoaded", function () {
    const resultDiv = document.getElementById("result");

    if (resultDiv && resultDiv.innerText.trim() !== "") {
        resultDiv.style.opacity = 0;
        setTimeout(() => {
            resultDiv.style.transition = "opacity 1s";
            resultDiv.style.opacity = 1;
        }, 200);
    }
});
