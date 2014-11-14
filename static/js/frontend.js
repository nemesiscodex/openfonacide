(function(){
    var app = angular.module('frontEnd', ['ngResource']);
    app.service('backEnd', ['$resource',function($resource){
            var backEndUrl = 'http://localhost:8000/';
            return{
                'instituciones':
                    $resource(backEndUrl + 'institucion', {}, {
                        query: {method: 'GET', isArray:true, cache:true}
                    }),
                'instituciones_short':
                    $resource(backEndUrl + 'institucion', {short:'true'}, {
                        query: {method: 'GET', isArray:true, cache:true}
                    })
            }
        }]);
    app.controller('PageController', [ '$scope', function($scope){

        $controller = this;
        $controller.tab = 'home';

        $scope.setTab = function(tabName){
            $controller.tab = tabName;
        };
        $scope.getTab = function(){
            return $controller.tab
        };
        $scope.isTab = function(tabName){
            return $controller.tab === tabName;
        }
    }]);

    app.controller('MapController', ['$scope', 'backEnd', function($scope,backEnd){

        $scope.loading = true;
        $scope.map = L.map('map').setView([-25.308, -57.6], 13);
            L.tileLayer('http://{s}.tiles.mapbox.com/v3/nemesiscodex.k7abci9m/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                maxZoom: 18
            }).addTo($scope.map);

        backEnd.instituciones_short.query({}, function(value, headers){
            var point;
            var markers = new L.MarkerClusterGroup({

                iconCreateFunction: function (cluster) {
                    return L.divIcon({ html: cluster.getChildCount(), className: 'mycluster', iconSize: L.point(40, 40) });
                }
            });

            if(value){
                for(var i=0; i<value.length; i++){
                    point = value[i];
                    markers.addLayer(new L.Marker([point.lat, point.lon], {title:point.id}));
                }
            }
            $scope.map.addLayer(markers);

            $scope.loading = false;
        });

    }]);
})();