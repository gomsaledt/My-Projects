let display = document.getElementById('display');
let buttons = Array.from(document.getElementsByClassName("buttons"));

buttons.map(button =>{
    button.addEventListener('click', (e) => {
        switch (e.target.innerText) {
			case "C":
				display.innerText = "";
				break;
			case "=":
				try {
					display.innerText = eval(display.innerText);
				} catch {
					display.innerText = "Error";
				}
				break;
			case "←":
                if (display.innerText === "Error"){
                    display.innerText = "";
                }

                if (display.innerText){
                    display.innerText = display.innerText.slice(0, -1);
                }
                break
			default:
                if(display.innerText === "Error"){
                    display.innerText = e.target.innerText;
                } else{
                    display.innerText += e.target.innerText;
                }
				break;
		}
    });
});