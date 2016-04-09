//object.onload = runpage.call


function runpage() {
	console.log("loaded");
	var form1 = document.getElementById("form1");
	var form2 = document.getElementById("form2");
	form2.style.display = 'none';
}

function week1() {
	console.log("week1");
	form1.style.display = 'block';
	form2.style.display = 'none';
}

function week2() {
	console.log("week2")
	form1.style.display = 'none';
	form2.style.display = 'block';
}