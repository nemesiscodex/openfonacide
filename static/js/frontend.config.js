(function() {
	angular.module('frontEnd')
		//Proteccion contra Cross Site Request Forgery
		.run(function($http, $cookies) {
			$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
		})
		//Cambia simbolos de angular de {{ }} a {$ $}
		//(compatibilidad django template)
		.config(function($interpolateProvider) {
			$interpolateProvider.startSymbol('{$');
			$interpolateProvider.endSymbol('$}');
		})
		.config(['$resourceProvider', function($resourceProvider) {
			// Don't strip trailing slashes from calculated URLs
			$resourceProvider.defaults.stripTrailingSlashes = false;
		}])
		//Rutas
		.config(['$routeProvider', '$locationProvider',
			function($routeProvider, $locationProvider) {
				$routeProvider
					.when('/', {
						templateUrl: 'partials/home.html',
					})
					.when('/accounts/login/', {
						templateUrl: 'partials/registration/login.html'
					})
					.when('/accounts/recuperar/', {
						controller: 'RecuperarController',
						controllerAs: 'recCtrl',
						templateUrl: 'partials/registration/recuperar.html'
					})
					.when('/map/', {
						controller: 'MapController',
						templateUrl: 'partials/map.html',
						reloadOnSearch: false
					})
					.when('/resumen/', {
						controller: 'ResumenController',
						templateUrl: 'partials/resumen.html'
					})
					.when('/graficos/', {
						controller: 'GraficosController',
						templateUrl: 'partials/graficos.html'
					})
					.when('/fonacide/', {
						controller: 'FonacideController',
						templateUrl: 'partials/fonacide.html'
					})
					.when('/match/', {
						controller: 'MatchController',
						templateUrl: 'partials/match.html',
						controllerAs: 'controller'
					})
					.when('/microplanificacion/', {
						controller: 'FonacideController',
						templateUrl: 'partials/microplanificacion.html'
					})
					.when('/microplanificacion-proceso/', {
						controller: 'FonacideController',
						templateUrl: 'partials/microplanificacion-proceso.html'
					})
					.when('/informacion/', {
						controller: 'FonacideController',
						templateUrl: 'partials/informacion.html'
					})
					.when('/acercade/', {
						controller: 'FonacideController',
						templateUrl: 'partials/acercade.html'
					})
					.when('/datasets/', {
						controller: 'FonacideController',
						templateUrl: 'partials/datasets.html'
					})
					.when('/legal/', {
						controller: 'FonacideController',
						templateUrl: 'partials/legal.html'
					})
					.when('/results', {
						controller: 'ResultadosController',
						templateUrl: 'partials/results.html'
					});

				$locationProvider.html5Mode(true);
			}
		]);;
})();
