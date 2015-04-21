(function() {

	/**
	 * Controlador del mapa
	 */
	angular.module('frontEnd')
		.controller('MapController', ['$scope', 'backEnd', '$filter', '$routeParams',
			function($scope, backEnd, $filter, $routeParams) {

				//---------------
				$scope.showInfo = false;
				$scope.modalTitle = "";
				$scope.loading = true;
				$scope.infoData = {};

				$scope.showInfoPopUp = function(id, idInstitucion) {
					$scope.infoData = {};
					$scope.infoData.instituciones = [];
					$scope.institucion_actual = undefined;
					backEnd.establecimiento.get({
						id: id
					}, function(value, headers) {
						$scope.infoData.establecimiento = value;
						$scope.showInfo = true;
						backEnd.institucion.query({
							id: id
						}, function(value, headers) {


							$scope.infoData.instituciones = value;
							if ($.inArray(idInstitucion, $scope.infoData.instituciones.map(
									function(el) {
										return el.codigo_institucion
									})) >= 0)
								$scope.institucion_actual = idInstitucion;
							else
								$scope.institucion_actual = $scope.infoData.instituciones[0].codigo_institucion;
							$scope.periodo = 2015;

							// $('#info_modal').modal('show');
							// setTimeout(function(){
							//  $('#info_modal').modal('refresh');
							// },1300);
							console.log($('#ng-view'));
							$scope.$parent.$mapDirective.parent().find('.right.sidebar').sidebar({
								context: $scope.$parent.$sidebarContext,
								dimPage: false,
								closable: false
							}).sidebar('show');
						});
					});
					backEnd.prioridades.get({
						id: id
					}, function(value, headers) {
						$scope.prioridades = value;


					});


				};

				$scope.onEachFeature = function(feature, layer) {
					// Load the default style.
					layer.setStyle(defaultStyle);
					// Create a self-invoking function that passes in the layer
					// and the properties associated with this particular record.
					(function(layer, properties) {
						// Create a mouseover event
						layer.on("mouseover", function(e) {
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
								css: {
									fontSize: "16px",
									marginBottom: "3px"
								}
							}).appendTo(popup);
							// Add the popup to the map
							popup.appendTo("#map");
						});
						// Create a mouseout event that undoes the mouseover changes
						layer.on("mouseout", function(e) {
							// Start by reverting the style back
							layer.setStyle(defaultStyle);
							// And then destroying the popup
							$("#popup-" + properties.DISTRICT).remove();
						});
						// Close the "anonymous" wrapper function, and call it while passing
						// in the variables necessary to make the events work the way we want.
					})(layer, feature.properties);
				};


				$scope.update = function(filterType) {

					$scope.loading = true;

					switch (filterType) {
						case 'fonacide':
							if ($scope.ContratacionesLayer) {
								$scope.map.removeLayer($scope.ContratacionesLayer);
							}
							updateMap(function(map) {
								var ret = $filter('filter')(map, function(elemento, index) {

									return (elemento.f == 't')
								}, true);
								return ret;
							});
							break;
						case 'denunciaPrensa':
							updateMap(function(map) {
								return map;
							});
							break;
						case 'denunciaCiudadania':
							updateMap(function(map) {
								return map;
							});
							break;
						case 'informeContraloria':
							updateMap(function(map) {
								return map;
							});
							break;
						case 'contrataciones':
							/* Geojson para contratataciones */

							$scope.map.removeLayer($scope.markers);

							if (!$scope.ContratacionesLayer) {

								$scope.ContratacionesLayer = L.geoJson().addTo($scope.map);


								$.getJSON("/static/geojson/00.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/01.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/02.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/03.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/04.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/05.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/06.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/07.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/08.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/09.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/10.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/11.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/12.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/13.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/14.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/15.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/16.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});
								$.getJSON("/static/geojson/17.json", function(data) {
									$scope.ContratacionesLayer.addData(data);
								});

								$scope.ContratacionesLayer.on('mouseover', function(e) {
									e.layer.openPopup();
								});
								$scope.ContratacionesLayer.on('mouseout', function(e) {
									e.layer.closePopup();
								});


							}


							$scope.loading = false;


							/* FIN GEOJSON*/


							break;
						default:
							if ($scope.ContratacionesLayer) {
								$scope.map.removeLayer($scope.ContratacionesLayer);
							}

							updateMap(function(map) {
								return map
							});
					}
				};

				var updateMap = function(filterFunction) {

					var point;
					var marker;
					var data = filterFunction($scope.mapData);

					if ($scope.markers)
						$scope.map.removeLayer($scope.markers);

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
					var redMarker = L.AwesomeMarkers.icon({
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
								icon: redMarker
							});
							marker.bindPopup("<h4>" + point.name +
								'</h4><a class="circular ui teal icon button" href="/map/' + point.id +
								'" ><i class="plus outline icon"></i> Detalles</a><hr>' + point.dir
							);
							markers.addLayer(marker);
						}
					}

					$scope.map.addLayer(markers);


					$scope.loading = false;
				};
				$scope.$parent.$parent.initMap = function() {
					if ($routeParams.establecimiento)
						$scope.showInfoPopUp($routeParams.establecimiento, $routeParams.institucion);
					if (!$scope.$parent.mapData)
						backEnd.establecimiento_short.query({}, function(data, headers) {
							$scope.mapData = JSONH.unpack(data);
							$scope.$parent.mapData = $scope.mapData;
							$scope.update('');
						});
					else {
						$scope.mapData = $scope.$parent.mapData;
						// $scope.update('');
					}
				};

			}
		]);

})();
