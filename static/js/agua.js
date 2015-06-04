function calcular_abastecimiento(){
          tipo_abastecimiento =  $( "input:checked" ).next().html();
          $('.tipo_abastecimiento').html(tipo_abastecimiento);
          console.log(tipo_abastecimiento);
          

         resultado =  $.grep( abastecimiento , function( n, i ) {
            return n.abastecimiento_agua===tipo_abastecimiento;
          });

         cantidad_tipo_abastecimiento = 0;

         for (i = 0; i < resultado.length; i++) {  //loop through the array
            cantidad_tipo_abastecimiento += resultado[i].cantidad;  //Do the math!
          }

          $('.cantidad_tipo_abastecimiento').html(cantidad_tipo_abastecimiento);

        porcentaje_tipo_abastecimiento = (cantidad_tipo_abastecimiento*100)/total_instituciones;
        gota(porcentaje_tipo_abastecimiento);

        




}

function gota(porcentaje) {

  $("#fillgauge1").html('');

    loadLiquidFillGauge("fillgauge1", porcentaje);
    var config1 = liquidFillGaugeDefaultSettings();
    config1.circleColor = "";
    config1.textColor = "#FF4444";
    config1.waveTextColor = "#FFAAAA";
    config1.waveColor = "#FFDDDD";
    config1.circleThickness = 0;
    config1.textVertPosition = 0.2;
    config1.waveAnimateTime = 1000;
    loadLiquidFillGauge("fillgauge2", 28, config1);
};




function mapa (datos) {



function changeData(data, tipo_abastecimiento){
    
    for(var i = 0; i < data.length; i++){
        if(data[i].hasOwnProperty("cantidad")){
            data[i]["value"] = data[i]["cantidad"];
            delete data[i]["cantidad"];
        }

        if(data[i].hasOwnProperty("nombre_departamento")){
            data[i]["name"] = data[i]["nombre_departamento"];
            delete data[i]["nombre_departamento"];
        }
        delete data[i]["codigo_departamento"];

        delete data[i]["abastecimiento_agua"];


        
    }

   
}

changeData(datos);
console.log(datos);




  
   $('.modal-mapa').modal('show');
    require.config({

      paths: {
                echarts: 'static/echarts'
            },


                    
                });

       
        
        // use



        require(
            [
                 'echarts',
                'echarts/chart/map',   // load-on-demand, don't forget the Magic switch type.
              
            ],
            function (ec) {
                // Initialize after dom ready
                var myChart = ec.init(document.getElementById('main-map'));

                option = {
                          title : {
                               text: tipo_abastecimiento,
                              subtext: 'Tipo de abastecimiento de agua',
                              sublink: 'http://datos.mec.gov.pyl',
                              x:'right'
                          },
                          tooltip : {
                              trigger: 'item',
                              showDelay: 0,
                              transitionDuration: 0.2,
                              formatter : function (params) {
                                  var value = (params.value + '').split('.');
                                  value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');
                                  return params.seriesName + '<br/>' + params.name + ' : ' + value;
                              }
                          },
                          dataRange: {
                              x : 'right',
                              min: 0,
                              max: 300,
                              color: ['blue','teal','lightskyblue'],
                              text:['High','Low'],           
                              calculable : true
                          },
                          toolbox: {
                              show : true,
                              //orient : 'vertical',
                              x: 'left',
                              y: 'top',
                              feature : {
                                  mark : {show: false},
                                  dataView : {show: false, readOnly: false},
                                  restore : {show: true},
                                  saveAsImage : {show: true}
                              }
                          },
                          series : [
                              {
                                  name: tipo_abastecimiento,
                                  type: 'map',
                                  roam: true,
                                  mapType: 'PRY', // 自定义扩展图表类型
                                  itemStyle:{
                                      emphasis:{label:{show:true}}
                                  },
                                  
                                  data: datos
                              }
                          ]
                      }; 
                             
             require('echarts/util/mapData/params').params.PRY = {
            getGeoJson: function (callback) {
                $.getJSON('static/js/geoJson/py-dptos.json', callback);
            }
        };         
              
                // Load data into the ECharts instance 
                myChart.setOption(option); 
            }
       );


};
