//Random background-color for note
let notes = document.querySelectorAll(".note");
const colorList = [
    "brown",
    "cornflowerblue",
    "crimson",
    "darkorange",
    "deeppink"
];

for (let note of notes){
    let index = Math.floor(Math.random() * colorList.length);
    note.style.backgroundColor = colorList[index];
    
}
//Random background-color for note

//Read note
function showContent(element, type, index){
    let readContentList = document.querySelectorAll(element);
    let read = readContentList[index - 1];
    if (type === "show"){
        read.style.display = "flex";
    }
    else if (type === "hide"){
        read.style.display = "none";
    }
}
