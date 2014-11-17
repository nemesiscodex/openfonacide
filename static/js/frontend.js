(function(){
    var app = angular.module('frontEnd', ['ngResource']);

    app.config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

    function nuevaDirectiva(nombre, template){
        app.directive(nombre, function(){
        return {
            restrict: 'E',
            templateUrl: 'partials/'+template
        }
    });
    }

    /**
     * Directivas
     */
    nuevaDirectiva('footerInfo','footer.html');
    nuevaDirectiva('api','api.html');
    nuevaDirectiva('institucionList','institucion-list.html');
    nuevaDirectiva('home','home.html');
    nuevaDirectiva('siteNav','nav.html');
    nuevaDirectiva('institucionModal','institucion-modal.html');
    nuevaDirectiva('establecimientoTabla','institucion-modal/establecimiento-tabla.html');
    nuevaDirectiva('institucionesTabla','institucion-modal/instituciones-tabla.html');
    nuevaDirectiva('comentarios','institucion-modal/comentarios.html');
    nuevaDirectiva('denuncias','institucion-modal/denuncias.html');
    nuevaDirectiva('fonacide','institucion-modal/fonacide.html');


    /**
     * Servicio backend utilizando la api de django rest
     */
    app.service('backEnd', ['$resource',function($resource){
            var backEndUrl = 'http://mecmapi-nemesiscodex.rhcloud.com/';
            return{
                "establecimiento":
                    $resource(backEndUrl + 'establecimiento/:id', {id:"@id"}, {
                        query: {method: 'GET', isArray:true, cache:true},
                        get: {method: 'GET', isArray:false, cache:true}
                    }),
                "establecimiento_short":
                    $resource(backEndUrl + 'establecimiento/:id', {id:"@id",short:'true'}, {
                        query: {method: 'GET', isArray:true, cache:true}
                    }),
                "institucion":
                    $resource(backEndUrl + 'institucion/:id', {id:"@id"}, {
                        query: {method: 'GET', isArray:true, cache:true}
                    })
            }
        }]);

    /**
     * Controlador de la pagina
     */
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


    /**
     * Controlador del mapa
     */
    app.controller('MapController', ['$scope', 'backEnd', function($scope,backEnd){
        $scope.showInfo = false;
        $scope.modalTitle = "";
        $scope.setModalTitle = function(title){
            $scope.modalTitle = title;
        };
        $scope.loading = true;
        $scope.infoData = {};

        $scope.showInfoPopUp = function(id, title){
            $scope.setModalTitle(title);
            $scope.infoData = {};
            backEnd.establecimiento.get({id: id}, function(value, headers){
                $scope.infoData.establecimiento = value;
                $scope.showInfo = true;
            });
            backEnd.institucion.query({id:id}, function(value, headers){
                $scope.infoData.instituciones = value;
                console.log($scope.infoData);
            });
        };

        $scope.map = L.map('map').setView([-25.308, -57.6], 13);
            L.tileLayer('http://{s}.tiles.mapbox.com/v3/nemesiscodex.k7abci9m/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                maxZoom: 18
            }).addTo($scope.map);

        backEnd.establecimiento_short.query({}, function(value, headers){
            var point;
            var marker;
            var markers = new L.MarkerClusterGroup({

                iconCreateFunction: function (cluster) {
                    return L.divIcon({ html: cluster.getChildCount(), className: 'mycluster', iconSize: L.point(40, 40) });
                }
            });

            if(value){
                for(var i=0; i<value.length; i++){
                    point = value[i];
                    marker = new L.Marker([point.lat, point.lon], {title:point.name});
                    marker.bindPopup("<p><b>"+point.name+'<a href="javascript:void(0)" onClick="openPopUp('+point.id+',\''+point.name.replace('\n','')+'\')" class="link mdi-action-launch"></a></b><hr>'+point.dir+"</p>");
                    markers.addLayer(marker);
                }
            }
            $scope.map.addLayer(markers);

            $scope.loading = false;
        });

    }]);
})();