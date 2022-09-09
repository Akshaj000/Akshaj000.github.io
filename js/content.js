const addContent = (content) => {
    console.log(content)
    const list_container = document.getElementById('lister')
    let parent = document.createElement("a")
    parent.classList.add("list-element")
    if(content["title"]){
        let head = document.createElement("h2")
        head.append(content["title"])
        parent.append(head)
    }
    if(content["description"]){
        let paragraph = document.createElement("p")
        paragraph.append(content["description"])
        parent.append(paragraph)
    }
    parent.href = content["link"]
    if (content["type"] == "youtube") {
        let splited = content["link"].split("/")
        if (!content["link"].includes("embed")) {
            content["link"] = `https://www.youtube.com/embed/${splited[splited.length-1]}`
        } else {
            parent.href = `https://www.youtube.com/watch?v=${splited[splited.length-1]}`
        }
        let child = document.createElement("iframe");
        child.style.height = "30vh";
        child.style.width = "98%";
        child.src = content["link"]
        parent.append(child)

    } else if (content["type"] == "twitter"){
        let child = document.createElement("blockquote")
        child.classList.add("twitter-tweet")
        let link = document.createElement("a")
        link.href = content["link"]
        child.append(link)
        parent.append(child)
        let script = document.createElement("script")
        script.src = "https://platform.twitter.com/widgets.js";
        script.charset = "utf-8"
        script.async = true
        parent.append(script)

    } else if (content["type"] == "instagram"){
        let child = document.createElement("iframe")
        child.src = content["link"]
        child.style.height = "80vh"
        child.style.width = "98%"
        parent.append(child)
        let splited = content["link"].split("/")
        parent.href = `https://www.instagram.com/p/${splited[splited.length-2]}`

    } else if (content["type"] == "other"){
        let child = document.createElement("iframe")
        child.src = content["link"]
        child.style.height = "40vh"
        child.style.width = "98%"
        child.style.overflow = "scroll"
        parent.append(child)
    } else {
        let child = document.createElement("div")
        child.style.height = "25vh"
        child.style.width = "98%"
        parent.href = "#"
        parent.append(child)
    }
    list_container.prepend(parent)
}

const fetchContent = () => {
    const contents = [{},{},{},{}]

    for (let i = 0; i < contents.length; i++) {
        addContent(contents[i])
    }
}

onload(fetchContent())