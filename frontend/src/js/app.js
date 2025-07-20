
document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const inputText = document.getElementById("userInput").value.trim();
  const result = document.getElementById("result");

  // Clear previous result styling
  result.classList.remove("text-red-600");

  if (!inputText) {
    result.textContent = "Please enter something about your mood.";
    result.classList.remove("hidden");
    result.classList.add("text-red-600");
    return;
  }

  try {
    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: inputText }),
    });

    const data = await response.json();

    result.textContent = data.predicted_mood
      ? `Predicted Mood: ${data.predicted_mood}`
      : `Error: ${data.error || 'Unknown error'}`;
    result.classList.remove("hidden");

  } catch (error) {
    result.textContent = "Error: Unable to connect to the prediction server.";
    result.classList.remove("hidden");
    result.classList.add("text-red-600");
    console.error(error);
  }
});


