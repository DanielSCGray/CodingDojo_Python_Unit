async function pourDrink() {
    
    let result = await fetch("http://www.thecocktaildb.com/api/json/v1/1/random.php");
    let data = await result.json();
    console.log(data)
    let dr_name = data.drinks[0].strDrink
    document.getElementById('name').innerHTML = `<h3>${dr_name}</h3>`
    let dr_pic = data.drinks[0].strDrinkThumb
    document.getElementById('drink_pic').innerHTML = `<img class='img-thumbnail img-responsive' src='${dr_pic}' alt='drink picture'>`
    let tags_html = ''
    if (data.drinks[0].strCategory) {
        tags_html += `<div class="col-2"><button class="btn btn-outline-success me-2">${data.drinks[0].strCategory}</button></div>`
    }
    if (data.drinks[0].strAlcoholic) {
        tags_html += `<div class="col-2"><button class="btn btn-outline-danger me-2">${data.drinks[0].strAlcoholic}</button></div>`
    }
    if (data.drinks[0].strGlass) {
        tags_html += `<div class="col-2"><button class="btn btn-outline-secondary me-2">${data.drinks[0].strGlass}</button></div>`
    }
    document.getElementById('tags').innerHTML = tags_html
    let ingredient_list = ''
    ingredient_list += "<ul class='list-group list-group-flush'>"
    for (let i = 1; i < 16; i++) {
        if (data.drinks[0][`strIngredient${i}`] && data.drinks[0][`strMeasure${i}`]) {
            ingredient_list += `\n<li class='list-group-item'>${data.drinks[0][`strMeasure${i}`]} ${data.drinks[0][`strIngredient${i}`]}</li>\n`
        }
        else if (data.drinks[0][`strIngredient${i}`]) {
            ingredient_list += `\n<li class='list-group-item'>    ${data.drinks[0][`strIngredient${i}`]}</li>\n`
        }
        else {
            break
        }
    }
    ingredient_list += "</ul >"
    document.getElementById('ingredients').innerHTML = ingredient_list
    let instructions = data.drinks[0].strInstructions
    document.getElementById('instructions').innerText = instructions

    return


}
function reset() {
    document.getElementById('name').innerHTML = ''
    document.getElementById('drink_pic').innerHTML = ''
    document.getElementById('ingredients').innerHTML = ''
    document.getElementById('instructions').innerText = ''
    return
}


function test() {
    document.getElementById('name').innerText = 'tested'
    return
}

// test()
// { 
//     "drinks": 
//         [
//             { 
//                 "idDrink": "17826",
//                 "strDrink": "The Jimmy Conway", 
//                 "strDrinkAlternate": null, 
//                 "strTags": null, 
//                 "strVideo": null, 
//                 "strCategory": "Cocktail", 
//                 "strIBA": null, 
//                 "strAlcoholic": "Alcoholic", 
//                 "strGlass": "Whiskey sour glass", 
//                 "strInstructions": "Fill glass with ice\r\nPour in The Irishman and Disaronno\r\nFill to the top with Cranberry Juice\r\nGarnish with a slice of lemon\u2026Enjoy!",
//                 "strDrinkThumb": "https:\/\/www.thecocktaildb.com\/images\/media\/drink\/wbcvyo1535794478.jpg", 
//                 "strIngredient1": "Irish Whiskey", 
//                 "strIngredient2": "Amaretto", 
//                 "strIngredient3": "Cranberry Juice", 
//                 "strIngredient4": null, 
//                 "strIngredient5": null, 
//                 "strIngredient6": null, 
//                 "strIngredient7": null, 
//                 "strIngredient8": null, 
//                 "strIngredient9": null, 
//                 "strIngredient10": null, 
//                 "strIngredient11": null, 
//                 "strIngredient12": null, 
//                 "strIngredient13": null, 
//                 "strIngredient14": null, 
//                 "strIngredient15": null, 
//                 "strMeasure1": "50 ml", 
//                 "strMeasure2": "50 ml", 
//                 "strMeasure3": "4 oz", 
//                 "strMeasure4": null, 
//                 "strMeasure5": null, 
//                 "strMeasure6": null, 
//                 "strMeasure7": null, 
//                 "strMeasure8": null, 
//                 "strMeasure9": null, 
//                 "strMeasure10": null, 
//                 "strMeasure11": null, 
//                 "strMeasure12": null, 
//                 "strMeasure13": null, 
//                 "strMeasure14": null, 
//                 "strMeasure15": null, 
//                 "strImageSource": null, 
//                 "strImageAttribution": null, 
//                 "strCreativeCommonsConfirmed": "No", 
//                 "dateModified": "2018-09-01 10:34:38" 
//             }
//         ] 
//     }