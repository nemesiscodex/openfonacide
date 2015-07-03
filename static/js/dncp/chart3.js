   function changeData1(data){


    
    for(var i = 0; i < data.length; i++){
          if(data[i].hasOwnProperty("categoria")){
            data[i]["name"] = data[i]["categoria"];
            delete data[i]["categoria"];
          
        }

        if(data[i].hasOwnProperty("cantidad")){
            data[i]["value"] = data[i]["cantidad"];
            delete data[i]["cantidad"];
            
        }

     
  


        
    }



   
}


   function grafica3( datos, anio, opcion,url) {


    changeData1(datos);

   

    // configure for module loader
        require.config({
            paths: {
                echarts: 'static/echarts'
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
        text: 'Categorías más solicitadas por ' + opcion + ' en el año ' + anio,
        subtext: opcion + '',
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