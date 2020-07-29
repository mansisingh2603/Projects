//code to animate a car that starts from a red light and slowly picks up speed.

let redLight = document.querySelector("#redLight");
let car      = document.querySelector("#car");

setTimeout(()=>{
    startAnimation();
}, 2000)

let startAnimation = () => {
    redLight.style.display = "none";
    let startKeyframes = {"left": "2vw"};
    let endKeyframes = {"left": "100vw"};
    let options = {
        duration: 3000
        easing:cubic-bezier(0.76, 0, 0.24, 1);; //starts slow and gains speed
    };

    car.animate([startKeyframes, endKeyframes], options);
};
