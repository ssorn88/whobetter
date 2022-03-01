function initTrendChart() {

    if ( names.length == 0 ) {
        document.getElementById("trend").style.display = 'none';
        return;
    }

    var comparisonItem = [];
    var exploreQuery = "date=today%201-m&geo=KR&q=";

    for (let i=0 ; i<names.length ; i++ ) {
        // 1명 data 생성 후 리스트에 추가
        var data = new Object();
        data.keyword = names[i];
        data.geo = "KR";
        data.time = "today 1-m";
        comparisonItem.push(data);

        encoded = encodeURI(names[i]);
        exploreQuery += encoded;
        if(i!=names.length-1) {
            exploreQuery += ",";
        }

    }

    document.getElementById("trend").innerHTML = "";
    trends.embed.renderExploreWidgetTo(document.getElementById("trend"), "TIMESERIES", {"comparisonItem":comparisonItem, "category":0,"property":""},{"exploreQuery":exploreQuery,"guestPath":"https://trends.google.co.kr:443/trends/embed/"});
}
