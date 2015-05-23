(function () {
    /**
     * Controlador de Match Difuso
     */
    angular.module('frontEnd')
        .controller('MatchController', ['$scope', 'backEnd', 'DTOptionsBuilder', 'DTDefaultOptions','$timeout', function ($scope, backEnd, DTOptionsBuilder, DTDefaultOptions, $timeout) {
            // STILL IMPROVING!

            var controller = this;
            controller.guardar = function(){
                $('.checkbox input:checked').each(function (idx, el) {
                    console.log($(el).data('llamado') + '-' + $(el).data('institucion'));
                })
            };
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
            $.fn.dataTableExt.oStdClasses.sPageButton = 'ui basic button';
            $.fn.dataTableExt.oStdClasses.sInfo = 'ui white message sInfo';
            $.fn.dataTableExt.oStdClasses.sFilterInput = 'ui basic input';
            $.fn.dataTableExt.oStdClasses.sLength = 'ui top attached white message sLength';
            $.fn.dataTableExt.oStdClasses.sFilter = 'ui bottom attached white message sFilter';
            controller.dtOptions = DTOptionsBuilder.newOptions()
                .withOption('bProcessing','true')
                .withOption('drawCallback', function(){
                    var save_button = $('<button>Guardar</button>')
                        .addClass('ui teal tiny button right floated save-button')
                        .css('margin-top','-5px');

                    if($('.sLength .save-button').length == 0){
                        $('.sLength').append(save_button);
                    }
                    if($('.sInfo .save-button').length == 0){
                        $('.sInfo').append(save_button.clone());
                    }
                    $('.save-button').click(controller.guardar);
                    $('#toggle').click(function(){
                        $('.match.checkbox:visible').checkbox('toggle');
                    });
                });
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
