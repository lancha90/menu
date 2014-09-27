var we_eat = angular.module('we_eat', []);

we_eat.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


function mainController($scope, $http) {
    // Configuración
    $scope.formData = {};
    $scope.navigation = [];
    $scope.url_image = 'http://we-eat.herokuapp.com/static/css/image/';


    // Navegación
    $scope.breadcrumbs = [];
    $scope.is_categories = true;
    $scope.is_foods = false;
    $scope.is_detail_foods = false;
    $scope.is_cart_shop = false;
    
    // Contexto
    $scope.cart_shop = [];
    $scope.current_food;

    $http.defaults.headers.common['Authorization'] = 'Basic cm9vdDpJbmdfZGhlcnJlcmFfOTA=';
    $http.defaults.headers.common['Accept'] = 'application/json';

    // Cuando se cargue la página, pide del API todos los TODOs
   $http.get('http://we-eat.herokuapp.com/api/v1/categories/')
        .success(function(data) {
            $scope.categories = data;
        })
        .error(function(data) {
            console.log('Error: ' + data);
        });

    $http.get('http://we-eat.herokuapp.com/api/v1/restaurants/1/foods/')
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
        $scope.cart_shop.push(_food);
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

    // Cuando se añade un nuevo TODO, manda el texto a la API
    /*$scope.createTodo = function(){
        $http.post('/api/todos', $scope.formData)
            .success(function(data) {
                $scope.formData = {};
                $scope.todos = data;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error:' + data);
            });
    };

    // Borra un TODO despues de checkearlo como acabado
    $scope.deleteTodo = function(id) {
        $http.delete('/api/todos/' + id)
            .success(function(data) {
                $scope.todos = data;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error:' + data);
            });
    };*/
}


we_eat.controller('mainController',mainController);