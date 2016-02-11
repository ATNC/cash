angular.module('cashApp')
    .factory('cardDetails', [
        '$http', function ($http) {

            var api = {};

            //ne rest
            //
            api.getCard = function (data) {
                return $http.get('/get_card', {
                    params: {data:data}
                })

            };
            //api.getCard = function (data) {
            //    return $http.get('/test/'+data.cards_num.replace(/\-/g, ''),
            //        {
            //            params: {data:data}
            //        })
            //
            //};





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
