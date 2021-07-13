(function () {
  'use strict';
  
  
  angular.module('Searchapp', [])
  .controller('SearchappController', SearchappController);

PapyDeveloperController.$inject = ['$scope'];
function SearchappController($scope, $http) {
  $scope.searchingfunction = function() {
      if ($scope.search > 1){
          $http.get('/api/v1/results', $scope.search)
          .success(function()
            {
              $scope.search2 = "Showing Results For ";
              $scope.search2 += $scope.search;
              $scope.h1color = "whitesmoke";
              data_to_parse = response.data  
              var final
              for (i in data_to_parse)
              {
                var temp = i;
                temp.replace("'", '');
                var temp2 = temp.slice(12);
                temp2.concat('\n');
                final.concat(temp2);
                }
            $scope.ResultDiv = final;
            })
            .error(function(){
                alert('Failed! Please contact Support!')
            });
        
        }
        else{
            $scope.display = "none";
            $scope.search2 = "Please Enter Data First";
            $scope.h1color = "red";

        }
    
    }}})();