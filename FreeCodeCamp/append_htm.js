//calling the function in window.onload to make sure the HTML is loaded
window.onload = function() {
    //creating a new paragraph
    var p = document.createElement("p");
    var node = document.createTextNode("Some new text");
    //adding the text to the paragraph
	console.log(p)
	console.log(node)
    p.appendChild(node);

    var div = document.getElementById("demo");
    //adding the paragraph to the div
    div.appendChild( node);
};