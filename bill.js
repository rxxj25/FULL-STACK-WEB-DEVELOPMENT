document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("billForm");
    const resultDiv = document.getElementById("result");
    const MAINTENANCE_FEE = 1000;

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Generate random values for electricity usage and water usage
        const electricityUsage = getRandomValue(0, 100); // Assuming maximum usage is 100 kWh
        const waterUsage = getRandomValue(0, 50); // Assuming maximum usage is 50 gallons

        const electricityBill = electricityUsage * 1.2;
        const waterBill = waterUsage * 2;
        const totalBill = electricityBill + waterBill + MAINTENANCE_FEE;

        resultDiv.innerHTML = `
            <h2>Bill Summary</h2>
            <p>Electricity Bill: Rs${electricityBill.toFixed(2)}</p>
            <p>Water Bill: Rs${waterBill.toFixed(2)}</p>
            <p>Maintenance Fee: Rs${MAINTENANCE_FEE.toFixed(2)}</p>
            <p><strong>Total Bill: Rs${totalBill.toFixed(2)}</strong></p>
        `;

        // Show the result box
        resultDiv.classList.remove("hidden");
    });

    // Function to generate random value within a range
    function getRandomValue(min, max) {
        return Math.random() * (max - min) + min;
    }
});
