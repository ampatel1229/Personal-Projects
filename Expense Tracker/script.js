const expenseTableBody = document.getElementById("expenseTableBody");
const totalAmount = document.getElementById("totalAmount");
let expenses = [];

function addExpense() {
  const item = document.getElementById("item").value;
  const amount = parseFloat(document.getElementById("amount").value);

  if (item && amount) {
    const expense = {
      item,
      amount
    };
    expenses.push(expense);
    displayExpenses();
    clearForm();
    updateTotal();
  }
}

function displayExpenses() {
  expenseTableBody.innerHTML = "";
  expenses.forEach(expense => {
    const row = document.createElement("tr");
    const itemCell = document.createElement("td");
    itemCell.textContent = expense.item;
    row.appendChild(itemCell);
    const amountCell = document.createElement("td");
    amountCell.textContent = "$" + expense.amount.toFixed(2);
    row.appendChild(amountCell);
    expenseTableBody.appendChild(row);
  });
}

function clearForm() {
  document.getElementById("item").value = "";
  document.getElementById("amount").value = "";
}

function updateTotal() {
  const total = expenses.reduce((accumulator, currentValue) => {
    return accumulator + currentValue.amount;
  }, 0);
  totalAmount.textContent = total.toFixed(2);
}
