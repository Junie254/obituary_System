document.getElementById('obituaryForm').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const dob = document.getElementById('date_of_birth').value;
    const dod = document.getElementById('date_of_death').value;
    const content = document.getElementById('content').value;
    const author = document.getElementById('author').value;

    if (!name || !dob || !dod || !content || !author) {
        alert('All fields are required.');
        event.preventDefault();
    }
});
