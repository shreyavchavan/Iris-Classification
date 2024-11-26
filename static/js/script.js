document.getElementById("classification-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const sepalLength = parseFloat(document.getElementById("sepal-length").value);
  const sepalWidth = parseFloat(document.getElementById("sepal-width").value);
  const petalLength = parseFloat(document.getElementById("petal-length").value);
  const petalWidth = parseFloat(document.getElementById("petal-width").value);

  const features = [sepalLength, sepalWidth, petalLength, petalWidth];

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features }),
    });

    const result = await response.json();

    if (response.ok) {
      document.getElementById("result").classList.remove("hidden");
      document.getElementById("result").innerHTML = `Prediction: ${result.prediction}`;
    } else {
      alert(result.error || "Error making prediction");
    }
  } catch (error) {
    alert("An error occurred while making the request.");
  }
});
