(function(){
    var app = angular.module('frontEnd', ['ngResource','ngCookies', 'vcRecaptcha']);

    app.run(function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    });

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
    nuevaDirectiva('visualizaciones','visualizaciones.html');
    nuevaDirectiva('home','home.html');
    nuevaDirectiva('siteNav','nav.html');
    nuevaDirectiva('institucionModal','institucion-modal.html');
    nuevaDirectiva('establecimientoTabla','institucion-modal/establecimiento-tabla.html');
    nuevaDirectiva('institucionesTabla','institucion-modal/instituciones-tabla.html');
    nuevaDirectiva('comentarios','institucion-modal/comentarios.html');
    //nuevaDirectiva('denuncias','institucion-modal/denuncias.html');
    nuevaDirectiva('fonacide','institucion-modal/fonacide.html');


    /**
     * Servicio backend utilizando la api de django rest
     */
    app.service('backEnd', ['$resource',function($resource){
            var backEndUrl = '';
            return{
                "establecimiento":
                    $resource(backEndUrl + 'establecimiento/:id', {id:"@id"}, {
                        query: {method: 'GET', isArray:true, cache:true},
                        get: {method: 'GET', isArray:false, cache:true}
                    }),
                "prioridades":
                    $resource(backEndUrl + 'prioridades/:id', {id:"@id"}, {
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
                    }),
                "comentarios":
                    $resource(backEndUrl + 'comentarios/:id', {id:"@id"}, {
                        get: {method: 'GET', isArray: true, cache: false},
                        save: {method: 'POST', headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                            transformRequest: function (obj) {
                                var str = [];
                                for (var p in obj)
                                    str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                                return str.join("&");
                            }}
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

    app.controller('comentsController', ['$scope', 'backEnd', 'vcRecaptchaService', function($scope, backEnd, vcRecaptchaService){

        $scope.recaptchaKey = '6Lc8B_8SAAAAADo-UUdXveJmdX584QbAJn4Nxsuu';


        $controller = this;
        $controller.establecimiento = "";
        $scope.setEstablecimiento = function(establecimiento){
            $controller.establecimiento = establecimiento;
             backEnd.comentarios.get({id:$controller.establecimiento}, function(value, headers){
                $scope.comentarios = value;
            });

        };

        $scope.inicializar = function(){
            $scope.comentarios = [];


            $scope.comentario = {
                texto: '',
                autor: '',
                fecha: '',
                email: ''
            };
            
            $controller.tab = 'map';
        };



        $scope.comentarios = [];

        $scope.error = false;

        $scope.inicializar();
        $scope.guardarComentario = function(comentario){
            comentario.fecha = Date.now();
            comentario.captcha = JSON.stringify(vcRecaptchaService.data());
            backEnd.comentarios.save({id: $controller.establecimiento}, comentario, function(){
                $('#info_modal').modal('show').modal('setting', 'closable', true);
                comentario.texto = "";
                $scope.error = false;
                $scope.setEstablecimiento($controller.establecimiento);
            }, function(){
                $scope.error = true;
                $('#nuevo-comentario').modal('show').modal('setting', 'closable', false);
            });
        };


    }]);


    /**
     * Controlador del mapa
     */
    app.controller('MapController', ['$scope', 'backEnd', '$filter', function($scope,backEnd,$filter){
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
                backEnd.institucion.query({id:id}, function(value, headers){
                    $scope.infoData.instituciones = value;
                    $('#info_modal').modal('show');
                    setTimeout(function(){
                        $('#info_modal').modal('refresh');
                    },1300);

                });
            });
            backEnd.prioridades.get({id: id}, function(value, headers){
                $scope.prioridades = value;
            });

        };

        var sidebar = L.control.sidebar('sidebar');

        $scope.map = L.map('map').setView([-25.308, -57.6], 13);
//            L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
            L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://openstreetmap.org">OpenStreetMap</a>',
                maxZoom: 18
            }).addTo($scope.map);

        backEnd.establecimiento_short.query({}, function(data, headers){

            $scope.mapData = data;
            sidebar.addTo($scope.map);
            $( "#slider-range-min" ).slider({
      range: "min",
      value: 37,
      min: 1,
      max: 700,
      slide: function( event, ui ) {
        $( "#amount" ).val( "" + ui.value );
      }
    });
            $( "#amount" ).val( "" + $( "#slider-range-min" ).slider( "value" ) );


            $scope.update('');
        });

        $scope.update = function(filterType){

            $scope.loading = true;

            switch (filterType){
                case 'fonacide':
                    updateMap(function(map){
                        var ret = $filter('filter')(map, function(elemento,index){

                            return (elemento.f == 't')
                        }, true);
                        return ret;
                    });
                    break;
                case 'denunciaPrensa':
                    updateMap(function(map){
                        return map;
                    });
                    break;
                case 'denunciaCiudadania':
                    updateMap(function(map){
                        return map;
                    });
                    break;
                case 'informeContraloria':
                    updateMap(function(map){
                        return map;
                    });
                    break;
                default:
                    updateMap(function(map){return map});
            }
        };

        var updateMap = function(filterFunction){

            var point;
            var marker;
            var data = filterFunction($scope.mapData);

            if($scope.markers)
                $scope.map.removeLayer($scope.markers);

            $scope.markers = new L.MarkerClusterGroup({

                iconCreateFunction: function (cluster) {
                    return L.divIcon({ html: cluster.getChildCount(), className: 'mycluster', iconSize: L.point(40, 40) });
                }
            });
            var markers = $scope.markers;
            if(data){
                for(var i=0; i<data.length; i++){
                    point = data[i];
                    marker = new L.Marker([point.lat, point.lon], {title:point.name});
                    marker.bindPopup("<h4>"+point.name+'</h4><div class="ui labeled blue tiny icon button" onClick="openPopUp('+point.id+',\''+point.name.replace('\n','')+'\')" ><i class="plus outline icon"></i>Detalles</div><hr>'+point.dir);
                    markers.addLayer(marker);
                }
            }

            $scope.map.addLayer(markers);


            $scope.loading = false;
        }
    }]);
})();
