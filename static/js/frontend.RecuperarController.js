(function() {
	/**
	 * Controlador de recuperacion de contraseña
	 */
	angular.module('frontEnd')
		.controller('RecuperarController', ['$scope', '$location', function($scope,
			$location) {
			var $controller = this;
			var query = $location.search();

			$controller.action = $location.$$url;

			if (query.token) {
				$controller.confirmar = true;
			} else
				$controller.confirmar = false;

			if (query.error) {
				$controller.error = query.error;
				$controller.message = query.message;

			} else if (query.success) {
				$controller.success = query.success;
				$controller.message = query.message;
			}

		}]);

})();
