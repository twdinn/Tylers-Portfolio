var orderSubmitted = () => {
  var order = document.createElement("h1");
  order.textContent = "Your order Was Submitted";

  var message = document.getElementById("order-form");
  message.appendChild(order);
};
