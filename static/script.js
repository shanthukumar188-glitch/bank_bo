function addCustomer() {
    const name = document.getElementById("name").value;
    const balance = document.getElementById("balance").value;

    fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, balance })
    }).then(() => loadCustomers());
}

function loadCustomers() {
    fetch('/customers')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("list");
            list.innerHTML = "";
            data.forEach(c => {
                const li = document.createElement("li");
                li.innerText = `${c[1]} - ₹${c[2]}`;
                list.appendChild(li);
            });
        });
}