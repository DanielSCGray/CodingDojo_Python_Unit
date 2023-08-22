async function getData() {
    let result = await fetch("https://api.github.com/users/adion81");
    let data = await result.json();
    // console.log(data['login'])
    let name = data['name']
    let avatar = data['avatar_url']
    let followers = data['followers']
    // console.log(name)
    let user_info = name + ' has ' + followers + ' followers'
    document.getElementById('user_info').innerText = user_info
    document.getElementById('avatar').innerHTML = `<img src='${avatar}' alt='user avatar'>`
    return makeAtuple(nameSTR)
}
// let test = getData()
// let data = getData()
console.log(data)
// console.log(data['login'])

function makeAtuple(a) {
    return (a)
}