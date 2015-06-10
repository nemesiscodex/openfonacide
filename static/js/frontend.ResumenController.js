(function(){
    function get_options_pie(titulo, subtitulo, legendData, series){
        return {
            title: {
                text: titulo,
                subtext: subtitulo,
                x: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: function(params, ticket, callback){
                    var html = params.seriesName + " <br/>"+ params.name + " : " + params.value ;
                    if(params.indicator){
                        html += " (" + params.indicator + "%)";
                    }
                    return html;
                }
            },
            legend: {
                orient: 'vertical',
                x: 'left',
                data: legendData
            },
            toolbox: {
                show: true,
                feature: {
                    //mark: {show: true},
                    //dataView: {show: true, readOnly: true},
                    dataView : {
                        show : true,
                        title : 'Ver datos',
                        readOnly: true,
                        lang: ['Datos', 'Cerrar', 'Actualizar']
                    },
                    magicType: {
                        show: true,
                        type: ['pie', 'funnel'],
                        title: {
                            pie: 'Gráfico circular',
                            funnel: 'Gráfico de embudo'
                        }
                    },
                    restore: {
                        show: true,
                        title: 'Restaurar'
                    },
                    saveAsImage: {
                        show: true,
                        title: 'Guardar como imagen'
                    }
                }
            },
            series: series
        };
    }

    function get_options_bar(titulo, subtitulo, legendData, legendSelected, categoryData, series){
        return {
            title : {
                text: titulo,
                subtext: subtitulo,
                x: 'center'
            },
            tooltip : {
                trigger: 'axis'
            },
            legend: {
                data: legendData,
                orient: 'vertical',
                x: 'left',
                selected: legendSelected
            },
            grid: {y: 70, y2:30, x: 180, x2: 30},
            toolbox: {
                show: true,
                feature: {
                    dataView : {
                        show : true,
                        title : 'Ver datos',
                        readOnly: true,
                        lang: ['Datos', 'Cerrar', 'Actualizar']
                    },
                    magicType: {
                        show: true,
                        type: ['bar', 'line'],
                        title: {
                            bar: 'Gráfico de barras',
                            line: 'Gráfico de lineas'
                        }
                    },
                    restore: {
                        show: true,
                        title: 'Restaurar'
                    },
                    saveAsImage: {
                        show: true,
                        title: 'Guardar como imagen'
                    }
                }
            },
            xAxis : [
                {
                    type : 'category',
                    data : categoryData
                },
                {
                    type : 'category',
                    axisLine: {show:false},
                    axisTick: {show:false},
                    axisLabel: {show:false},
                    splitArea: {show:false},
                    splitLine: {show:false},
                    data : categoryData
                }
            ],
            yAxis : [
                {
                    name: 'Cantidad',
                    type : 'value'
                },
                {
                    name: 'Beneficiados',
                    type : 'value'
                }
            ],
            series: series
        }
    }

    function get_series_doble_pie(innerTitle, innerData, outerTittle, outerData){
        return [
            {
                name: innerTitle,
                type: 'pie',
                selectedMode: 'single',
                radius: '55%',
                center: ['25%', '60%'],
                itemStyle : {
                    normal : {
                        label: {
                            position: 'inner',
                            textStyle: {
                                fontWeight: 'bold',
                                color: '#555'
                            },
                            formatter: function(params){
                                if(params.percent){
                                    return params.value + "\n(" + params.percent + "%)";
                                }
                                return params.value;
                            }

                        },
                        labelLine: false
                    }
                },
                // for funnel
                x: '26%',
                width: '25%',
                funnelAlign: 'right',
                max: innerData.map(function(obj){return obj.value}).reduce(function(a, b){ return (a>b)? a:b;}, 0),
                data: innerData
            },
            {
                name: outerTittle,
                type: 'pie',
                radius: '60%',
                center: ['70%', '60%'],
                itemStyle : {
                    normal : {
                        label: {
                            position: 'inner',
                            textStyle: {
                                fontWeight: 'bold',
                                color: '#555'
                            },
                            formatter: function(params){
                                if(params.percent){
                                    return params.value + "\n(" + params.percent + "%)";
                                }
                                return params.value;
                            }

                        },
                        labelLine: false
                    }
                },
                // for funnel
                x: '51%',
                width: '25%',
                funnelAlign: 'left',
                max: outerData.map(function(obj){return obj.value}).reduce(function(a, b){ return (a>b)? a:b;}, 0),

                data: outerData
            }
        ];
    }

    function get_series_bar(data){
        function get_item_style(color){
            return {
                normal: {
                    color: color,
                    label: {
                        show: true,
                        textStyle: {
                            fontWeight: 'bold'
                        }
                    }
                }
            };
        }

        return [
            {
                name: 'Prioridades',
                type: 'bar',
                itemStyle: get_item_style('rgba(0, 181, 173, 1)'),
                data: data.map(function (arr) {
                    if(arr[1] == null || arr[1] == undefined){
                        return 0;
                    }
                    return arr[1]
                })
            },
            {
                name: 'Promedio',
                yAxisIndex: 1,
                type: 'bar',
                itemStyle: get_item_style('rgba(182, 162, 222, 1)'),
                data: data.map(function (arr) {
                    if(arr[4] == null || arr[4] == undefined){
                        return 0;
                    }
                    return arr[4]
                })
            },
            {
                name: 'Requerida',
                type: 'bar',

                xAxisIndex: 1,
                itemStyle: get_item_style('rgba(0, 181, 173, 0.5)'),
                data: data.map(function (arr) {
                    if(arr[2] == null || arr[2] == undefined){
                        return 0;
                    }
                    return arr[2]
                })
            },
            {
                name: 'Beneficiados',
                yAxisIndex: 1,
                xAxisIndex: 1,
                type: 'bar',
                itemStyle: get_item_style('rgba(182, 162, 222, 0.5)'),
                data: data.map(function (arr) {
                    if(arr[3] == null || arr[3] == undefined){
                        return 0;
                    }
                    return arr[3]
                })
            }
        ]
    }

    angular.module('frontEnd')
      .controller('ResumenController', ['$scope', '$timeout', 'backEnd', function($scope, $timeout, backEnd){
        $scope.loading = false;
        $scope.sin_datos = true;
        $scope.checkFiltros = {
            ubicacionCheck: false,
            prioridadCheck: false,
            dncpCheck: false,
            estadoCheck: false
        };
        $scope.ubicacionCheck = true;
        require.config({
            paths: {
                echarts: 'static/echarts'
            }
        });
        require(
            [
                'echarts',
                'echarts/chart/funnel',   // load-on-demand, don't forget the Magic switch type.
                'echarts/chart/pie',
                'echarts/chart/bar',
                'echarts/chart/line'
            ], function(ec){
                echarts = ec;
            });

        $scope.activar_filtro = function () {
            $('#actualizar-resumen').transition('jiggle');
        };
        $scope.filterObject = {};
        $scope.data = {};
        $scope.departamentoSelected = '';
        $scope.estadosSeleccionados = {
            estado: '',
            informes: false
        };
        $scope.prioridadesSeleccionadas = {
          sanitarios: false,
          aulas: false,
          mobiliarios: false,
          otros: false
        };
        $scope.dncpSeleccionadas = {
          planificaciones: false,
          adjudicaciones: false
        };

        $scope.ubicacionesSeleccionadas = [];

        var cargarAnio = function(){
            $scope.anios = ['2012', '2015'];
        };
        cargarAnio();


        $scope.actualizarResumen = function(){
          $scope.loading = true;
          $scope.sin_datos = false;
          var resumen = {};
          resumen.anios = $scope.anioSelected;
          if($scope.checkFiltros.ubicacionCheck){
            resumen.ubicaciones = $scope.ubicacionesSeleccionadas;
          }
          if($scope.checkFiltros.prioridadCheck){
            resumen.prioridades = $scope.prioridadesSeleccionadas;
          }
          if($scope.checkFiltros.dncpCheck){
            resumen.dncp = $scope.dncpSeleccionadas;
          }
          if($scope.checkFiltros.estadoCheck){
            resumen.estado = $scope.estadosSeleccionados;
          }

          backEnd.resumen.get({params: resumen}, function(data){

              $scope.loading = false;

              $scope.data = data;

              var charts = [];
              var chart = undefined, options= undefined;

              //Texto Inicial
              $scope.rDepartamentos = [];
              $scope.rDistritos = [];
              $scope.rDistritosParent = [];
              $scope.rBarrios = [];
              $scope.rBarriosParent = [];
              var obtenerUbicacion = angular.element('#ubicacion').scope().obtenerTextoUbicacion;
              if($scope.data.ubicaciones && typeof (obtenerUbicacion) == 'function'){
                  var ubicaciones = $scope.data.ubicaciones;
                  $scope.rDepartamentos = ubicaciones
                      .filter(function(obj){return !!obj[0] && !obj[1] && !obj[2]})
                      .map(function(obj){return obtenerUbicacion(obj, true, true);});
                  $scope.rDistritos = ubicaciones
                      .filter(function(obj){return !!obj[0] && !!obj[1] && !obj[2]})
                      .map(function(obj){return obtenerUbicacion(obj, true, true);});
                  $scope.rDistritosParent = ubicaciones
                      .filter(function(obj){return !!obj[0] && !!obj[1] && !obj[2]})
                      .map(function(obj){return obtenerUbicacion(obj, false, false, ' ➜ ');});
                  $scope.rBarrios = ubicaciones
                      .filter(function(obj){return !!obj[0] && !!obj[1] && !!obj[2]})
                      .map(function(obj){return obtenerUbicacion(obj, true, true);});
                  $scope.rBarriosParent = ubicaciones
                      .filter(function(obj){return !!obj[0] && !!obj[1] && !!obj[2]})
                      .map(function(obj){return obtenerUbicacion(obj, false, false, ' ➜ ');});
              }

              //Graficos
              //tipo requerimiento
              var tipoRequerimiento = {};
              if(data.tipo_requerimiento){
                  var row = undefined;
                  for(var i = 0; i < data.tipo_requerimiento.length; i++){
                      //row = [tipo_requerimiento, cantidad_pedidos, cantidad_requerida_por_pedido, tipo_requerimiento_infraestructura]
                      row = data.tipo_requerimiento[i];
                      if(!tipoRequerimiento[row[0]]){
                          tipoRequerimiento[row[0]] = {}
                      }
                      if(!tipoRequerimiento[row[0]]['pedidos']){
                          tipoRequerimiento[row[0]]['pedidos'] = []
                      }
                      if(!tipoRequerimiento[row[0]]['requerida']){
                          tipoRequerimiento[row[0]]['requerida'] = []
                      }
                      tipoRequerimiento[row[0]]['pedidos'].push({name: row[3], value:row[1]});
                      tipoRequerimiento[row[0]]['requerida'].push({name: row[3],  value:row[2]});
                  }
              }
              $('.chart-item').css('height', '300px').parent().show();
              if(tipoRequerimiento['sanitario']){
                  //series
                  options = get_options_pie('Sanitarios', 'Tipo de Requerimientos',
                      ['NUEVO', 'REPARACION', 'ADECUACION'],
                      get_series_doble_pie('Cantidad de prioridades', tipoRequerimiento['sanitario']['pedidos'],
                                'Cantidad Requerida',  tipoRequerimiento['sanitario']['requerida']));
                  chart = echarts.init(document.getElementById('chart-sanitarios'), 'macarons');
                  chart.setOption(options);
                  charts.push(chart);
              }else{
                  $('#chart-sanitarios').parent().hide();
              }
              if(tipoRequerimiento['aulas']) {
                  //series
                  options = get_options_pie('Aulas', 'Tipo de Requerimientos',
                      ['NUEVO', 'REPARACION', 'ADECUACION'],
                      get_series_doble_pie('Pedidos', tipoRequerimiento['aulas']['pedidos'],
                          'Requerido', tipoRequerimiento['aulas']['requerida']));
                  chart = echarts.init(document.getElementById('chart-aulas'), 'macarons');
                  chart.setOption(options);
                  charts.push(chart);
              }else{
                  $('#chart-aulas').parent().hide();
              }
              if(tipoRequerimiento['otros']){
                  //series
                  options = get_options_pie('Otros espacios', 'Tipo de Requerimientos',
                      ['NUEVO', 'REPARACION', 'ADECUACION'],
                      get_series_doble_pie('Pedidos', tipoRequerimiento['otros']['pedidos'],
                                'Requerido',  tipoRequerimiento['otros']['requerida']));
                  chart = echarts.init(document.getElementById('chart-otros'), 'macarons');
                  chart.setOption(options);
                  charts.push(chart);
              }else{
                  $('#chart-otros').parent().hide();
              }
              if(data.beneficiarios.length > 0){
                  var $chart = $('#chart-mobiliarios');
                  var $chartParent = $chart.parent();
                  options = get_options_bar("Beneficiarios", "Fonacide",
                      ['Prioridades', 'Promedio', 'Requerida', 'Beneficiados'],
                      {'Prioridades':true, 'Requerida':false, 'Beneficiados':false, 'Promedio':true},
                      data.beneficiarios.map(function(arr){return arr[0]}),
                      get_series_bar(data.beneficiarios));
                  chart = echarts.init(document.getElementById('chart-mobiliarios'), 'macarons');
                  chart.setOption(options);
                  charts.push(chart);
              }else{
                  $('#chart-mobiliarios').parent().hide();
              }


              window.charts = charts;
              $(window).off("resize");
              $(window).resize(function(){
                for(var index in window.charts){
                    if(window.charts.hasOwnProperty(index)){
                        window.charts[index].resize();
                    }
                }
              });
              $timeout(function(){
                  $scope.$apply();
                  $('.dep-label').popup({
                    on: 'hover'
                  });
              },0, false);
          });

        };

    }]);
})();
