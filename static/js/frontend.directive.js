(function () {
    var app = angular.module('frontEnd');

    function nuevaDirectiva(nombre, template, config) {
        if (typeof(config) != 'object')
            config = {};
        app.directive(nombre, function () {
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
        link: function (scope, element, attrs) {
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
    nuevaDirectiva('microplanificacion', 'microplanificacion.html');
    nuevaDirectiva('microplanificacion-proceso', 'microplanificacion-proceso.html');
    nuevaDirectiva('informacion', 'informacion.html');
    nuevaDirectiva('home', 'home.html');
    nuevaDirectiva('siteNav', 'nav.html');
    nuevaDirectiva('match', 'match.html');

    nuevaDirectiva('filtroUbicacion', 'filtro-ubicacion.html', {
        scope: {
            multiple: "=",
            seleccionados: "=?",
            seleccionado: "=?",
            activado: "=?",
            callback: '='
        },
        link: function (scope, element, attrs, ctrl) {
            ctrl.multiple = scope.multiple;
            ctrl.selected = scope.seleccionado;
            ctrl.callback = (typeof (scope.callback) == 'function') ? scope.callback : function () {/* no-op */};
        },
        controllerAs: 'ctrl',
        controller: ['backEnd', '$scope', '$timeout', function (backEnd, $scope, $timeout) {
            var $control = this;
            if (typeof($control.selected) != 'object') {
                $control.selected = {
                    departamento: '',
                    distrito: '',
                    barrio: '',
                    check: false
                };
            }
            $scope.$watch('ctrl.selected.check', function(value){
                $scope.activado = value;
            });
            $scope.seleccionados = [];
            $control.cambioDepartamento = function () {
                $control.distritos = [];
                $control.barrios = [];
                $control.selected.distrito = "";
                $control.selected.barrio = "";
                for (i in $control.ubicaciones) {
                    if ($control.ubicaciones[i].id == $control.selected.departamento) {
                        $control.distritos = $control.ubicaciones[i].distritos;
                        break;
                    }
                }
                //Esto es por https://docs.angularjs.org/error/$rootScope/inprog?p0=$digest#triggering-events-programmatically
                $timeout(function () {
                    $('#ubicacion-distrito .dropdown,#ubicacion-barrio .dropdown').dropdown('clear');
                }, 0, false);

            };
            $control.cambioDistrito = function () {
                $control.barrios = [];
                $control.selected.barrio = "";
                for (i in $control.distritos) {
                    if ($control.distritos[i].id == $control.selected.distrito) {
                        $control.barrios = $control.distritos[i].barrios;
                        break;
                    }
                }
                $timeout(function () {
                    $('#ubicacion-barrio .dropdown').dropdown('clear');
                }, 0, false);
            };
            var cargarUbicacion = function () {
                //PLACEHOLDER
                backEnd.ubicaciones.get({}, function (data) {
                    var ubicaciones = data;

                    $control.distritos = [];
                    $control.barrios = [];
                    $control.ubicaciones = ubicaciones;

                    $timeout(function () {
                        // $('.ui.checkbox').checkbox();
                        $('.dropdown').dropdown();
                    }, 300, false);
                });

            };
            cargarUbicacion();
            $control.agregarUbicacion = function () {
                if (!$control.selected.departamento) {
                    return;
                }
                var flecha = " &#x279c; ";
                var seleccion = "";
                if ($scope.seleccionados
                        .filter(function (obj) {
                            return obj[0] == $control.selected.departamento
                                && obj[1] == $control.selected.distrito
                                && obj[2] == $control.selected.barrio;
                        }).length > 0) {
                    return;
                }
                $scope.seleccionados.push(
                    [$control.selected.departamento, $control.selected.distrito, $control.selected.barrio]
                );
                var depObj, disObj, barObj;

                depObj = $control.ubicaciones
                    .filter(function (obj) {
                        return obj.id == $control.selected.departamento;
                    });
                seleccion += depObj
                    .map(function (obj) {
                        return obj.nombre;
                    })
                    .reduce(function (a, b) {
                        return a + b;
                    });

                depObj = depObj[0];
                if ($control.selected.distrito) {
                    disObj = depObj.distritos
                        .filter(function (obj) {
                            return obj.id == $control.selected.distrito;
                        });
                    seleccion += flecha + disObj
                            .map(function (obj) {
                                return obj.nombre;
                            })
                            .reduce(function (a, b) {
                                return a + b;
                            });
                    disObj = disObj[0];
                }
                if ($control.selected.barrio) {
                    barObj = disObj.barrios
                        .filter(function (obj) {
                            return obj.id == $control.selected.barrio;
                        });
                    seleccion += flecha + barObj
                            .map(function (obj) {
                                return obj.nombre;
                            })
                            .reduce(function (a, b) {
                                return a + b;
                            });
                    barObj = barObj[0];
                }
                $('#ubicacion-labels').append(
                    $('<div class="ui label" style="margin-bottom: 5px" data-dep="' + $control.selected.departamento + '" data-dis="' + $control.selected.distrito + '" data-bar="' + $control.selected.barrio + '"></div>')
                        .html(seleccion)
                        .append(
                        $('<i class="delete icon"></i>')
                            .click(function () {
                                var label = $(this).parent();
                                $scope.seleccionados = $scope.seleccionados
                                    .filter(function (obj) {
                                        return !(obj[0] == label.data('dep')
                                        && obj[1] == label.data('dis')
                                        && obj[2] == label.data('bar'));
                                    });
                                label.remove();
                                $timeout(function(){
                                    $scope.$apply();
                                },0,false);
                            })
                    )
                );
            };
            $control.limpiarUbicacion = function () {
                $timeout(function () {
                    $('#ubicacion .ui.dropdown').dropdown('clear');
                }, 0, false);
            };
            $control.borrarUbicaciones = function () {
                $scope.seleccionados = [];
                $timeout(function () {
                    $('#ubicacion-labels .ui.label').remove();
                    $scope.$digest();
                }, 0, false);
            };

        }]
    });

})();
