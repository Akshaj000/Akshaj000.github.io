const addContent = (content) => {
    const list_container = document.getElementById('lister')

    let div = document.createElement("div")
    let parent = document.createElement("img")
    div.classList.add("gallery-element")
    parent.style.width = "100%";
    parent.style.height = "auto";
    parent.src = content["source"]
    div.append(parent);
    list_container.prepend(div)
}

const fetchContent = () => {
    fetch("../json/gallery.json")
        .then(response => response.json())
        .then(data => {
            for(let i=0; i< data.length; i++){
                addContent(data[i])
            }
        }
    )
}

fetchContent()