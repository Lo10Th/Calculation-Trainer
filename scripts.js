function checkAnswer(selectedAnswer) {
    const correctAnswer = "{{answer}}";
    const Element = document.getElementById("ifcorrect");
    if (selectedAnswer === correctAnswer) {
        Element.innerHTML = "Correct!";
    } else {
        Element.innerHTML = "Wrong!";
    }
}