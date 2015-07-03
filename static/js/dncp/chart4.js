   function changeData(data){
    
    for(var i = 0; i < data.length; i++){
        if(data[i].hasOwnProperty("cantidad")){
            data[i]["value"] = data[i]["cantidad"];
            delete data[i]["cantidad"];
        }

        if(data[i].hasOwnProperty("tipo_procedimiento")){
            data[i]["name"] = data[i]["tipo_procedimiento"];
            delete data[i]["tipo_procedimiento"];
        }
  


        
    }

   
}


   function grafica4( datos, anio, opcion,url) {


    changeData(datos);

    // configure for module loader
        require.config({
            paths: {
                echarts:  'static/echarts'
            }
        });

        require(
            [
                'echarts',
                'echarts/chart/pie' // require the specific chart type
            ],
            function (ec) {
                // Initialize after dom ready
                var myChart = ec.init(document.getElementById('main1')); 
                
       option = {
    title : {
        text: 'Tipo de procedimiento del llamado mas utilizado por ' + opcion + 'en el año ' + anio,
        subtext: '',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
   
    toolbox: {
        show : true,
        feature : {
            mark : {show: false},
            dataView : {show: false, readOnly: false},
            magicType : {
                show: false, 
                type: ['pie', 'funnel'],
                option: {
                    funnel: {
                        x: '25%',
                        width: '50%',
                        funnelAlign: 'left',
                        max: 1548
                    }
                }
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    series : [
        {
            name:'Categoria',
            type:'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:datos
        }
    ]
};
                                                     
        
                // Load data into the ECharts instance 
                myChart.setOption(option); 
            }
        );


}