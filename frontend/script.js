const API_URL = "http://localhost:5000";

let cart = [];


// Load products from backend
async function loadProducts() {

    try {

        const response =
            await fetch(`${API_URL}/api/products`);

        const products =
            await response.json();

        displayProducts(products);

    } catch (error) {

        console.error("Error:", error);

        document.getElementById("product-container")
            .innerHTML =
            "<p>Unable to load products.</p>";
    }
}


// Display products
function displayProducts(products) {

    const container =
        document.getElementById("product-container");

    container.innerHTML = "";

    products.forEach(product => {

        const productDiv =
            document.createElement("div");

        productDiv.className = "product";

        productDiv.innerHTML = `

            <h3>${product.name}</h3>

            <p>${product.description}</p>

            <div class="price">
                ₹${product.price}
            </div>

            <button onclick="addToCart(${product.id}, '${product.name}', ${product.price})">
                Add to Cart
            </button>

        `;

        container.appendChild(productDiv);

    });
}


// Add product to cart
function addToCart(id, name, price) {

    cart.push({
        id: id,
        name: name,
        price: price
    });

    updateCart();

}


// Update cart
function updateCart() {

    const container =
        document.getElementById("cart-container");

    const count =
        document.getElementById("cart-count");

    const total =
        document.getElementById("cart-total");


    count.innerText = cart.length;


    if (cart.length === 0) {

        container.innerHTML =
            "<p>Your cart is empty.</p>";

        total.innerText = "0";

        return;
    }


    container.innerHTML = "";


    let cartTotal = 0;


    cart.forEach((item, index) => {

        cartTotal += Number(item.price);

        const div =
            document.createElement("div");

        div.innerHTML = `

            <p>
                ${item.name}
                - ₹${item.price}

                <button onclick="removeFromCart(${index})">
                    Remove
                </button>
            </p>

        `;

        container.appendChild(div);

    });


    total.innerText = cartTotal;

}


// Remove product
function removeFromCart(index) {

    cart.splice(index, 1);

    updateCart();

}


// Automatically load products
loadProducts();
