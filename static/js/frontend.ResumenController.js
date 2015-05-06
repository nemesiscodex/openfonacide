(function(){
    angular.module('frontEnd')
      .controller('ResumenController', ['$scope', '$timeout', function($scope, $timeout){
        $scope.filterObject = {};
        $scope.departamentoSelected = '';
        $scope.prioridadesSeleccionadas = {
          sanitarios: false,
          aulas: false,
          mobiliarios: false,
          otros: false
        };
        $scope.dncpSeleccionadas = {
          adjudicados: false,
          informes: false
        };

        $scope.ubicacionesSeleccionadas = [];

        var cargarAnio = function(){
          var anios = ['2012','2013','2014','2015'];
          $scope.anios = anios;
        };
        cargarAnio();

        var cargarUbicacion = function(){
          //PLACEHOLDER
          var ubicaciones = [
            {
              "id": "0",
              "nombre": "Asuncion",
              "distritos": [
                 {
                   "id": "0",
                   "nombre": "Asuncion",
                   "barrios": [
                     {
                       "id": "1",
                       "nombre": "Villa Aurelia"
                     },
                     {
                       "id": "2",
                       "nombre": "Mariscal Estigarribia"
                     },
                     {
                       "id": "3",
                       "nombre": "Villa Morra"
                     }
                   ]
                 },
                  {
                    "id": "1",
                    "nombre": "Distrito 2",
                    "barrios": [
                      {
                        "id": "4",
                        "nombre": "Barrio 4"
                      },
                      {
                        "id": "5",
                        "nombre": "Barrio 5"
                      },
                      {
                        "id": "6",
                        "nombre": "Barrio 6"
                      }
                    ]
                  },
             ]
            },
          ];
          $scope.distritos = [];
          $scope.barrios = [];
          $scope.ubicaciones = ubicaciones;
          $scope.$watch('departamentoSelected', function(){
            $scope.distritos = [];
            $scope.distritoSelected = "";
            $scope.barrioSelected = "";
            for(i in $scope.ubicaciones){
              if($scope.ubicaciones[i].id == $scope.departamentoSelected){
                $scope.distritos = $scope.ubicaciones[i].distritos;
                break;
              }
            }
            //Esto es por https://docs.angularjs.org/error/$rootScope/inprog?p0=$digest#triggering-events-programmatically
            $timeout(function(){
              $('#ubicacion-distrito .dropdown,#ubicacion-barrio .dropdown').dropdown('clear');
            },0,false);

          });
          $scope.$watch('distritoSelected', function(){
            $scope.barrios = [];
            $scope.barrioSelected = "";
            for(i in $scope.distritos){
              if($scope.distritos[i].id == $scope.distritoSelected){
                $scope.barrios = $scope.distritos[i].barrios;
                break;
              }
            }
            $timeout(function(){
              $('#ubicacion-barrio .dropdown').dropdown('clear');
            },0,false);
          });

          $timeout(function(){
            // $('.ui.checkbox').checkbox();
            $('.dropdown').dropdown();
          },300, false);
        };
        cargarUbicacion();
        $scope.agregarUbicacion = function(){
          if(!$scope.departamentoSelected){
            return;
          }
          var flecha = " &#x279c; ";
          var seleccion = "";
          if($scope.ubicacionesSeleccionadas
            .filter(function(obj){
              return obj[0] == $scope.departamentoSelected
                &&  obj[1] == $scope.distritoSelected
                &&  obj[2] == $scope.barrioSelected;
            }).length > 0){
              return;
          }
          $scope.ubicacionesSeleccionadas.push(
            [$scope.departamentoSelected, $scope.distritoSelected, $scope.barrioSelected]
          );
          var depObj, disObj, barObj;

          depObj = $scope.ubicaciones
            .filter(function(obj){
              return obj.id == $scope.departamentoSelected;
              });
          seleccion += depObj
            .map(function(obj){
              return obj.nombre;
              })
            .reduce(function(a,b){
              return a+b;
              });

          depObj = depObj[0];
          if($scope.distritoSelected){
            disObj = depObj.distritos
              .filter(function(obj){
                return obj.id == $scope.distritoSelected;
                });
            seleccion += flecha + disObj
              .map(function(obj){
                return obj.nombre;
                })
              .reduce(function(a,b){
                return a+b;
                });
            disObj = disObj[0];
          }
          if($scope.barrioSelected){
            barObj = disObj.barrios
              .filter(function(obj){
                return obj.id == $scope.barrioSelected;
                });
            seleccion += flecha + barObj
              .map(function(obj){
                return obj.nombre;
                })
              .reduce(function(a,b){
                return a+b;
                });
              barObj = barObj[0];
          }
          $('#ubicacion-labels').append(
            $('<div class="ui label" style="margin-bottom: 5px" data-dep="'+$scope.departamentoSelected+'" data-dis="'+$scope.distritoSelected+'" data-bar="'+$scope.barrioSelected+'"></div>')
              .html(seleccion)
              .append(
                $('<i class="delete icon"></i>')
                .click(function(){
                  var label = $(this).parent();
                  $scope.ubicacionesSeleccionadas = $scope.ubicacionesSeleccionadas
                    .filter(function(obj){
                      return !(obj[0] == $scope.departamentoSelected
                        &&  obj[1] == $scope.distritoSelected
                        &&  obj[2] == $scope.barrioSelected);
                    });
                  label.remove();
                  $scope.$digest();
                })
              )
            );
        };

        $scope.limpiarUbicacion = function(){
          $timeout(function(){
            $('#ubicacion .ui.dropdown').dropdown('clear');
          }, 0, false);
        };

        $scope.borrarUbicaciones = function(){
          $scope.ubicacionesSeleccionadas = [];
          $timeout(function(){
            $('#ubicacion-labels .ui.label').remove();
            $scope.$digest();
          }, 0, false);
        };

        $scope.actualizarResumen = function(){
          var resumen = {};
          resumen.anios = $scope.anioSelected;
          if($scope.ubicacionCheck){
            resumen.ubicaciones = $scope.ubicacionesSeleccionadas;
          }
          if($scope.prioridadCheck){
            resumen.prioridades = $scope.prioridadesSeleccionadas;
          }
          if($scope.dncpCheck){
            resumen.dncp = $scope.dncpSeleccionadas;
          }
          if($scope.estadoCheck){
            resumen.estado = $scope.estadosSelected;
          }
          console.log(resumen);
          var charts = [];
          var config = {
            xAxis: [
              {
                type: 'category',
                data: ['Aulas', 'Sanitarios', 'Mobiliarios', 'Otros Espacios']
              }
            ],
            yAxis: [
              {
                type: 'value'
              }
            ],
            legend: {
              data: ['Nuevo', 'Reparación']
            },
            series: [
              {
                name: 'Nuevo',
                type: 'bar',
                itemStyle: {
                  normal: {
                    label: {
                      show: true,
                      position: 'inside',
                      textStyle: {
                        fontSize: '15',
                        fontWeight: 'bold'
                      }
                    }
                  }
                },
                data: [2400, 2100, 3300, 1500]
              },
              {
                name: 'Reparación',
                type: 'bar',
                itemStyle: {
                  normal: {
                    label: {
                      show: true,
                      position: 'inside',
                      textStyle: {
                        fontSize: '15',
                        fontWeight: 'bold'
                      }
                    }
                  }
                },
                data: [5400, 3500, 0, 4590]
              }
            ],
            tooltip : {
              trigger: 'axis'
            },
          };

          $('.chart.card').show();
          $('.chart-item').css('height', '300px');
          $('.chart-item').each(function(id, el){
            var chart = echarts.init(el, 'macarons');

            chart.setOption(config);
            charts.push(chart);
          });
          window.charts = charts;
          $(window).off("resize");
          $(window).resize(function(){
            for(index in window.charts){
              charts[index].resize();
            }
          })
        };

    }]);
})();
