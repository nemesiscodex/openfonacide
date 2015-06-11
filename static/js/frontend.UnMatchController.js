(function () {
    /**
     * Controlador de UnMatch, rompe la relación entre Institucion y Planificación/Adjudicación
     */
    angular.module('frontEnd')
        .controller('UnMatchController', ['$scope', 'backEnd', 'DTOptionsBuilder', 'DTDefaultOptions', '$timeout', function ($scope, backEnd, DTOptionsBuilder, DTDefaultOptions, $timeout) {

            var controller = this;
            controller.guardar = function () {
                var data_list = new Array();
                $('.checkbox input:checked').each(function (idx, el) {
                    var tmp_obj = {
                        'id_llamado': $(el).data('llamado'),
                        'codigo_institucion': $(el).data('institucion'),
                        'periodo': $(el).data('periodo'),
                        'indice': $(el).data('indice'),
                        'id': $(el).data('databaseid'),
                        'idp': $(el).data('databaseidp')
                    };
                    data_list.push(tmp_obj);
                });
                $('#each_unmatch_controller').addClass('active');
                $('#each_unmatch_controller').show();
                backEnd.unlink.save(JSON.stringify(data_list), function (data) {
                    var respuesta_list = data['resultado'];
                    var resultados = $scope.resultados;
                    for (var respuesta in respuesta_list) {
                        resultados.splice(respuesta_list[respuesta], 1);
                    }

                }).$promise.finally(function () {
                        $('#each_unmatch_controller').removeClass('active');
                        $('#each_unmatch_controller').hide();
                    });

            };
            DTDefaultOptions.setLanguage({
                sProcessing: "Procesando...",
                sLengthMenu: "Mostrar _MENU_ registros",
                sZeroRecords: "No se encontraron resultados",
                sEmptyTable: "Ningún dato disponible en esta tabla",
                sInfo: "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                sInfoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
                sInfoFiltered: "(filtrado de un total de _MAX_ registros)",
                sInfoPostFix: "",
                sSearch: "Buscar:",
                sUrl: "",
                sInfoThousands: ",",
                sLoadingRecords: "Cargando...",
                oPaginate: {
                    sFirst: "Primero",
                    sLast: "Último",
                    sNext: "Siguiente",
                    sPrevious: "Anterior"
                }
            });
            $.fn.dataTableExt.oStdClasses.sPageButton = 'ui basic button';
            $.fn.dataTableExt.oStdClasses.sInfo = 'ui white message sInfo';
            $.fn.dataTableExt.oStdClasses.sFilterInput = 'ui basic input';
            $.fn.dataTableExt.oStdClasses.sLength = 'ui top attached white message sLength';
            $.fn.dataTableExt.oStdClasses.sFilter = 'ui bottom attached white message sFilter';
            controller.dtInstance = {};
            controller.dtOptions = DTOptionsBuilder.newOptions()
                .withOption('bProcessing', 'true')
                .withOption('drawCallback', function () {
                    var save_button = $('<button>Eliminar Relación</button>')
                        .addClass('ui teal tiny button right floated save-button')
                        .css('margin-top', '-5px');
                    var each_unmatch_loader = $('<div id="each_unmatch_loader" class="ui text loader mini">Espere...</div>');

                    if ($('.sLength .save-button').length == 0) {
                        $('.sLength').append(each_unmatch_loader);
                        $('.sLength').append(save_button);
                    }
                    if ($('.sInfo .save-button').length == 0) {
                        $('.sLength').append(each_unmatch_loader);
                        $('.sInfo').append(save_button.clone());
                    }
                    $('.save-button').click(controller.guardar);
                    $('#toggle').click(function () {
                        $('.unmatch.checkbox:visible').checkbox('toggle');
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
            var makeJoinListArray = function (instituciones) {

                var res = new Array();

                for (var i in instituciones) {
                    var planificaciones = instituciones[i].planificaciones
                    for (var p in planificaciones) {
                        var el = {};
                        for (var parameter in instituciones[i]) {
                            if (parameter != "planificaciones") {
                                el[parameter] = instituciones[i][parameter];
                            }
                        }
                        for (var parameter in planificaciones[p]) {
                            if (parameter == "id") {
                                el["idp"] = planificaciones[p][parameter];
                            } else {
                                el[parameter] = planificaciones[p][parameter];
                            }
                        }
                        res.push(el);
                    }
                }
                return res;

            };
            backEnd.unlink.get({}, function (data) {
                $scope.cargando = true;
                $('#unmatch_loader').show();

                $scope.resultados = makeJoinListArray(data);

                //$scope.resultados = data;

            }).$promise.finally(function () {
                    $scope.cargando = false;
                    $('#unmatch_loader').hide();
                });
        }]);

})();
