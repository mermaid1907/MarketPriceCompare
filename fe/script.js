const dataUserCardTemplate = document.querySelector("[data-user-card-template]");
const dataUserCardsContainer = document.querySelector("[data-user-cards-container]");
const searchInput = document.querySelector("[data-search]")

let products = []

// searchInput.addEventListener("input", e => {
//     const value = e.target.value
//     console.log(value)
//     products.forEach(product => {
//         const isVisible = product.productName.includes(value) || product.price.includes(value)
//         product.element.classList.toggle("hide", !isVisible)
//     })
// })

searchInput.addEventListener("input", function (e){
    const productName = document.querySelectorAll(".header")
    const search = searchInput.value.toLowerCase();

    productName.forEach((productName) => {
        productName.parentElement.style.display = "block";
        if(!productName.innerHTML.toLowerCase().includes(search)){
            productName.parentElement .style.display = "none";
        }
    });

    console.log(search);
})

fetch("http://localhost:8080/products")
.then(res => res.json())
.then(data => {
    products = data.map(product => {
        const card = dataUserCardTemplate.content.cloneNode(true).children[0]
        const header = card.querySelector("[data-header]")
        const body = card.querySelector("[data-body]")
        header.textContent = product.productName
        body.textContent = product.price
        dataUserCardsContainer.append(card)
        return {name: product.productName, price: product.price, element: card}
    })
    
})