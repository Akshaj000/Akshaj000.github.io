const addContent = (content) => {
    const list_container = document.getElementById('lister')

    let parent = document.createElement("img")
    parent.classList.add("gallery-element")
    parent.style.width = "100%";
    parent.style.height = "auto";
    parent.src = content["source"]
    list_container.prepend(parent)
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