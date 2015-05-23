    // configure for module loader
        require.config({
            paths: {
               echarts: './js/build/dist'
            }
        });

        require(
            [
                'echarts',
                'echarts/chart/pie' // require the specific chart type
            ],
            function (ec) {
                // Initialize after dom ready
                var myChart = ec.init(document.getElementById('main4')); 
  var idx = 1;
option = {
    timeline : {
        data : [
            '2013-01-01', '2013-02-01', '2013-03-01', '2013-04-01', '2013-05-01',
            { name:'2013-06-01', symbol:'emptyStar6', symbolSize:8 },
            '2013-07-01', '2013-08-01', '2013-09-01', '2013-10-01', '2013-11-01',
            { name:'2013-12-01', symbol:'star6', symbolSize:8 }
        ],
        label : {
            formatter : function(s) {
                return s.slice(0, 7);
            }
        }
    },
    options : [
        {
            title : {
                text: '',
                subtext: ''
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                data:['Contratacion Directa','licitacion publica','concuso de ofertas','Subasta a la Baja Electrónica','Lic3']
            },
            toolbox: {
                show : true,
                 orient : 'vertical',
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {
                        show: true, 
                        type: ['pie', 'funnel'],
                        option: {
                            funnel: {
                                x: '25%',
                                width: '50%',
                                funnelAlign: 'left',
                                max: 1700
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
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    center: ['50%', '45%'],
                    radius: '50%',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        },
        {
            series : [
                {
                    name:'Porcentaje por tipo de procedimiento',
                    type:'pie',
                    data:[
                        {value: idx * 128 + 80,  name:'Contratacion Directa'},
                        {value: idx * 64  + 160,  name:'licitacion publica'},
                        {value: idx * 32  + 320,  name:'concuso de ofertas'},
                        {value: idx * 16  + 640,  name:'Subasta a la Baja Electrónica'},
                        {value: idx++ * 8  + 1280, name:'Lic3'}
                    ]
                }
            ]
        }
    ]
};
                    
                                     
        
                // Load data into the ECharts instance 
                myChart.setOption(option); 
            }
        );
