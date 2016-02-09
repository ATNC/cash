angular.module('cashApp')
    .factory('cardDetails', [
        '$http', function ($http) {

            var api = {};

            api.getCard = function (data) {
                return $http.post('/', {data:data})

            };
            api.getInfo = function () {
                return $http.get('/get_id')
            };
            api.addTransaction = function (code) {
                return $http.get('/add_transaction', {
                    params: {data: code}
                })
            };
            api.logout = function () {
                return $http.get('/logout')
            };

            return api

        }
    ]);