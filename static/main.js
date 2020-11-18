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

const HideMenu = ()=>{
    let main = document.querySelector("#main")
    let navMenu = document.querySelector(".nav__menu")
    main.addEventListener("click", ()=>{
       
        navMenu.classList.remove('show')

    })
}

showMenu()
HideMenu()


const  fadeOut = ()=>{
    document.getElementById("alert").classList.add("fadeout")
}


setTimeout(fadeOut, 7000)