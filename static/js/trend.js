window.onload = function() {
    // 비교 인원 ( 임시 )
    var cnt = 3;
    // 이름 리스트 ( 임시 )
    const names = ["이재명", "심상정", "윤석열"];

    var comparisonItem = [];
    var exploreQuery = "geo=KR&q=";

    for (let i=0 ; i<3 ; i++ ) {
        // 1명 data 생성 후 리스트에 추가
        var data = new Object();
        data.keyword = names[i];
        data.geo = "KR";
        data.time = "today 1-m";
        comparisonItem.push(data)

        encoded = encodeURI(names[i]);
        exploreQuery += encoded += ",";
    }

    exploreQuery += "&date=today 1-m,today 1-m";
    var jsonData = JSON.stringify(comparisonItem);

    trends.embed.renderExploreWidget("TIMESERIES",
    {"comparisonItem":comparisonItem, "category":0,"property":""},
    {"exploreQuery":exploreQuery,"guestPath":"https://trends.google.co.kr:443/trends/embed/"});
}