seedApp = angular.module 'seedApp',[]
seedApp.controller 'seedCtrl',['$scope','$http',
    ($scope,$http) ->
        $http.get('/questions')
             .success( 
            (r) ->
                $scope.questions= r.question_files
            )

]
