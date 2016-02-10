angular.module('cashApp', ['ui.router', 'ngResource', 'ngCookies', 'ui.mask'])
    .config(['$httpProvider', '$interpolateProvider',function($httpProvider, $interpolateProvider) {
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    }])

    .config(function($stateProvider, $urlRouterProvider ) {
        $stateProvider

            // route for the home page
            .state('app', {
                 //abstract: true,
                url:'/',
                templateUrl : '/static/views/home.html',
                        //controller  : 'IndexController'



            });
$stateProvider
            // route for the aboutus page
            .state('account', {
                url:'/account',
                //abstract:true,

                templateUrl : '/static/views/account.html',
                resolve: {
                    first: function ($q, $http, $state) {
                        var deferred = $q.defer();
                        $http.get('/get_id').then(
                            function (response) {
                                if (angular.isUndefined(response.data.info)) {
                                    $state.go('app');
                                   deferred.reject(response.data)
                                } else {
                                    deferred.resolve(response.data)
                                }
                            }
                        );
                        return deferred.promise;

                    }
                },


            })
            .state('account.money', {

                url:'/money',
                views : {
                    '@': {
                        templateUrl : '/static/views/account.money.html'
                    },

                }
                //resolve: {
                //    first: function ($q, $http, $state) {
                //        var deferred = $q.defer();
                //        $http.get('/get_id').then(
                //            function (response) {
                //                if (angular.isUndefined(response.data.info)) {
                //                    $state.go('app');
                //                   deferred.reject(response.data)
                //                } else {
                //                    deferred.resolve(response.data)
                //                }
                //            }
                //        );
                //        return deferred.promise;
                //
                //    }
                //},


            })



        ;


        $urlRouterProvider.otherwise('/');
    })

;