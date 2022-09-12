const addContent = (content) => {
    const list_container = document.getElementById('lister')
    let parent = document.createElement("div")
    parent.classList.add("blog-element")
    parent.style.padding = "30px";
    if(content["link"]){
        parent.href = content["link"]
    }
    let element = document.getElementById("zero-md")
    let child = document.createElement("zero-md")
    child.innerHTML = element.innerHTML
    child.style.display = "block";
    child.src = `../blogs/${content["file"]}`
    parent.append(child)
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