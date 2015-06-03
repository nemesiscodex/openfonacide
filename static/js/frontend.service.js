(function () {
    /**
     * Servicio backend utilizando la api de django rest
     */
    angular.module('frontEnd')
        .service('backEnd', ['$resource', function ($resource) {
            var backEndUrl = '';
            return {
                "establecimiento": $resource('establecimiento/:id', {
                    id: "@id"
                }, {
                    query: {
                        method: 'GET',
                        isArray: true,
                        cache: true
                    },
                    get: {
                        method: 'GET',
                        isArray: false,
                        cache: true
                    }
                }),
                "prioridades": $resource('prioridades/:id', {
                    id: "@id"
                }, {
                    query: {
                        method: 'GET',
                        isArray: true,
                        cache: false
                    },
                    get: {
                        method: 'GET',
                        isArray: false,
                        cache: false
                    }
                }),
                //"establecimiento_short": $resource('establecimiento/:id', {
                "establecimiento_short": $resource('establecimiento/:id', {
                    id: "@id",
                    short: 'true'
                }, {
                    query: {
                        method: 'GET',
                        isArray: true,
                        cache: false
                    }
                }),
                "institucion": $resource('institucion/:id', {
                    id: "@id"
                }, {
                    query: {
                        method: 'GET',
                        isArray: true,
                        cache: true
                    }
                }),
                "comentarios": $resource('comentarios/:id', {
                    id: "@id"
                }, {
                    get: {
                        method: 'GET',
                        isArray: true,
                        cache: false
                    },
                    save: {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        transformRequest: function (obj) {
                            var str = [];
                            for (var p in obj)
                                str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                            return str.join("&");
                        }
                    }
                }),
                "filtros": $resource('filtros/', {},
                    {
                        query: {
                            method: 'GET',
                            isArray: true,
                            cache: false
                        }
                    }
                ),
                "resumen": $resource('_resumen/', {},
                    {
                        query: {
                            method: 'GET',
                            isArray: true,
                            cache: false
                        }
                    }
                ),
                "ubicaciones": $resource('ubicacion.json', {},
                    {
                        get: {
                            method: 'GET',
                            isArray: true,
                            cache: true
                        }
                    }
                ),
                "temporal": $resource('temporal/', {},
                    {
                        get: {
                            method: 'GET',
                            isArray: true,
                            cache: true
                        },
                        save: {
                            // Especificar
                            method: 'POST',
                            cache: false,
                            headers: {
                                //'Content-Type': 'application/x-www-form-urlencoded'
                                'Content-Type': 'application/json'
                            }
                        }
                    }
                ),
                "institucionapi": $resource('api/v1/institucion/:id', {id: "@id"},
                    {
                        get: {
                            method: 'GET',
                            cache: false
                        }
                    }
                )
            }
        }]);

})();
