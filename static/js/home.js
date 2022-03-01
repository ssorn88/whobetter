var $ments = document.getElementsByClassName("ment-1");
var ments = ["어렵고 복잡한,", "수없이 버려지는,", "비교하기 어려운,"]

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

document.addEventListener("DOMContentLoaded", async function(){
    for(let i=0 ; i<3 ; i++ ) {
        var typewriter = new Typewriter($ments[i], {
            loop: false
        });

        typewriter.typeString(ments[i])
        .start();

        await sleep(2000);

    }

    for(let i=0 ; i<3 ; i++ ) {
        $ments[i].innerHTML = ments[i];
    }
});