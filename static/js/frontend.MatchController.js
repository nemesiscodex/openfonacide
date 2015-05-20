(function() {
	/**
	 * Controlador de Match Difuso
	 */
	angular.module('frontEnd')
		.controller('MatchController', ['$scope', 'backEnd', function($scope, backEnd) {

			backEnd.temporal.get({}, function(data){
				$scope.resultados = data;
			});

		}]);

})();
