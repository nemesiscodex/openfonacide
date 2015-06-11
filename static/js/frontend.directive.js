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
            var size = (scope.inputClass === 'massive')? '140px' : '100px';
            var $input = $(element).find('.icon.input');
            var $dropdown = $(element).find('.dropdown.busqueda');
            $dropdown.addClass(scope.inputClass);
            $input.addClass(scope.inputClass);
            console.log($dropdown.css('height'));
            $input.css('width', 'calc(100% - ' + size + ')');
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
    nuevaDirectiva('agregarAdjudicacion', 'agregar-adjudicacion.html');
    nuevaDirectiva('institucionList', 'institucion-list.html');
    nuevaDirectiva('visualizaciones', 'visualizaciones.html');
    nuevaDirectiva('microplanificacion', 'microplanificacion.html');
    nuevaDirectiva('microplanificacion-proceso', 'microplanificacion-proceso.html');
    nuevaDirectiva('informacion', 'informacion.html');
    nuevaDirectiva('home', 'home.html');
    nuevaDirectiva('siteNav', 'nav.html');
    nuevaDirectiva('linkbreak', 'linkbreak.html');
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
                        $('#ubicacion').find('.ui.dropdown').dropdown();
                    }, 300, false);
                });

            };
            cargarUbicacion();
            $scope.obtenerTextoUbicacion = function(selected, excluirPadres, incluirHojaNoRaiz, separador){
                if(separador == undefined){
                    separador = " &#x279c; ";
                }
                var seleccion = "";
                if (excluirPadres == undefined){
                    excluirPadres = false;
                }
                if (incluirHojaNoRaiz == undefined){
                    incluirHojaNoRaiz = true;
                }
                var depObj, disObj, barObj;

                depObj = $control.ubicaciones
                    .filter(function (obj) {
                        return obj.id == selected[0];
                    });
                if(!excluirPadres || (!selected[1])){
                    seleccion += depObj
                        .map(function (obj) {
                            return obj.nombre;
                        })
                        .reduce(function (a, b) {
                            return a + b;
                        });
                }

                depObj = depObj[0];
                if (selected[1]) {
                    disObj = depObj.distritos
                        .filter(function (obj) {
                            return obj.id == selected[1];
                        });

                    if((!excluirPadres || (!selected[2])) && (incluirHojaNoRaiz || !!selected[2])){
                        if(seleccion != ''){
                            seleccion += separador;
                        }
                        seleccion += disObj
                                .map(function (obj) {
                                    return obj.nombre;
                                })
                                .reduce(function (a, b) {
                                    return a + b;
                                });
                    }
                    disObj = disObj[0];
                }
                if (selected[2]) {
                    barObj = disObj.barrios
                        .filter(function (obj) {
                            return obj.id == selected[2];
                        });


                    if(incluirHojaNoRaiz){
                        if(seleccion != ''){
                            seleccion += separador;
                        }
                        seleccion += barObj
                            .map(function (obj) {
                                return obj.nombre;
                            })
                            .reduce(function (a, b) {
                                return a + b;
                            });
                    }
                    barObj = barObj[0];
                }
                return seleccion;

            };
            $control.agregarUbicacion = function () {
                var selected = [];
                if (!$control.selected.departamento) {
                    return;
                }
                if ($scope.seleccionados
                        .filter(function (obj) {
                            return obj[0] == $control.selected.departamento
                                && obj[1] == $control.selected.distrito
                                && obj[2] == $control.selected.barrio;
                        }).length > 0) {
                    return;
                }
                selected = [$control.selected.departamento, $control.selected.distrito, $control.selected.barrio];
                $scope.seleccionados.push(selected);

                $('#ubicacion-labels').append(
                    $('<div class="ui label" style="margin-bottom: 5px" data-dep="' + $control.selected.departamento + '" data-dis="' + $control.selected.distrito + '" data-bar="' + $control.selected.barrio + '"></div>')
                        .html($scope.obtenerTextoUbicacion(selected))
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
