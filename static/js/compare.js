function selectCandidate() {
    if ( name == "default" ) {
        return;
    }

    if ( names.length >= 4 ) {
        alert("비교는 4명까지 가능합니다.");
        return;
    }

    names.push(name);

    // 트렌드 전환
    initTrendChart(name);
}