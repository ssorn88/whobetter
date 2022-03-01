function selectCandidate(value) {

    var name = value.split('|')[0];
    var pk = value.split('|')[1];

    if ( name == "default" ) {
        return;
    }

    if ( name in names ) {
        return;
    }

    if ( names.length >= 4 ) {
        alert("비교는 4명까지 가능합니다.");
        return;
    }

    names.push(name);

    console.log(name, pk);

    // 트렌드 전환
    initTrendChart();

    document.getElementById(pk).style.display = "block";
}

function dismiss(value) {

    var name = value.split('|')[0];
    var pk = value.split('|')[1];

    document.getElementById(pk).style.display = "none";

    for(let i = 0; i < names.length; i++) {
      if(names[i] === name)  {
        names.splice(i, 1);
        i--;
      }
    }

    // 트렌드 전환
    initTrendChart();
}
