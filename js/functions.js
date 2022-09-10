const d = import("../json/details.json", {assert : {type: 'json'}});
console.log(d)
const toggleTheme = () => {

    let element = document.body;
    element.classList.toggle("dark-mode");

    let links = document.getElementsByClassName("link");
    for (let i=0; i<links.length; i++){
        if(links[i].classList.contains("link-light-mode")) {
            links[i].classList.toggle("link-dark-mode")
            links[i].classList.remove("link-light-mode")
        }else {
            links[i].classList.toggle("link-light-mode")
            links[i].classList.remove("link-dark-mode")
        }
    }

    let image = document.getElementById("switch");
    if (image.classList.contains("toggle-off")){
        image.src = "resources/toggleon.png";
        image.classList.add("toggle-on")
        image.classList.remove("toggle-off")
    } else {
        image.src = "resources/toggleoff.png";
        image.classList.add("toggle-off")
        image.classList.remove("toggle-on")
    }
}

const changeImage = () => {
    let myimages = ["resources/profilepic.png"]
    let dp = document.getElementById("dp")
    const randomImage = myimages[Math.floor(Math.random() * myimages.length)];
    dp.valueOf().src = randomImage
}

const toggleThemeOnDefault = () => {
    const isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (isDark){
        toggleTheme();
    }
}

const changeDetailOnDefault = () => {
    fetch("../json/details.json")
        .then(response => response.json())
        .then(data => {
            let mydetails = data
            let details = document.getElementById("my-details");
            const randomElement = mydetails[Math.floor(Math.random() * mydetails.length)];
            details.textContent=randomElement.detail;
            setTimeout(() => { changeDetailOnDefault(); }, 2000);
        }
    )
}

const start = () => {
    toggleThemeOnDefault();

    try {
        changeDetailOnDefault();
    }catch (e){}
}

start()