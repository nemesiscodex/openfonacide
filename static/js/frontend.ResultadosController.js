(function(){
  angular.module('frontEnd')
    .controller('ResultadosController', ['$scope', '$location', '$compile',
      '$rootScope', 'backEnd', '$timeout',
          function($scope, $location, $compile, $rootScope, backEnd, $timeout){
      $scope.fetch = true;
      $scope.offset = 0;
      $scope.count = 0;
      $scope.cantidad = 20;
      $scope.tipo = 'nombre';
      $scope.tipoAnterior = 'nombre';

      $scope.$watch('tipo', function(newVal, oldVal){
        if($scope.tipoAnterior == $scope.tipo) return;
        $scope.fetch = true;
        $scope.offset = 0;
        $scope.count = 0;
        $scope.tipoAnterior = $scope.tipo;
        $('result-element').remove();
        $location.search('type', $scope.tipo);
        // fetchResults();
      });

      var fetchResults = function(){
        if(!$scope.fetch) return;
        var
          $segment = $('.results.segment'),
          $loader  = $segment.find('.inline.loader');
        $loader.addClass('active');
        var query = $.extend({}, $location.search());
        query.offset = $scope.offset;
        query.cantidad = $scope.cantidad;
        $scope.offset += $scope.cantidad;
        if(query.type){
          $scope.tipo = query.type;
          $scope.tipoAnterior = $scope.tipo;
        }
        query.tipo = $scope.tipo;

        backEnd.institucion.get(query,function(data, headers){
          var tipoResults = data.results[$scope.tipo].results;
          var $element = undefined;
          var scope = undefined;
          if(tipoResults.length == 0)
            $scope.fetch = false;
          $timeout(function(){
            $segment = $('.results.segment'),
            $loader  = $segment.find('.inline.loader');
            for(index in tipoResults){
              $scope.count++;
              $element = $('<result-element numero="numero" result="result"></result-element>');
              scope = $rootScope.$new();
              scope.numero = $scope.count;
              scope.result = tipoResults[index];
              $loader.before($compile($element)(scope));
            }
            $loader.removeClass('active');
          })
        })
      }
      // fetchResults();
      $('.results.segment')
        .visibility({
          once: false,
          // update size when new content loads
          observeChanges: true,
          // load content on bottom edge visible
          onBottomVisible: fetchResults
          // function() {
          //   // loads a max of 5 times
          //   var
          //     $segment = $('.results.segment'),
          //     $loader  = $segment.find('.inline.loader'),
          //     $content = $('<h3 class="ui header">Loaded Content #' + $scope.count + '</h3><img class="ui wireframe image" src="/images/wireframe/paragraph.png"><img class="ui wireframe image" src="/images/wireframe/paragraph.png"><img class="ui wireframe image" src="/images/wireframe/paragraph.png">')
          //   ;
          //   if($scope.count <= 5) {
          //     $loader.addClass('active');
          //     setTimeout(function() {
          //       $loader
          //         .removeClass('active')
          //         .before($content)
          //       ;
          //       // $('.visibility.example > .overlay, .visibility.example > .demo.segment, .visibility.example .items img')
          //       //   .visibility('refresh')
          //       // ;
          //     }, 1000);
          //   }
          //   $scope.count++;
          // }
        })
      ;
    }]);
})();
