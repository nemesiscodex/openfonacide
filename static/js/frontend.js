(function(){
    var app = angular.module('frontEnd', ['ngResource','ngCookies', 'ngRoute', 'ngAnimate']);

    app.run(function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    });

    app.config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

    app.config(['$routeProvider', '$locationProvider',
      function($routeProvider, $locationProvider) {
        $routeProvider
          .when('/', {
            templateUrl: 'partials/home.html',
          })
          .when('/map/', {
            controller: 'MapController',
            templateUrl: '../partials/map.html'
          })

          .when('/map/:establecimiento', {
            controller: 'MapController',
            templateUrl: '../partials/map.html'
          })
          .when('/map/:establecimiento/:institucion', {
            controller: 'MapController',
            templateUrl: '../../partials/map.html'
          })
          .when('/resumen/', {
            controller: 'ResumenController',
            templateUrl: '../partials/resumen.html'
          })
          .when('/graficos/', {
            controller: 'GraficosController',
            templateUrl: '../partials/graficos.html'
          })
          .when('/fonacide/', {
            controller: 'FonacideController',
            templateUrl: '../partials/fonacide.html'
          });

        $locationProvider.html5Mode(true);
    }]);

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
    nuevaDirectiva('loginModal','login.html');
    nuevaDirectiva('institucionList','institucion-list.html');
    nuevaDirectiva('visualizaciones','visualizaciones.html');
    nuevaDirectiva('home','home.html');
    nuevaDirectiva('search','search.html');
    nuevaDirectiva('siteNav','nav.html');
    nuevaDirectiva('institucionModal','institucion-modal.html');
    nuevaDirectiva('establecimientoTabla','institucion-modal/establecimiento-tabla.html');
    nuevaDirectiva('institucionesTabla','institucion-modal/instituciones-tabla.html');
    nuevaDirectiva('comentarios','institucion-modal/comentarios.html');
    nuevaDirectiva('aulas','institucion-modal/instituciones-tabs/aulas.html');
    nuevaDirectiva('mobiliarios','institucion-modal/instituciones-tabs/mobiliarios.html');
    nuevaDirectiva('denuncias','institucion-modal/instituciones-tabs/denuncias.html');
    nuevaDirectiva('sanitarios','institucion-modal/instituciones-tabs/sanitarios.html');
    nuevaDirectiva('informacion','institucion-modal/instituciones-tabs/informacion.html');
    nuevaDirectiva('fonacide','institucion-modal/fonacide.html');
    nuevaDirectiva('resumen','institucion-modal/fonacide.html');


    /**
     * Servicio backend utilizando la api de django rest
     */
    app.service('backEnd', ['$resource',function($resource){
            var backEndUrl = '';
            return{
                "establecimiento":
                    $resource(backEndUrl + '../establecimiento/:id', {id:"@id"}, {
                        query: {method: 'GET', isArray:true, cache:true},
                        get: {method: 'GET', isArray:false, cache:true}
                    }),
                "prioridades":
                    $resource(backEndUrl + '../prioridades/:id', {id:"@id"}, {
                        query: {method: 'GET', isArray:true, cache:true},
                        get: {method: 'GET', isArray:false, cache:true}
                    }),
                "establecimiento_short":
                    $resource(backEndUrl + '../establecimiento/:id', {id:"@id",short:'true'}, {
                        query: {method: 'GET', isArray:true, cache:true}
                    }),
                "institucion":
                    $resource(backEndUrl + '../institucion/:id', {id:"@id"}, {
                        query: {method: 'GET', isArray:true, cache:true}
                    }),
                "comentarios":
                    $resource(backEndUrl + '../comentarios/:id', {id:"@id"}, {
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
        $controller.subTab = 'info';

        $scope.setSubTab = function(tabName){
            $controller.subTab = tabName;
        };
        $scope.getSubTab = function(){
            return $controller.subTab
        };
        $scope.isSubTab = function(tabName){
            return $controller.subTab === tabName;
        };

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

    app.controller('FonacideController', ['$scope', function($scope){

    }]);
    app.controller('GraficosController', ['$scope', function($scope){

    }]);
    app.controller('ResumenController', ['$scope', function($scope){

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

        // var sidebar = L.control.sidebar('sidebar');

        $scope.map = L.map('map').setView([-25.308, -57.6], 13);

//            L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://openstreetmap.org">OpenStreetMap</a>',
//                maxZoom: 18
//            }).addTo($scope.map);
        var mapLink =
            '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © '+ mapLink,
            maxZoom: 18,
            }).addTo($scope.map);

        $scope.onEachFeature = function(feature, layer) {
    // Load the default style.
    layer.setStyle(defaultStyle);
    // Create a self-invoking function that passes in the layer
    // and the properties associated with this particular record.
    (function(layer, properties) {
      // Create a mouseover event
      layer.on("mouseover", function (e) {
        // Change the style to the highlighted version
        layer.setStyle(highlightStyle);
        // Create a popup with a unique ID linked to this record
        var popup = $("<div></div>", {
            id: "popup-" + properties.DISTRICT,
            css: {
                position: "absolute",
                bottom: "85px",
                left: "50px",
                zIndex: 1002,
                backgroundColor: "white",
                padding: "8px",
                border: "1px solid #ccc"
            }
        });
        // Insert a headline into that popup
        var hed = $("<div></div>", {
            text: "District " + properties.DISTRICT + ": " + properties.REPRESENTATIVE,
            css: {fontSize: "16px", marginBottom: "3px"}
        }).appendTo(popup);
        // Add the popup to the map
        popup.appendTo("#map");
      });
      // Create a mouseout event that undoes the mouseover changes
      layer.on("mouseout", function (e) {
        // Start by reverting the style back
        layer.setStyle(defaultStyle);
        // And then destroying the popup
        $("#popup-" + properties.DISTRICT).remove();
      });
      // Close the "anonymous" wrapper function, and call it while passing
      // in the variables necessary to make the events work the way we want.
    })(layer, feature.properties);
};






        backEnd.establecimiento_short.query({}, function(data, headers){
            $scope.mapData = JSONH.unpack(data);
//            $( "#slider-range-min" ).slider({
//      range: "min",
//      value: 37,
//      min: 1,
//      max: 700,
//      slide: function( event, ui ) {
//        $( "#amount" ).val( "" + ui.value );
//      }
//    });
//            $( "#amount" ).val( "" + $( "#slider-range-min" ).slider( "value" ) );


            $scope.update('');
        });

        $scope.update = function(filterType){

            $scope.loading = true;

            switch (filterType){
                case 'fonacide':
                   if ( $scope.ContratacionesLayer) {
                    $scope.map.removeLayer($scope.ContratacionesLayer);}
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
                case 'contrataciones':
                     /* Geojson para contratataciones */

                    $scope.map.removeLayer($scope.markers);

                   if (! $scope.ContratacionesLayer) {

                    $scope.ContratacionesLayer = L.geoJson().addTo($scope.map);


                   $.getJSON( "/static/geojson/00.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/01.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/02.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/03.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/04.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/05.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/06.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/07.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/08.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/09.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/10.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/11.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/12.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/13.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/14.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/15.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/16.json", function( data ) {$scope.ContratacionesLayer.addData(data);});
                   $.getJSON( "/static/geojson/17.json", function( data ) {$scope.ContratacionesLayer.addData(data);});

                    $scope.ContratacionesLayer .on('mouseover', function(e) {
                            e.layer.openPopup();
                        });
                        $scope.ContratacionesLayer.on('mouseout', function(e) {
                            e.layer.closePopup();
                        });


                   }



                   $scope.loading=false;






                        /* FIN GEOJSON*/


                    break;
                default:
                     if ( $scope.ContratacionesLayer) {
                    $scope.map.removeLayer($scope.ContratacionesLayer);}

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
            var redMarker = L.AwesomeMarkers.icon({
                prefix: '',
                icon: ' university icon margin-left',
                markerColor: 'blue',
                extraClasses: 'info icon'
              });
            if(data){
                for(var i=0; i<data.length; i++){
                    point = data[i];
                    marker = new L.Marker([point.lat, point.lon], {title:point.name, icon: redMarker});
                    marker.bindPopup("<h4>"+point.name+'</h4><div class="ui labeled blue tiny icon button" onClick="$(\'.right.sidebar\').sidebar(\'toggle\');openPopUp('+point.id+',\''+point.name.replace('\n','')+'\')" ><i class="plus outline icon"></i>Detalles</div><hr>'+point.dir);
                    markers.addLayer(marker);
                }
            }

            $scope.map.addLayer(markers);


            $scope.loading = false;
        }
    }]);
})();
