    // configure for module loader
        require.config({
            paths: {
                echarts: '/static/js/build/dist'
            }
        });

        require(
            [
                'echarts',
                'echarts/chart/bar' // require the specific chart type
            ],
            function (ec) {
                // Initialize after dom ready
                var myChart = ec.init(document.getElementById('main1')); 
                
   option = {
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 
            type : 'shadow'        // On hover stack: 'line' | 'shadow'
        }
    },
    legend: {
        data:['Contratacion Directa', 'licitacion publica','concuso de ofertas','ASu','Lic 2']
    },
    toolbox: {
        show : true,
         orient : 'vertical',
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'value'
        }
    ],
    yAxis : [
        {
            type : 'category',
            data : ['Asuncion','San Lorenzo','Capiata','Caazapa','Limpio','Ciudad del Este','Encarnacion']
        }
    ],
    series : [
        {
            name:'Contratacion Directa',
            type:'bar',
            stack: 'true',
            itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
            data:[320, 302, 301, 334, 390, 330, 320]
        },
        {
            name:'licitacion publica',
            type:'bar',
            stack: 'true',
            itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'concuso de ofertas',
            type:'bar',
            stack: 'true',
            itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
            data:[220, 182, 191, 234, 290, 330, 310]
        },
        {
            name:'ASu',
            type:'bar',
            stack: 'true',
            itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
            data:[150, 212, 201, 154, 190, 330, 410]
        },
        {
            name:'Lic 2',
            type:'bar',
            stack: 'true',
            itemStyle : { normal: {label : {show: true, position: 'insideRight'}}},
            data:[820, 832, 901, 934, 1290, 1330, 1320]
        }
    ]
};
                                     
        
                // Load data into the ECharts instance 
                myChart.setOption(option); 
            }
        );
