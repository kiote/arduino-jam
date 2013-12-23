ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [55.742362, 37.555551],
            zoom: 11
        });

    ymaps.route([
        'Москва, улица Льва Толстого, 16',
        'Москва, Хорошевское шоссе, 82к8'
    ]).then(function (route) {
        myMap.geoObjects.add(route);
        var moveList = 'Трогаемся,</br>',
            way,
            segments;
        // Получаем массив путей.
        for (var i = 0; i < route.getPaths().getLength(); i++) {
            way = route.getPaths().get(i);
            segments = way.getSegments();
            for (var j = 0; j < segments.length; j++) {
                var street = segments[j].getStreet();
                moveList += ('Едем ' + segments[j].getHumanAction() + (street ? ' на ' + street : '') + ', проезжаем ' + segments[j].getLength() + ' м.,');
                moveList += '</br>'
            }
        }
        moveList += 'Останавливаемся.';
        // Выводим маршрутный лист.
        $('#list').append(moveList);
    }, function (error) {
        alert('Возникла ошибка: ' + error.message);
    });
}
