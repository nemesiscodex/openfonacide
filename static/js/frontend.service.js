(function() {
	/**
	 * Servicio backend utilizando la api de django rest
	 */
	angular.module('frontEnd')
		.service('backEnd', ['$resource', function($resource) {
			var backEndUrl = '';
			return {
				"establecimiento": $resource(backEndUrl + '../establecimiento/:id', {
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
				"prioridades": $resource(backEndUrl + '../prioridades/:id', {
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
				"establecimiento_short": $resource(backEndUrl + '../establecimiento/:id', {
					id: "@id",
					short: 'true'
				}, {
					query: {
						method: 'GET',
						isArray: true,
						cache: false
					}
				}),
				"institucion": $resource(backEndUrl + '../institucion/:id', {
					id: "@id"
				}, {
					query: {
						method: 'GET',
						isArray: true,
						cache: true
					}
				}),
				"comentarios": $resource(backEndUrl + '../comentarios/:id', {
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
						transformRequest: function(obj) {
							var str = [];
							for (var p in obj)
								str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
							return str.join("&");
						}
					}
				}),
				"filtros": $resource(backEndUrl + '../filtros/',{},
					{
						query: {
							method: 'GET',
							isArray: true,
							cache: false
						}
					}
				)
			}
		}]);

})();
