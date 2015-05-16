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
      $(element).find('.input,.label').addClass(scope.inputClass);
    }
  });
  nuevaDirectiva('resultElement', 'result-element.html', {
    scope: {
      result: '=',
      numero: '='
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
  nuevaDirectiva('match', 'match.html');
})();
