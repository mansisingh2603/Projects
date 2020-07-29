//Setup website here
let hero = document.querySelector("#hero");
let villain = document.querySelector("#villain");
let lightning = document.querySelector("#lightning");

//Setup animation code here
let lightningStart = {"left": "190px"};	//let is block scoped
let lightningEnd = {"left": "860px"};
let options = {"duration": 1000};  /*1000ms is the duration*/
//making the monster rotate out of screen
let hitMonster=() =>{
	let monsterStart ={
		transform: 'rotate(0deg)',
		opacity:100

	};

	let monsterEnd = {
		transform: 'rotate(10000deg)',
		opacity: 0

	};
	let options = {"duration" : 1500};
	villain.animate([monsterStart,monsterEnd], options);


}




lightning.animate([lightningStart, lightningEnd], options).onfinish= hitMonster;