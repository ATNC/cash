angular.module('cashApp')
    .directive('mainPage', [function () {
        return {
            restrict:'E',
            templateUrl: '/static/views/partials/start.html',
            controllerAs: 'ctrl',

            controller: function ($scope, cardDetails, $state) {
                var errors = {
                    "not_found":'Карта не найдена',
                    "block": 'Карта заблокирована',
                    "invalid_pwd": "Не правильный пароль"
                };
                $scope.card = {
                    cards_num:undefined,
                };
                $scope.error = false;
                $scope.show_pin = false;
                $scope.key_direct = 'cards_num';
                $scope.key_length = 19;
                $scope.getNum = function () {
                    $scope.error = false;
                    $scope.show_pin = false;

                    cardDetails.getCard($scope.card)
                        .then(
                            function (response) {
                                console.log(response)

                                if (angular.isUndefined(response.data.success)) {
                                    $scope.message = errors[response.data.error];
                                    //$scope.error = true;
                                } else {
                                    $scope.key_direct = 'cards_pin';
                                    $scope.key_length = 4;

                                    $scope.show_pin = true
                                }
                            }
                    )


                };

                $scope.tryAuth = function () {
                    cardDetails.getCard($scope.card)
                        .then(
                        function (response) {


                            if (angular.isUndefined(response.data.success)) {
                                var count = response.data.count;
                                if (count > 0) {
                                    $scope.message = errors[response.data.error] + " " +
                                    "До блокирования осталось " + count + " попыток";
                                        $scope.error = true;
                                } else {
                                    $scope.message = errors['block'];
                                    //$scope.error = true;
                                }

                            } else {
                                $state.go('account')
                            }
                        }

                    )

                }
            },

        }
    }])

    .directive('cabinet', [function () {
        return {
            restrict:'E',
            templateUrl: '/static/views/partials/actions.html',
            controllerUs: 'cabinet',
            controller: function ($scope, $state, $http, cardDetails) {
                $scope.info = {};
                $scope.balance = false;
                $scope.date = new Date();
                cardDetails.getInfo().then(
                    function (response) {
                       if (!angular.isUndefined(response.data.info)) {
                                 $scope.info = response.data.info

                        } else {
                            $state.go('app')
                        }
                });
                $scope.getBalance = function (code,sum) {
                    var data = {
                        'code': code,
                        'sum': sum || 'None'
                    };
                    cardDetails.addTransaction(data).
                        then(
                            function (response) {
                                console.log(response)
                            }
                    )
                };
                $scope.logout = function () {
                    cardDetails.logout().then(
                        function (response) {
                            $state.reload();
                        }
                    )
                }
            }
        }
    }])
    .directive('money', [function () {
        return {
            restrict:'E',
            templateUrl: '/static/views/partials/money.html',
            controller: function ($scope, $state, $http, cardDetails) {
                $scope.card = {};
                $scope.key_length = 19;
                $scope.info = {}
                $scope.balance = false;
                $scope.key_direct = 'money';
                $scope.date = new Date();
                cardDetails.getInfo().then(
                    function (response) {
                        if (!angular.isUndefined(response.data.info)) {
                                 $scope.info = response.data.info


                        } else {
                            $state.go('app')
                        }
                });
                $scope.getMoney = function (code,sum) {
                    if (!angular.isUndefined($scope.card.money) && $scope.card.money < $scope.info.card_balance) {
                         var data = {
                            'code': code,
                            'sum': $scope.card.money
                        };
                        cardDetails.addTransaction(data).
                            then(
                                function (response) {
                                    $scope.success = true;
                                },
                            function (response) {
                                console.log('eqwewqe')

                            }

                        )
                        } else {
                            $scope.message = angular.isUndefined($scope.card.money) ? '' : 'Запрашиваемая сумма превышает Ваш лимит'
                        }
                };
                $scope.logout = function () {
                    cardDetails.logout().then(
                        function (response) {
                            $state.reload();
                        }
                    )
                }
            }
        }
    }])
    .directive('keypad', [function () {
            return {
                restrict:'E',
                templateUrl: '/static/views/keypad.html',
                controller: function ($scope) {
                    $scope.append = function (num) {
                        $scope.message = '';
                        if (!angular.isUndefined($scope.card[$scope.key_direct]) && $scope.card[$scope.key_direct].length >=$scope.key_length) {
                            return
                        }
                        if (angular.isUndefined($scope.card[$scope.key_direct])) {

                            $scope.card[$scope.key_direct] = num
                        }
                        else {
                            var len = $scope.card[$scope.key_direct].length,
                                arr = [4, 9, 14];
                            if ( arr.indexOf(len) >= 0 ) {

                                $scope.card[$scope.key_direct] = $scope.card[$scope.key_direct] + "-" + num

                            } else {
                                $scope.card[$scope.key_direct] = $scope.card[$scope.key_direct] + num

                            }

                        }
                    }

                    $scope.clear = function () {
                        if (!angular.isUndefined($scope.card[$scope.key_direct])) {
                            $scope.message = '';
                            $scope.card[$scope.key_direct] = undefined;
                        }
                    }
                }
            }
        }])

        .directive('keypadMoney', [function () {
                    return {
                        restrict:'E',
                        templateUrl: '/static/views/keypad_money.html',
                        controller: function ($scope) {
                            $scope.append = function (num) {
                                $scope.message = ''
                                if (!angular.isUndefined($scope.card[$scope.key_direct]) && $scope.card[$scope.key_direct].length >=20) {
                                    return
                                }
                                if (angular.isUndefined($scope.card[$scope.key_direct])) {

                                    $scope.card[$scope.key_direct] = num
                                }
                                else {
                                        $scope.card[$scope.key_direct] = $scope.card[$scope.key_direct] + num
                                }
                            };

                            $scope.clear = function () {
                                if (!angular.isUndefined($scope.card[$scope.key_direct])) {
                                    $scope.message = '';
                                    $scope.card[$scope.key_direct] = undefined;
                                }
                            }
                        }
                    }
                }])

