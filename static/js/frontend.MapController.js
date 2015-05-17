(function() {

  function intersect_safe(a, b){
   var ai = bi= 0;
   var result = [];

   while( ai < a.length && bi < b.length ){
      if      (a[ai] < b[bi] ){ ai++; }
      else if (a[ai] > b[bi] ){ bi++; }
      else /* they're equal */
      {
        result.push(ai);
        ai++;
        bi++;
      }
   }

   return result;
  }

  String.prototype.hashCode = function() {
    var hash = 0, i, chr, len;
    if (this.length == 0) return hash;
    for (i = 0, len = this.length; i < len; i++) {
      chr   = this.charCodeAt(i);
      hash  = ((hash << 5) - hash) + chr;
      hash |= 0; // Convert to 32bit integer
    }
    return hash;
  };

  function gen_hash(obj){
    return "hash" + JSON.stringify(obj).hashCode();
  }

  /**
   * Controlador del mapa
   */
  angular.module('frontEnd')
    .controller('MapController', ['$scope', 'backEnd', '$filter',
      '$routeParams', '$rootScope', '$timeout',
      function($scope, backEnd, $filter, $routeParams, $rootScope, $timeout) {
        $scope.activar_filtro = function(){
          $('.refresh').parent().transition('jiggle')
        };
        $scope.ubicacionSeleccionada = {};
        $scope.prioridadesSeleccionadas = {
          sanitarios: true,
          aulas: true,
          mobiliarios: true,
          otros: true
        };
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
            backEnd.establecimiento_short.get({md5:true}, function(data){
              var md5hashnew = data.hash;
              var md5hashold = '';
              var needReload = false;
              if(Storage !== 'undefined'){
                md5hashold = localStorage.getItem('establecimientoHash');
                needReload = md5hashold !== md5hashnew;
                window.mapData = localStorage.getItem('mapData');
                if(window.mapData != undefined)
                  window.mapData = JSONH.unpack(JSON.parse(window.mapData));
              }else{
                needReload = true;
              }
              if(window.mapData && !needReload){
                $scope.mapData = window.mapData;
                $scope.loading = false;
                if(window.markers == undefined)
                  $scope.actualizar(function(array){return array.filter(originalFilterFunction)});
              }else{
                backEnd.establecimiento_short.query({}, function(data) {

                  $scope.mapData = JSONH.unpack(data);
                  window.mapData = $scope.mapData;
                  if(Storage !== 'undefined'){
                    localStorage.setItem('mapData', JSON.stringify(data));
                    localStorage.setItem('establecimientoHash',md5hashnew);
                  }
                  $scope.actualizar(function(array){return array.filter(originalFilterFunction)});
                });
              }

            });

            if ($routeParams.establecimiento){
              $scope.showInfoPopUp($routeParams.establecimiento,
                $routeParams.institucion);
            }
          };

        /**
        * { hash: data}
        */
        $scope.filtros = {};
        if(Storage !== 'undefined'){
            $scope.filtros = JSON.parse(localStorage.getItem('filtros'));
            if($scope.filtros == null){
                $scope.filtros = {};
            }
        }
        $scope.filtroArray = [];
        var actualizarFiltroArray = function(){
          $scope.filtroArray = undefined;
          var filtro;
          for(index in $scope.filtros){
            filtro = $scope.filtros[index];
            if(filtro.activo){
              if($scope.filtroArray == undefined){
                $scope.filtroArray = filtro.data;
                continue;
              }
              intersect_safe($scope.filtroArray, filtro.data)
            }
          }
          if($scope.filtroArray == undefined){
            $scope.filtroArray = [];
          }
          window.filtroArray = $scope.filtroArray;
          window.filtros = $scope.filtros;
        };
        var originalFilterFunction = function(obj){
          if($scope.filtroArray.length > 0)
            return $scope.filtroArray.indexOf(obj.id) != -1;
          return obj;
        };

        $scope.filtro = function(){

            $scope.loading = true;
            var params = {};
            if($scope.ubicacionSeleccionada.check){
                params.ubicacion = $scope.ubicacionSeleccionada;
            }
            if($scope.prioridadesSeleccionadas.check){

                params.prioridades = $scope.prioridadesSeleccionadas;
                params.prioridades.rango = [$('#slider-lower').val(), $('#slider-upper').val()];
            }
            if(JSON.stringify(params) != '{}'){
                var _filtro = $scope.filtros[gen_hash(params)];
                if(_filtro){
                    $scope.filtroArray = _filtro;
                    $scope.actualizar(function(array){return array.filter(originalFilterFunction)});
                }else{
                    backEnd.filtros.query(params, function(data){
                      $scope.filtroArray = data;
                      $scope.filtros[gen_hash(params)] = data;
                      if(Storage !== 'undefined'){
                        localStorage.setItem('filtros', JSON.stringify($scope.filtros));
                      }
                      if($scope.filtroArray.length > 0){
                        $scope.actualizar(function(array){return array.filter(originalFilterFunction)});
                      }else{
                        alert('No se produjeron resultados para el filtro.');
                          $scope.loading = false;
                      }
                    });
                }
            }else{
                $scope.filtroArray = [];
                $scope.actualizar(function(array){return array.filter(originalFilterFunction)});
            }
        };
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
          if (window.markers){
            $scope.map.removeLayer(window.markers);
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

          window.markers = markers;
          $scope.loading = false;

        };
        //mostrar detalle
        $scope.mostrarDetalle = function() {};

        //mostrar adjudicaciones

         $scope.mostrarAdjudicaciones = function() {
            $scope.show_adjudicaciones = !$scope.show_adjudicaciones;
          };

        //mostrar Documentos de contraloria

         $scope.mostrarContraloria = function() {
            $scope.show_contraloria = !$scope.show_contraloria;
          };

        //filtrar

        //---------------

        //TODO: refactor
        $scope.showInfoPopUp = function(id, idInstitucion) {
          $('#map').css('width', '100%');
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

                $scope.map.invalidateSize();
                $scope.$digest();
                angular.element('.right.sidebar')
                .sidebar({
                  context: angular.element('[ng-view]'),
                  dimPage: false,
                  closable: false,
                  onVisible: function(){
                    $timeout(function(){
                      if(isNaN(lat) || isNaN(lon)){
                        alert('No se puede localizar el establecimiento.');
                      }else{
                        $('#map').css('width', '35%');
                        $scope.map.invalidateSize();
                        $scope.map.setView([lat, lon], 17);
                      }
                    },0);

                  }
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
