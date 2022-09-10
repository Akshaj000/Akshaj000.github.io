const addContent = (content) => {
    console.log(content)
    const list_container = document.getElementById('lister')
    let parent = document.createElement("a")
    parent.classList.add("list-element")
    parent.style.padding = "30px";
    if(content["title"]){
        let head = document.createElement("h2")
        head.style.fontFamily = "Brush Script MT"
        head.append(content["title"])
        parent.append(head)
    }
    if(content["date"]){
        let date = document.createElement("p")
        date.style.textAlign = "right"
        date.append(content["date"])
        parent.append(date)
    }
    if(content["content"]){
        let paragraph = document.createElement("p")
        paragraph.style.textAlign = "left"
        paragraph.style.fontFamily = "Times New Roman', serif"
        paragraph.append(content["content"])
        parent.append(paragraph)
    }
    if(content["link"]){
        parent.href = content["link"]
    }
    list_container.prepend(parent)
}

const fetchContent = () => {
    fetch("../json/blogs.json")
        .then(response => response.json())
        .then(data => {
            for(let i=0; i< data.length; i++){
                addContent(data[i])
            }
        }
    )
}

fetchContent()