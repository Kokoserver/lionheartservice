const showMenu = ()=>{
    let navMenu = document.querySelector(".nav__menu")
    let toggler = document.querySelector('#toggler')

    if(navMenu && toggler){
    toggler.addEventListener("click", ()=>{
        navMenu.classList.toggle('show')
    })
     
    }
    return
}

showMenu()

const  fadeOut = ()=>{
    document.getElementById("alert").classList.add("fadeout")
}


setTimeout(fadeOut, 5000)