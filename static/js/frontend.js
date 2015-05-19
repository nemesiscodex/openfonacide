(function(){
    var app = angular.module('frontEnd', ['ngResource','ngCookies', 'ngRoute', 'ngAnimate', 'duScroll']);

    //TODO: estos controllers tienen que tener su propio archivo
    // una vez que realmente se usen.

    app.controller('FonacideController', ['$scope', function($scope){

    }]);
    app.controller('GraficosController', ['$scope', function($scope){

    }]);

    app.filter('capitalize', function() {
  return function(input, scope) {
    if (input!=null)
    input = input.toLowerCase();
    return input.substring(0,1).toUpperCase()+input.substring(1);
  }
});


})();
