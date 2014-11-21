var we_eat = angular.module('we_eat', []);

we_eat.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

function mainController($scope, $http) {

    // Configuración
    $scope.formData = {};
    $scope.navigation = [];
    //$scope.url_base = 'http://we-eat.herokuapp.com/';
    $scope.url_base = 'http://127.0.0.1:8000/';
    $scope.url_image = 'https://s3.amazonaws.com/weeat/media/';


    // Navegación
    $scope.breadcrumbs = [];
    $scope.is_show_banner = false;
    $scope.is_categories = true;
    $scope.is_foods = false;
    $scope.is_detail_foods = false;
    $scope.is_cart_shop = false;
    
    // Contexto
    $scope.cart_shop = [];
    $scope.current_food;

    $http.defaults.headers.common['Authorization'] = 'Basic cm9vdDpJbmdfZGhlcnJlcmFfOTA=';
    $http.defaults.headers.common['Accept'] = 'application/json';
    $http.defaults.headers.common['Content-Type'] = 'application/json';

    // Cuando se cargue la página, pide del API todos los TODOs
   $http.get($scope.url_base+'api/v1/categories/')
        .success(function(data) {
            $scope.categories = data;
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });

    $http.get($scope.url_base+'api/v1/restaurants/1/foods/')
        .success(function(data) {
            $scope.foods = data;
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });

    $scope.back=function(){
        if($scope.navigation.length > 1 ){
            $scope.navigation.pop();
            toShow=$scope.navigation.pop();

            toShow.event.apply(this,toShow.params);
        }
    }

    // Adiciona un item a la orden 
    $scope.add_cart_shop=function(_food){

        count = prompt('Digite la cantidad:');

        $scope.cart_shop.push({'food':_food,'count':count});
    };

    // Visualizar el listado de categorias del restaurante
    $scope.view_categories=function(){
        $scope.hide_view();
        $scope.is_categories = true;
        $scope.navigation.push({
            event:$scope.view_categories, 
            params: []
        });   
    }

    // Visualizar los platos de la categoria seleccionada
    $scope.view_foods=function(_id,_name){
        $scope.foods_categories = [];
        for(i in $scope.foods){
            for(j in $scope.foods[i].categorie){
                if($scope.foods[i].categorie[j] == _id){
                    $scope.foods_categories.push($scope.foods[i]);
                }
            }
        }
        $scope.hide_view();
        $scope.is_foods = true;
        $scope.name_categorie=_name;
        $scope.navigation.push({
            event: $scope.view_foods,
            params: [_id,_name]
        });
    };

    // Visualizar el datalle de un plato seleccionado
    $scope.view_food_detail=function(_food){
        $scope.current_food=_food;
        $scope.hide_view();
        $scope.is_detail_foods = true;
        $scope.navigation.push({
            event:$scope.view_food_detail,
            params:[_food]
        });
    }

    // Visualizar el listado de platos en la orden
    $scope.view_order=function(){
        $scope.hide_view();
        $scope.is_cart_shop = true;
        $scope.navigation.push({
            event:$scope.view_order, 
            params: []
        });   
    }

    // Oculta todos los views
    $scope.hide_view=function(){
        $scope.is_categories = false;
        $scope.is_foods = false;
        $scope.is_detail_foods = false;
        $scope.is_cart_shop = false;
    };


    $scope.navigation.push({
        event: $scope.view_categories,
        params: []
    });

    // envia la petición al servidor para tramitar la orden 
    $scope.send_order=function(){

        list_order = [];
        for(i in $scope.cart_shop){
            list_order.push({
                'food':$scope.cart_shop[i].food.id,
                'count':$scope.cart_shop[i].count
            });
        }

        $http.post($scope.url_base+'api/v1/orders/1/add/', {
            "foods": list_order, 
            "comment": "sin ensalada por favor"
            })
            .success(function(data) {
                $scope.formData = {};
                $scope.todos = data;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error:');
                console.log(data);
            });
    };

    $scope.remove_decimal=function(value){
        return value.replace(/(\.\d+)+/,'');
    }

    $scope.show_banner=function(){

        if(!$scope.is_show_banner){
            $scope.is_show_banner = true;
            $('div.container').css({'width':'80%','margin-left': '20%'});
            $('div.banner').css({'margin-left':'0'});
        }else{
            $scope.is_show_banner = false;
            $('div.container').css({'width':'100%','margin-left': '0'});
            $('div.banner').css({'margin-left':'-20%'});
        }
    }
}

we_eat.filter('noFractionCurrency',
    [ '$filter', '$locale', function(filter, locale) {
      var currencyFilter = filter('currency');
      var formats = locale.NUMBER_FORMATS;
      return function(amount, currencySymbol) {
        var value = currencyFilter(amount, currencySymbol);
        var sep = value.indexOf(formats.DECIMAL_SEP);
        console.log(amount, value);
        if(amount >= 0) { 
          return value.substring(0, sep);
        }
        return value.substring(0, sep) + ')';
      };
    } ]);

we_eat.controller('mainController',mainController);