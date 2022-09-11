const d = import("../json/details.json", {assert : {type: 'json'}});
console.log(d)
const toggleTheme = (theme = null) => {
    let element = document.body;
    if (!theme || theme == "dark"){
        element.classList.toggle("dark-mode");
    }
    console.log(theme)

    let links = document.getElementsByClassName("link");
    for (let i=0; i<links.length; i++){
        if(theme == "light" || links[i].classList.contains("link-dark-mode")) {
            links[i].classList.add("link-light-mode")
            links[i].classList.remove("link-dark-mode")
        }else{
            links[i].classList.add("link-dark-mode")
            links[i].classList.remove("link-light-mode")
        }
    }

    let image = document.getElementById("switch");
    if (theme == "light" || image.classList.contains("toggle-on")){
        image.src = "resources/toggleoff.png";
        image.classList.add("toggle-off")
        image.classList.remove("toggle-on")
        localStorage.setItem("theme", "light");
    } else{
        image.src = "resources/toggleon.png";
        image.classList.add("toggle-on")
        image.classList.remove("toggle-off")
        localStorage.setItem("theme", "dark");
    }
}

const changeImage = () => {
    let myimages = ["resources/profilepic.png"]
    let dp = document.getElementById("dp")
    const randomImage = myimages[Math.floor(Math.random() * myimages.length)];
    dp.valueOf().src = randomImage
}

const toggleThemeOnDefault = () => {
    let theme = localStorage.getItem("theme");
    if (theme){
        if (theme=="dark"){
            toggleTheme("dark")
        } else {
            toggleTheme("light")
        }
    } else {
        const isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        if (isDark) {
            toggleTheme();
        }
    }
}

const delay = async (delayInms) => {
    return new Promise(resolve => setTimeout(resolve, delayInms));
  }

const changeDetailOnDefault = () => {
    fetch("../json/details.json")
        .then(response => response.json())
        .then(async data => {
            let mydetails = data
            let details = document.getElementById("my-details");
            for (let j=0; j<mydetails.length; j++) {
                let detail = mydetails[j].detail
                for (let i = 0; i < detail.length; i++) {
                    await delay(200)
                        .then(() => {
                            if (i == 0) {
                                details.textContent = detail[0]
                            } else {
                                details.textContent += detail[i]
                            }
                        })
                }
                if(j==mydetails.length-1){
                    j=-1;
                }
                details.textContent = detail;
            }
            setTimeout(() => {
                changeDetailOnDefault();
            }, 2000);
        }
    )
}

const start = () => {
    toggleThemeOnDefault();
    try {
        changeDetailOnDefault();
    }catch (e){
        
    }
}

start()