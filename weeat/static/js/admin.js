var we_eat_admin = angular.module('we_eat_admin',[]);

we_eat_admin.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

function mainController($scope, $http) {

	$http.defaults.xsrfCookieName = 'csrftoken';
	$http.defaults.xsrfHeaderName = 'X-CSRFToken'
	
	$scope.is_popup = false;
	$scope.popup_message = '';


	$scope.complete_order=function(_order){
		$http({
        	url: '/chef/update_order/',
        	method: "POST",
        	headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        	data: $.param({
            	order: _order
        		})
    		}).success(function(data) {
    			$scope.is_popup = true;
    			$scope.popup_message=data.message;
    			$('#order_'+_order).remove();
            })
            .error(function(data) {
                $scope.is_popup = true;
    			$scope.popup_message=data.message;
            });
    };

    $scope.hide_popup=function(){
    	$scope.is_popup = false;
    };

};

we_eat_admin.controller('mainController',mainController);