(function() {

	/**
	 * Controlador de la pagina
	 */
	angular.module('frontEnd')
		.controller('PageController', ['$scope', '$location', function($scope,
			$location) {
			$controller = this;
			$controller.tab = 'home';
			$controller.subTab = 'info';

			$scope.$location = $location;

			$scope.setSubTab = function(tabName) {
				$controller.subTab = tabName;
			};
			$scope.getSubTab = function() {
				return $controller.subTab
			};
			$scope.isSubTab = function(tabName) {
				return $controller.subTab === tabName;
			};

			$scope.setTab = function(tabName) {
				$controller.tab = tabName;
			};
			$scope.getTab = function() {
				return $controller.tab
			};
			$scope.isTab = function(tabName) {
				return $controller.tab === tabName;
			}
		}]);
})();
