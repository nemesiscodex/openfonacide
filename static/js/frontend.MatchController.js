(function() {
	/**
	 * Controlador de Match Difuso
	 */
	angular.module('frontEnd')
		.controller('MatchController', ['$scope', '$location', 'backEnd', function($scope,
			$location, backEnd) {
			var $controller = this;
			
			backEnd.temporal.get({}, function(data){
				$scope.resultados = data;
			});

		}]);

})();
