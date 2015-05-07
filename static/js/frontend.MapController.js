(function() {

  /**
   * Controlador del mapa
   */
  angular.module('frontEnd')
    .controller('MapController', ['$scope', 'backEnd', '$filter',
      '$routeParams', '$rootScope', '$timeout',
      function($scope, backEnd, $filter, $routeParams, $rootScope, $timeout) {
        $scope.scrollTo = function (id) {
          $location.hash(id);
          $anchorScroll();
        };
        $scope.create = function (){

          if(window.mapLoaded){
            $scope.inicializar();
            $timeout(function(){
              angular.element('.mapContainer').html(window.mapElement);
            });
            $scope.map = window.map;
            return;
          }
          window.mapLoaded = true;

          var map = L.map('map')
            .setView([-25.308, -57.6], 13);

          /* Open Street Map */
          //Mapnik
          var osmMapnikLayer = L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            });
          //B&W
          var osmBWLayer = L.tileLayer(
            'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            });
          //DE
          var osmDELayer = L.tileLayer(
            'http://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            });
          //HOT
          var osmHOTLayer = L.tileLayer(
            'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, Tiles courtesy of <a href="http://hot.openstreetmap.org/" target="_blank">Humanitarian OpenStreetMap Team</a>'
            });
          /* ThunderForest */
          //OpenCycleMap
          var thunderforestOpenCycleMapLayer = L.tileLayer(
            'http://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://www.opencyclemap.org">OpenCycleMap</a>, &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            });
          /* CartoDB*/
          //Positron
          var cartodbPositronLayer = L.tileLayer(
            'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
              subdomains: 'abcd',
              minZoom: 0,
              maxZoom: 18
            });

          var baseLayers = {
            "Open Street Map - Mapnik": osmMapnikLayer,
            "Open Street Map - Blanco y Negro": osmBWLayer,
            "Open Street Map - DE": osmDELayer,
            "Open Street Map - HOT": osmHOTLayer,
            "ThunderForest - Open Cycle Map": thunderforestOpenCycleMapLayer,
            "CartoDB - Positron": cartodbPositronLayer
          };

          var layerControl = L.control.groupedLayers(baseLayers, {}, {});
          map.addControl(layerControl);

          osmMapnikLayer.addTo(map);
          window.map = map;
          $scope.map = map;
          $timeout(function(){
            window.mapElement = angular.element('#map')[0];
          });
          $scope.inicializar();
        };
        //inizializar
        $scope.inicializar = function() {
						$scope.last = {};
            //
            $scope.modalTitle = "";
            //
            $scope.loading = true;
            //{verified}
            $scope.infoData = {};
            //
            $scope.infoData.instituciones = [];
            //
            $scope.institucion_actual = undefined;
            //
            $scope.periodo = 2015;

            if(window.mapData){
              $scope.mapData = window.mapData;
              $scope.loading = false;
            }else{
              backEnd.establecimiento_short.query({}, function(data) {

                $scope.mapData = JSONH.unpack(data);
                window.mapData = $scope.mapData;
                $scope.actualizar();
              });
            }
            if ($routeParams.establecimiento){
              $scope.showInfoPopUp($routeParams.establecimiento,
                $routeParams.institucion);
            }
          }
          //actualizar/filtrar
        $scope.actualizar = function(filterFunction) {
          var point;
          var marker;
          var data = {};
          if (typeof(filterFunction) === 'function'){
            data = filterFunction($scope.mapData);
          }else{
            data = $scope.mapData;
          }
          if ($scope.markers){
            $scope.map.removeLayer($scope.markers);
          }
          $scope.markers = new L.MarkerClusterGroup({

            iconCreateFunction: function(cluster) {
              return L.divIcon({
                html: cluster.getChildCount(),
                className: 'mycluster',
                iconSize: L.point(40, 40)
              });
            }
          });
          var markers = $scope.markers;
          var grayMarker = L.AwesomeMarkers.icon({
            prefix: '',
            icon: ' university icon margin-left',
            markerColor: 'gray',
            extraClasses: 'info icon'
          });
          if (data) {
            for (var i = 0; i < data.length; i++) {
              point = data[i];
              marker = new L.Marker([point.lat, point.lon], {
                title: point.name,
                icon: grayMarker
              });
              marker.bindPopup("<h4>" + point.name +
                '</h4><a class="circular ui teal icon button" href="/map?establecimiento=' +
                point.id +
                '" ><i class="plus outline icon"></i> Detalles</a><hr>' +
                point.dir
              );
              markers.addLayer(marker);
            }
          }

          $scope.map.addLayer(markers);


          $scope.loading = false;

        };
        //mostrar detalle
        $scope.mostrarDetalle = function() {};

        //mostrar adjudicaciones

         $scope.mostrarAdjudicaciones = function() {
            $scope.show_adjudicaciones = !$scope.show_adjudicaciones;
          };

        //filtrar

        //---------------

        //TODO: refactor
        $scope.showInfoPopUp = function(id, idInstitucion) {
          $scope.establecimiento = id;
          if(!idInstitucion){
            idInstitucion = '';
          }
          if($scope.last.codigo_establecimiento === id
                && $scope.last.codigo_institucion === idInstitucion){
            return;
          }
          $scope.last = {"codigo_establecimiento":id, "codigo_institucion":idInstitucion};
          //{verified}
          $scope.infoData = {};
          //
          $scope.infoData.instituciones = [];
          //
          $scope.institucion_actual = undefined;
          //
          $scope.periodo = 2015;
          var establecimiento_nuevo = {};
          var instituciones_nuevas = [];
          backEnd.establecimiento.get({
            id: id
          }, function(value) {
            establecimiento_nuevo = value;
            var lat = parseFloat(establecimiento_nuevo.latitud);
            var lon = parseFloat(establecimiento_nuevo.longitud);

            if(isNaN(lat) || isNaN(lon)){
              alert('No se puede localizar el establecimiento.');
            }else{
              $scope.map.setView([lat, lon], 16);
            }

            backEnd.institucion.query({
              id: id
            }, function(value) {
              instituciones_nuevas = value;
              // $scope.infoData.instituciones = value;

              $scope.infoData.instituciones = instituciones_nuevas;
              $scope.infoData.establecimiento = establecimiento_nuevo;
              //Verifica consistencia de datos
              if ($.inArray(idInstitucion, $scope.infoData.instituciones
                  .map(
                    function(el) {
                      return el.codigo_institucion;
                    })) >= 0){
                $scope.institucion_actual = idInstitucion;
              }else{
                $scope.institucion_actual = instituciones_nuevas[
                  0].codigo_institucion;
              }
              $timeout(function(){
                $scope.$digest();
                angular.element('.right.sidebar')
                .sidebar({
                  context: angular.element('[ng-view]'),
                  dimPage: false,
                  closable: false
                })
  							.sidebar('show');

              });


            });
          });
          backEnd.prioridades.get({
            id: id
          }, function(value) {
            $scope.prioridades = value;
          });


        };
        $scope.create();

      }
    ]);

})();
