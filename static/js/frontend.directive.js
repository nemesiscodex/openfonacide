(function() {
	var app = angular.module('frontEnd');

	function nuevaDirectiva(nombre, template, config) {
		if (typeof(config) != 'object')
			config = {};
		app.directive(nombre, function() {
			return $.extend({
				restrict: 'E',
				templateUrl: 'partials/' + template
			}, config);
		});
	}

	/**
	 * Directivas
	 */

	nuevaDirectiva('search', 'search.html', {
		scope: {
			inputClass: '@'
		},
		link: function(scope, element, attrs) {
			$(element).find('.input').addClass(scope.inputClass);
		}
	});
	nuevaDirectiva('mapDirective', 'map-directive.html', {
		link: function(scope, element, attrs, controller) {
			if (scope.$parent.$parent.$mapElement) {
				angular.element(element).parent().html(scope.$parent.$parent.$mapElement);
				scope.$parent.$parent.initMap();
				return;
			}
			scope.$parent.$parent.$mapElement = $(element).find('#map');

			scope.$parent.$mapDirective = $(element);
			if (scope.$parent.$parent.map)
				scope.$parent.$parent.map.remove();
			var map = L.map($(element).find('#map')[0]).setView([-25.308, -57.6], 13);

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
			scope.$parent.$parent.map = map;

			(function() {
				scope.$parent.$parent.$sidebarContext = $(element).parent();
				$(element).parent().find('.sidebar').sidebar({
					context: scope.$parent.$parent.$sidebarContext,
					dimPage: false,
					closable: false
				});

				$('.ui.checkbox').checkbox();

				$('.ui.dropdown').dropdown();

				$(element).parent().find(".filter.launch").click(function() {
					$('.left.sidebar').sidebar('toggle');
				});
			})();
			scope.$parent.$parent.initMap();
		}
	});
	nuevaDirectiva('footerInfo', 'footer.html');
	nuevaDirectiva('api', 'api.html');
	nuevaDirectiva('loginModal', 'login.html');
	nuevaDirectiva('denunciaModal', 'denuncia.html');
	nuevaDirectiva('archivosContraloria', 'archivos-contraloria.html');
	nuevaDirectiva('institucionList', 'institucion-list.html');
	nuevaDirectiva('visualizaciones', 'visualizaciones.html');
	nuevaDirectiva('home', 'home.html');
	nuevaDirectiva('siteNav', 'nav.html');
	nuevaDirectiva('institucionModal', 'institucion-modal.html');
	nuevaDirectiva('establecimientoTabla',
		'institucion-modal/establecimiento-tabla.html');
	nuevaDirectiva('institucionesTabla',
		'institucion-modal/instituciones-tabla.html');
	nuevaDirectiva('comentarios', 'institucion-modal/comentarios.html');
	nuevaDirectiva('aulas', 'institucion-modal/instituciones-tabs/aulas.html');
	nuevaDirectiva('mobiliarios',
		'institucion-modal/instituciones-tabs/mobiliarios.html');
	nuevaDirectiva('denuncias',
		'institucion-modal/instituciones-tabs/denuncias.html');
	nuevaDirectiva('sanitarios',
		'institucion-modal/instituciones-tabs/sanitarios.html');
	nuevaDirectiva('informacion',
		'institucion-modal/instituciones-tabs/informacion.html');
	nuevaDirectiva('fonacide', 'institucion-modal/fonacide.html');
	nuevaDirectiva('resumen', 'institucion-modal/fonacide.html');


})();
