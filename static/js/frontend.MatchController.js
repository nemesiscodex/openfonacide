(function() {
	/**
	 * Controlador de Match Difuso
	 */
	angular.module('frontEnd')
		.controller('MatchController', ['$scope', 'backEnd', 'DTOptionsBuilder', 'DTColumnDefBuilder', function($scope, backEnd, DTOptionsBuilder, DTColumnDefBuilder) {
            // STILL IMPROVING!
            var controller = this;
            var page_size = 10;
            var page_number = 1;
            controller.dtOptions = DTOptionsBuilder.newOptions()
            .withPaginationType('full_numbers')
            .withDisplayLength(page_size);

			backEnd.temporal.get({offset:(page_number - 1), limit: page_size}, function(data){
				$scope.resultados = data;
			});

		}]);

})();
