const addContent = (content) => {
    console.log(content)
    const list_container = document.getElementById('lister')
    let parent = document.createElement("a")
    parent.classList.add("list-element")
    parent.style.padding = "30px";
    parent.style.color = localStorage.getItem("theme") == "light" ? "black" : "white"
    if(content["title"]){
        let head = document.createElement("h2")
        head.style.fontFamily = "Brush Script MT"
        head.append(content["title"])
        parent.append(head)
    }
    if(content["description"]){
        let paragraph = document.createElement("p")
        paragraph.style.textAlign = "left"
        paragraph.style.fontFamily = "Times New Roman', serif"
        paragraph.append(content["description"])
        parent.append(paragraph)
    }
    if(content["repository"]){
        parent.href = content["repository"]
    }
    if(content["image"]){
        let child = document.createElement("img")
        child.src = content["image"]
        child.style.width = "100%"
        parent.append(child)
    }
    parent.classList.add("project-item")
    list_container.prepend(parent)
}

const fetchContent = () => {
    fetch("../json/projects.json")
        .then(response => response.json())
        .then(data => {
            for(let i=0; i< data.length; i++){
                addContent(data[i])
            }
        }
    )
}

fetchContent()