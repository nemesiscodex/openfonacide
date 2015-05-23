(function () {
    /**
     * Controlador de Match Difuso
     */
    angular.module('frontEnd')
        .controller('MatchController', ['$scope', 'backEnd', 'DTOptionsBuilder', 'DTDefaultOptions', function ($scope, backEnd, DTOptionsBuilder, DTDefaultOptions) {
            // STILL IMPROVING!
            var controller = this;
            controller.matches = [];
            var page_size = 1000;
            var page_number = 1;
            DTDefaultOptions.setLanguage({sProcessing:     "Procesando...",
            sLengthMenu:     "Mostrar _MENU_ registros",
                sZeroRecords:    "No se encontraron resultados",
                sEmptyTable:     "Ningún dato disponible en esta tabla",
                sInfo:           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                sInfoEmpty:      "Mostrando registros del 0 al 0 de un total de 0 registros",
                sInfoFiltered:   "(filtrado de un total de _MAX_ registros)",
                sInfoPostFix:    "",
                sSearch:         "Buscar:",
                sUrl:            "",
                sInfoThousands:  ",",
                sLoadingRecords: "Cargando...",
                oPaginate: {
                sFirst:    "Primero",
                    sLast:     "Último",
                    sNext:     "Siguiente",
                    sPrevious: "Anterior"
            }});
            controller.dtOptions = DTOptionsBuilder.newOptions()
                .withOption('bProcessing','true');
                /*
                .withColumnFilter({
                    aoColumns: [null,
                    {
                        type: 'number'
                    }, {
                        type: 'text',
                        bRegex: 'true',
                        bSmart: 'true'

                    }, {
                        type: 'text',
                        bRegex: 'true',
                        bSmart: 'true'
                    }, {
                        type: 'number'
                    }, {
                        type: 'text',
                        bRegex: 'true',
                        bSmart: 'true'
                    }, {
                        type: 'number'
                    }, {
                        type: 'text',
                        bRegex: 'true',
                        bSmart: 'true'
                    }, {
                        type: 'text',
                        bRegex: 'true',
                        bSmart: 'true'
                    }
                    ]
                });*/


            backEnd.temporal.get({}, function (data) {
                $scope.resultados = data;
            });
        }]);

})();
