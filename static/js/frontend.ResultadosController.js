(function(){
  angular.module('frontEnd')
    .controller('ResultadosController', ['$scope', '$location', '$compile',
      '$rootScope', 'backEnd', '$timeout', '$routeParams',
          function($scope, $location, $compile, $rootScope, backEnd, $timeout, $routeParams){
      $scope.fetch = true;
      $scope.offset = 0;
      $scope.query = $routeParams.q.toUpperCase();
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
          var $element = undefined, $compiledElement;
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
              $compiledElement = $compile($element)(scope);
              $loader.before($compiledElement);
              scope.$apply();
            }
            if(isNaN(data.query))
              $timeout(function(){
                var queryUp = data.query.toUpperCase();
                $.each($('result-element'), function(index, el){
                  $(el).html($(el).html().replace(queryUp, '<span class="highlight">'+queryUp+'</span>'));
                });
                $scope.$apply();
              },20);
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
