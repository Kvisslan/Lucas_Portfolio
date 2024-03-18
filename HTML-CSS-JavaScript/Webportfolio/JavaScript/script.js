// function myFunc(){
//     document.getElementById('test').style.padding = '40px';
// }

// function changeBackground() {
//     document.body.style.backgroundColor = "Blue";
// }

// function changeBackgroundOnSection() {
//     document.getElementById("test3").style.backgroundImage = "url('DJ_dog.jpg')";
//     document.getElementById("test3").style.minHeight = "100vh";
//     document.getElementById("test3").style.minWidth = "100vw";
//     document.getElementById("test3").style.backgroundImage = "no-repeat";
// }

// ---------------------------Skills--------------------------- //
function changeBackgroundOnSectionPython() {
    document.getElementById("skills").style.backgroundImage = "url('/images/Python.png')";
}
function changeBackgroundOnSectionJavaScript() {
    document.getElementById("skills").style.backgroundImage = "url('/images/JavaScript.png')";
}
function changeBackgroundOnSectionHTML5() {
    document.getElementById("skills").style.backgroundImage = "url('/images/HTML5.png')";
}
function changeBackgroundOnSectionCSS() {
    document.getElementById("skills").style.backgroundImage = "url('/images/CSS.png')";
}
function changeBackgroundOnSectionGithub() {
    document.getElementById("skills").style.backgroundImage = "url('/images/Python.png')";
}
function changeBackgroundOnSectionSQL() {
    document.getElementById("skills").style.backgroundImage = "url('/images/SQL.png')";
}



// let i = 0;
// while (ObjectsToHide[i] != "pythontexthidden"){
//     document.getElementById(i).style.display = "none";
//     i ++;
// }
// const ObjectsToHide = ["defaulttexthidden", "pythontexthidden", "javascripttexthidden", "html5texthidden", "csstexthidden", "githubtexthidden", "sqltexthidden"];
// let i = 0;

// while (ObjectsToHide[i] != "javascripttexthidden"){
//     let text = "";
//     text += ObjectsToHide[i];
//     // alert(text);
//     i++;
// }


function showPythonTextInSkills() {
    const ObjectsToHide = ["javascripttexthidden", "html5texthidden", "csstexthidden", "githubtexthidden", "sqltexthidden"];
    
    document.getElementById("pythontexthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "pythontexthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showJavaScriptTextInSkills() {
    const ObjectsToHide = ["pythontexthidden", "html5texthidden", "csstexthidden", "githubtexthidden", "sqltexthidden"];
    
    document.getElementById("javascripttexthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "javascripttexthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showHTML5TextInSkills() {
    const ObjectsToHide = ["pythontexthidden", "javascripttexthidden", "csstexthidden", "githubtexthidden", "sqltexthidden"];

    document.getElementById("html5texthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "html5texthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showCSSTextInSkills() {
    const ObjectsToHide = ["pythontexthidden", "javascripttexthidden", "html5texthidden", "githubtexthidden", "sqltexthidden"];
    
    document.getElementById("csstexthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "csstexthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showGithubTextInSkills() {
    const ObjectsToHide = ["pythontexthidden", "javascripttexthidden", "html5texthidden", "csstexthidden", "sqltexthidden"];

    document.getElementById("githubtexthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "githubtexthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showSQLTextInSkills() {
    const ObjectsToHide = ["pythontexthidden", "javascripttexthidden", "html5texthidden", "csstexthidden", "githubtexthidden"];

    document.getElementById("sqltexthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "sqltexthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
// ---------------------------/Skills--------------------------- //

// ---------------------------References--------------------------- //
function showPerson1TextInReferences() {
    const ObjectsToHide = ["person2texthidden", "person3texthidden"];
    
    document.getElementById("person1texthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "person1texthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showPerson2TextInReferences() {
    const ObjectsToHide = ["person1texthidden", "person3texthidden"];
    
    document.getElementById("person2texthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "person2texthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}
function showPerson3TextInReferences() {
    const ObjectsToHide = ["person1texthidden", "person2texthidden"];
    
    document.getElementById("person3texthidden").style.display = "block";
    let i = 0;
    while (ObjectsToHide[i] != "person3texthidden"){
        let text = "";
        text += ObjectsToHide[i];
        document.getElementById(text).style.display = "none";
        i++;
    }
}