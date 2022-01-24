const feedbackForm = document.getElementById("feedback-form");
feedbackForm.addEventListener(("submit"), (event) => {
    event.preventDefault();
    console.log("submitting form....");
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const given_by = document.querySelector('[name=given_by]').value;
    const feedbackMessage = document.querySelector('[name=feedback_message]').value;
    const about = document.querySelector('[name=about]').value;

    // Make POST request to backend
    fetch(feedbackUrl, {
        headers: { 
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        method: 'POST',
        mode: 'same-origin',
        body: JSON.stringify({
            "given_by": given_by,
            "feedback_message": feedbackMessage,
            "about": about
        })
    })
    .then(response => {
        console.log(response);
        alert("Feedback sent successfully");
        // Reset fields
        document.querySelector('[name=given_by]').value = "";
        document.querySelector('[name=feedback_message]').value = "";
    })
    .catch(error => console.error(error));
});