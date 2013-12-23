ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.742362, 37.555551],
            zoom: 11
        });

    ymaps.route([
        'Москва, улица Льва Толстого, 16',
        'Москва, Хорошевское шоссе, 89'
    ]).then(function (route) {
        myMap.geoObjects.add(route);
        var jamMeter = 0,
            way,
            segments;
        // Получаем массив путей.
        for (var i = 0; i < route.getPaths().getLength(); i++) {
            way = route.getPaths().get(i);
            segments = way.getSegments();
            for (var j = 0; j < segments.length; j++) {
                jamMeter += segments[j].getJamsTime();
            }
        }
        // Выводим маршрутный лист.
        $('#list').append(Math.round(jamMeter / 60));
    }, function (error) {
        alert('Возникла ошибка: ' + error.message);
    });
}
