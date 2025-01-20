// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function () {
    // Select the HTML element where you want to display the fetched data
    const resultElement = document.getElementById("shareholders-list");

    // Function to fetch shareholder data from the API
    function fetchShareholders() {
        fetch('/api/shareholders')  // The Flask API route for fetching data
            .then(response => response.json())
            .then(data => {
                // Check if data is not empty
                if (data.length > 0) {
                    let htmlContent = '';
                    data.forEach(shareholder => {
                        // Generate HTML for each shareholder
                        htmlContent += `
                            <div class="shareholder">
                                <p>Name: ${shareholder.name}</p>
                                <p>Box Number: ${shareholder.box_number}</p>
                                <p>Civil ID: ${shareholder.civil_id}</p>
                                <p>Phone: ${shareholder.phone1}</p>
                            </div>
                        `;
                    });
                    resultElement.innerHTML = htmlContent;
                } else {
                    resultElement.innerHTML = "<p>No shareholders found.</p>";
                }
            })
            .catch(error => {
                resultElement.innerHTML = "<p>Error fetching data.</p>";
                console.error("Error fetching shareholders:", error);
            });
    }

    // Call the function to fetch the data
    fetchShareholders();
});
